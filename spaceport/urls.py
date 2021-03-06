# Import 3rd party

# Import django
from django.urls import path
from django.conf.urls import url

# Import local
from . import views

urlpatterns = [
    path('',
         views.homepage,
         name='homepage'),
    path('discover.html',
         views.discover,
         name='discover'),
    path('delete_conf/<int:id>',
         views.delete_feedback,
         name='delete_feedback'),
    path('create_pipeline.html',
         views.create,
         name='create'),
    path('my_pipelines.html',
         views.my_pipelines,
         name='my_pipelines'),
    path('edit_pipeline/<int:id>',
         views.edit,
         name='edit_pipeline'),
    path('detail_view/<int:id>',
         views.detail_view,
         name='detail_view'),
    path('update/<int:id>',
         views.update,
         name='update'),
    path('delete_view/<int:id>',
         views.delete_view,
         name='delete_view'),
    path('delete/<int:id>',
         views.delete,
         name='delete'),
]
