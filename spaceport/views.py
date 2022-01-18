from django.shortcuts import render, redirect, reverse
import requests
from django.conf import settings
from django.contrib.auth.models import User
from .models import List, Result
import os
from .forms import CreateList
from slugify import slugify
import datetime
from django.utils import timezone
import pytz


mapbox_key = os.environ.get('MAPBOX_KEY', '')
skywatch_key = os.environ.get('SKYWATCH_KEY', '')


# display the homepage
def homepage(request):
    return render(request, 'index.html')

# save the form
def save(request):

    form = CreateList(request.POST)

    # if the form is valid, save it
    if form.is_valid():
        #form.save(commit=False)
        print("is valid")
    
    # if it's not valid, return to form
    else:

        print(form)
       
        context = {
            'form': form,
            'validation': 'Form not valid',
        }

        return render(request, 'create_pipeline.html', context)

    return render(request, 'save.html')


# create a pipeline (CREATE)
def create(request):

    # current logged in user
    user = str(request.user)

    # if user posts the form
    if request.method == 'POST':

        # fill in form details with users values
        form = CreateList(request.POST)

        # if form is valid, save as object and call the pipeline
        # fill in other fields of object
        # redirect to detail view of object
        if form.is_valid():

            # put aoi into correct format
            format_aoi = form.cleaned_data['aoi']['features'][0]['geometry']

            # api url
            url = 'https://api.skywatch.co/earthcache/pipelines'

            # api parameters required
            params = {
                'name': form.cleaned_data['pipeline_name'],
                'interval': form.cleaned_data['interval'],
                'start_date': str(form.cleaned_data['start_date']),
                'output': {
                    'id': form.cleaned_data['output_image'],
                    'format': 'geotiff',
                    'mosaic': 'off'
                },
                'end_date': str(form.cleaned_data['end_date']),
                'aoi': format_aoi,
                'max_cost': 0,
                'min_aoi_coverage_percentage': 50,
                'result_delivery': {
                    'max_latency': '0d',
                    'priorities': [
                        'latest',
                        'highest_resolution',
                        'lowest_cost'
                    ]
                },
                'resolution_low': 30,
                'resolution_high': 10,
                'tags': []
            }

            print(params)

            # post the pipeline to the api
            try:
                post_pipeline = requests.post(
                    url,
                    headers={'x-api-key': skywatch_key},
                    json=params)
                post_response = post_pipeline.json()

                print(post_response)

            # don't use bare except
            except:
                print("Couldn't reach API")
                # redirect to page saying api could not be found

            # if the api returns errors in returning a response,
            # redirect to form page with error message
            # (should not happen due to form validation, Django + JS)
            if 'errors' in post_response or 'error' in post_response:

                form = CreateList(request.POST)
                # error message

                context = {
                    'form': form,
                    # error message
                }

            # if no errors in api response,
            # save form as object and fill in other fields
            else:

                form.save()

                # get the object id
                current_list = List.objects.latest('id')
                id = current_list.id

                api_id = post_response['data']['id']
                # current_list.slug = slugify(pipeline_name)
                current_list.created_by = user
                current_list.status = 'pending'
                current_list.api_id = api_id
                current_list.save()

                # direct user to detail view of this model
                return redirect(reverse('detail_view', args=[id]))

        # if form is not valid
        # return to form
        else:
            print('NOT VALID')

    form = CreateList()

    context = {
        'form': form,
    }

    return render(request, 'create_pipeline.html', context)


# display all the user's models
def my_pipelines(request):

    user = str(request.user)

    active_pipelines = List.objects.filter(status='active', created_by=user).order_by('date_created')
    complete_pipelines = List.objects.filter(status='complete', created_by=user).order_by('date_created')
    pending_pipelines = List.objects.filter(status='pending', created_by=user).order_by('date_created')
    saved_pipelines = List.objects.filter(status='saved', created_by=user).order_by('date_created')

    num_active_pipelines = len(active_pipelines)
    num_complete_pipelines = len(complete_pipelines)
    num_pending_pipelines = len(pending_pipelines)
    num_saved_pipelines = len(saved_pipelines)

    context = {
        'active': active_pipelines,
        'complete': complete_pipelines,
        'pending': pending_pipelines,
        'saved': saved_pipelines,
        'active_num': num_active_pipelines,
        'complete_num': num_complete_pipelines,
        'pending_num': num_pending_pipelines,
        'saved_num': num_saved_pipelines,
    }

    return render(request, 'my_pipelines.html', context)


# display view of this object (READ)
def detail_view(request, id):

    context = {
        'pipeline': List.objects.get(id=id),
        'results': Result.objects.filter(pipeline_id=id)
    }

    return render(request, 'detail_view.html', context)


# edit the pipeline (UPDATE)

# delete the pipeline (both from models & in api) (DELETE)

# refresh the pipeline from the api
# this is not the UPDATE aspect of CRUD (see view.edit)
def update(request, id):

    time_now = timezone.now()

    # get the api id of this object to post to api
    api_id = List.objects.get(id=id).api_id

    # api url to update the pipeline status
    url = (f'https://api.skywatch.co/earthcache/pipelines/{api_id}')
    list_response = requests.get(
        url,
        headers={
            'x-api-key': skywatch_key,
        }
    ).json()

    # get object to update
    update_list = List.objects.get(id=id)

    # update fields in List object  & save
    update_list.results_updated = time_now
    update_list.status = list_response['data']['status']
    update_list.save()

    url = (f'https://api.skywatch.co/earthcache/pipelines/{api_id}/interval_results')

    results_response = requests.get(
        url,
        headers={
            'x-api-key': skywatch_key
        }
    ).json()

    print(results_response)

    # if there are no results created yet for this List object
    # create them
    if len(Result.objects.filter(pipeline_id=id)) == 0:

        for i in results_response['data']:

            # create new result object
            new_result = Result(
                pipeline_id=update_list,
                created_at=i['created_at'],
                updated_at=i['updated_at'],
                api_pipeline_id=i['pipeline_id'],
                status=i['status'],
                output_id=i['output_id'],
                message=i['message'],
                interval_start_date=i['interval']['start_date'],
                interval_end_date=i['interval']['end_date'],
            )

        # save the newly created result
        new_result.save()

        # if an image is found for each interval
        if len(i['results']) > 0:

            new_result.image_created_at = i['results'][0]['created_at'],
            new_result.image_updated_at = i['results'][0]['updated_at'],
            new_result.image_preview_url = i['results'][0]['preview_url'],
            new_result.image_visual_url = i['results'][0]['visual_url'],
            new_result.image_analytics_url = i['results'][0]['analytics_url'],
            new_result.image_metadata_url = i['results'][0]['metadata_url'],
            new_result.image_size = i['results'][0]['metadata']['size_in_mb'],
            new_result.image_valid_pixels_per = i['results'][0]['metadata']
            ['valid_pixels_percentage'],
            new_result.image_source = i['results'][0]['metadata']['source'],
            new_result.scene_height = i['overall_metadata']['scene_height'],
            new_result.scene_width = i['overall_metadata']['scene_width'],
            new_result.filled_area = i['overall_metadata']['filled_area_km'],
            new_result.aoi_area_per = i['overall_metadata']
            ['filled_area_percentage_of_aoi'],
            new_result.cloud_cover_per = i['overall_metadata']
            ['cloud_cover_percentage'],
            new_result.aoi_cloud_cover_per = i['overall_metadata']
            ['cloud_cover_percentage_of_aoi'],
            new_result.visible_area = i['overall_metadata']
            ['visible_area_km2'],
            new_result.aoi_visible_area_per = i['overall_metadata']
            ['visible_area_percentage_of_aoi'],

        # save the newly created result
        new_result.save()

    # if there are already results created for this List object
    # update them
    else:

        for i in results_response['data']:

            # get the object to update
            # use unique pipeline id, and interval dates
            # to get the correct result object
            update_result = Result.objects.get(
                pipeline_id=id,
                interval_start_date=i['interval']['start_date'],
                interval_end_date=i['interval']['end_date'])

            update_result.updated_at = i['updated_at']
            update_result.status = i['status']
            update_result.message = i['message']
            
            # if there are now images
            # add images to result object
            if len(i['results']) > 0:

                update_result.image_created_at = i['results'][0]['capture_time']
                update_result.image_updated_at = i['results'][0]['updated_at']
                update_result.image_preview_url = i['results'][0]['preview']
                update_result.image_visual_url = i['results'][0]['visual_url'],
                update_result.image_analytics_url = i['results'][0]['analytics_url'],
                update_result.image_metadata_url = i['results'][0]['metadata_url'],
                update_result.image_size = i['results'][0]['metadata']['size_in_mb'],
                update_result.image_valid_pixels_per = i['results'][0]['metadata']
                ['valid_pixels_percentage'],
                update_result.image_source = i['results'][0]['metadata']['source'],
                update_result.scene_height = i['overall_metadata']['scene_height'],
                update_result.scene_width = i['overall_metadata']['scene_width'],
                update_result.filled_area = i['overall_metadata']['filled_area_km'],
                update_result.aoi_area_per = i['overall_metadata']
                ['filled_area_percentage_of_aoi'],
                update_result.cloud_cover_per = i['overall_metadata']
                ['cloud_cover_percentage'],
                update_result.aoi_cloud_cover_per = i['overall_metadata']
                ['cloud_cover_percentage_of_aoi'],
                update_result.visible_area = i['overall_metadata']
                ['visible_area_km2'],
                update_result.aoi_visible_area_per = i['overall_metadata']
                ['visible_area_percentage_of_aoi']

            # save the updated result
            update_result.save()

    return redirect(reverse('detail_view', args=[id]))


