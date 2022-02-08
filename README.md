# Spaceport
Spaceport is a full stack website which allows users to access satellite imagery of the Earth.  The website was developed for Milestone 4 as part of the Code Institute Diploma in Software Developement. 

![Responsive website](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643885662/Spaceport/amiresponsive_mk6ufl.jpg)

# Table of contents
- [Spaceport](#spaceport)
- [Project Overview](#project-overview)
- [Access](#access)
- [Definitions](#definitions)
- [UX](#ux)
    * [Strategy](#strategy)
        + [Site user](#site-user)
        + [Admin](#admin)
    * [Structure](#structure)
        + [Pages](#pages)
        + [Database](#database)
    * [Style](#style)
    * [Scope](#scope)
- [Features]
    * Homepage
    * Discover
    * My Pipelines
    * Create Pipeline
    * Detail view
    * Edit
    * Delete
    * Account authentication
- [Technologies used]
- [Testing]
- [APIs]
    * Skywatch
    * Mapbox
- [Deployment]
- [Media]
- [Credits]
- [Acknowledgements]

# Project Overview
- This website was developed for submission as the Milestone 4 project of the Code Institute Diploma in Software Developement.
- The website is deployed using the Heroku pages at the following url:
- The repository on Github that contains the website source code and assets is available at the following url:
- The website was built with a responsive look and feel, designed to be enjoyable to use on all screen sizes.

## Technical Abstract
This project has been designed to provide users with a platform to access satellite imagery through the Skywatch ‘Application Programming Interface’ (or ‘API’). The project idea was initially proposed by a company called Astrosat (Scotland) who specialise in data visualisation of satellite images to enhance our understanding of the challenges we face on Earth.

Satellite imagery is becoming increasingly popular as a way of providing a different perspective on changing environments on the Earth's surface. For example, images taken by satellites can provide a more expansive view of rainforest deforestation in the Amazon, enabling more straightforward and accurate calculations of the proportion the total area that is felled, as well as the rate of destruction. Environmental organisations can thus utilise this technology to draw attention to decline in critical climactic environments.

Satellite imagery is also becoming more accessible to the global citizenry, whose uses for it range from specific projects to simple curiosity. In recognition that there are many who are interested in, but hitherto unfamiliar with, satellite technology, the website attempts to provide a comprehensive and accessible guide through the process.

The Skywatch ‘Application Programming Interface’ (or ‘API’) requires users to submit details of the satellite images they wish to access, defining within specific parameters. The API will then cross-reference these with the satellites available on its database, with the goal of straightforwardly delivering the desired images to the user.

While Astrosat regularly use the Skywatch EarthCache console to retrieve images, the company has less experience in interacting with the API itself.  This project attempts to provide insight into the intricacies of the API and to provide a user-friendly, front-end platform to demonstrate its capabilities.  

# Access
The assesor can create their own account to test the functionality of the website, and/or can use the details below to sign in and view some example pipelines which have been created for convenience.

- Username: ms4_test
- Password: spaceport_test_password

# Definitions
This website is based on a technical concept of accessessing satellite imagery, therefore see below some useful definitions which may be used in this document. These definitions and more can also be found on the Discover website page.
- Pipeline: a pipeline refers to the timeline, or projected plan or schedule, of receiving satellite images. Each object in the 'List' model represents a pipeline.  Pipelines are active if they have not completed all intervals, and complete if all intervals have been completed
- Interval: the interval describes the time period in which to look for images.  An interval of 1 day will aim to deliver 1 image per day; an interval of bi-weekly will aim to deliver 1 image every 14 days.
- AOI:  the Area of Interest is the area/coverage/footprint on Earth the user wants to search for images of

# UX
## Strategy
### Site User
The primary goals of the website user are as follows:
- To create an account on the website, which will allow them to create pipelines
- To create, update, edit and delete pipelines 
- To view the details of a pipeline they have created
- To view the schedule of receiving images
- To see a list of all their pipelines, ordered by status
- To understand the applications and purposes of satellite imagery

### Admin User


## Structure
### Pages
The website has five main pages, with user authentication on three:
- Homepage (all): to introduce users to the website and detail the purpose
- Discover (all): to allow users to explore the uses of satellite imagery
- My Pipelines (user): to list all pipelines created by the user
- View of pipeline (user): to display all details of the pipeline instance
- Create pipeline (user): to display an interactive form for creating a pipeline

The additional pages are as follows:
- Edit pipeline
- Delete pipeline
- Confirmation of deleted pipeline
- Log in/log out/sign up pages

The website was designed to be simple, clear and non-cluttered, basic in structure, with attractive images of satellites and images captured by satellites.
Bootstrap was used to aid responsiveness, as well as media queries in CSS.

### Database

- Spaceport App
- templates
- static
- README
- manage.py
- Procfile
- Requirements.txt

#### Database Model

![Schema](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643821929/Spaceport/SCHEMA_j2yy7r.jpg)

#### Models
There are three models in this project.  As the project uses an API for a lot of the information stored in the databases, see the associated tables to understand how the data is created (whether by the User, the Spaceport app, or from the API)

##### User
- The User model contains information about the user, as part of the Django allauth library
- No additional features are added to this model, as a basic username and password satisfy the requirements of the project
- The model fields are: 

##### List
- The List model contains information about the pipeline the user set up
- The model fields are as below:

| Field | Description | Created from | Field type|
|-------|-------------|--------------|-----------|
|id|the primary key for this model, used to cross reference Result objects|Django|Primary Key|
|pipeline_name|the name the user gives to the pipeline|User|Charfield|
|pipeline_des|the description the user inputs to identify the pipeline|User|Charfield|
|start_date|what date the pipeline will start looking for images|User|Date|
|end_date|what date the pipeline will stop looking for images|User|Date|
|interval|the interval period set by the user|User|Charfield (choice of 5)|
|aoi|the coordinates for the Area of Interest chosen by the user|User|JSON|
|output_image|the type of images the pipeline should return|User|Charfield (choice of 6)|
|cloud_cover|the maximum allowable cloud cover in returned images|User|Charfield|
|num_intervals|the number of intervals between the start and end date|API|Charfield|
|date_created|the date the pipeline was created|Spaceport|Date|
|aoi_area|the area in km2 of the AOI|API|Charfield|
|created_by|the user the pipeline was created by|Spaceport|Charfield|
|status|whether the pipeline is active, complete, or pending|Spaceport|Charfield|
|api_id|the unique id given to the pipeline by the API|API|Charfield|
|num_results|the number of results associated with the pipeline (same as num_intervals)|Spaceport|Charfield|
|num_images|the number of images successfully received by the pipeline|Spaceport|Charfield|
|results_updated|when the pipeline was last refreshed from the API|API|Datetime|
|featured_image|a url to display an image on My Pipelines page|API|Charfield|
|time_edited|when the pipeline was last edited|Spaceport|Datetime|


##### Result
- The Result model contains information about results relating to the pipeline.  The number of results for a pipeline is directly linked to the number of intervals a pipeline has. Example: if a pipeline is 5 days in length, with an interval of 1 day, there will be 5 intervals (1 for each day), and thus 5 results.
- It contains the List as the foreign key.
- The model fields are as below: 

| Field | Description | Created from | Field type|
|-------|-------------|--------------|-----------|
|id|the primary key for the results model0|Django|Primary Key|
|pipeline_id|the id from the List model|Django|Foreign Key|
|created_at|the time & date the result was created|API|Datetime|
|updated_at|the time & date the result was updated from the API|Spaceport|Datetime|
|api_pipeline_id|the unique API id of the pipeline|API|Charfield|
|output_id|the id from the API given to reference each output type|API|Charfield|
|status|the status of the result|Spaceport|Charfield|
|message|the message from the API for the result|API|Charfield|
|interval_start_date|the start date for this result|Spaceport|Date|
|interval_end_date|the end date for this result|Spaceport|Date|
|image_created_at|the time & date the image was captured by a satellite|API|Datetime|
|image_updated_at|the time & date the image was last updated by the satellite|API|Datetime|
|image_preview_url|the url for the preview of the image|API|Charfield|
|image_visual_url|the url for the full size image|API|Charfield|
|image_analytics_url|the url for for analytical image|API|Charfield|
|image_metadata_url|the url for the metadata JSON associated with the image|API|Charfield|
|image_size|the size of the image in megabytes|API|Charfield|
|image_valid_pixels_per|the % of valid pixels in the image|API|Charfield|
|image_source|the satellite the image was captured by|API|Charfield|
|scene_height||API|Charfield|
|scene_width||API|Charfield|
|filled_area|area in km2 of the AOI which was able to be captured|API|Charfield|
|aoi_area_per|% of the AOI which was captured|API|Charfield|
|cloud_cover_per|cloud cover % of the image|API|Charfield|
|aoi_cloud_cover_per|cloud cover % of the AOI|API|Charfield|
|visible_area|visible area in the image|API|Charfield|
|aoi_visible_area_per|visible area as a % of the AOI|API|Charfield|

## Style
The styling is kept clean and minimal throughout the site.  As the content of the site may appear technically complex to new users, there are no distracting fonts, colours or images to confound the user. Attractive images are used where relevant to pique the interest of the user and indicate, alongside the text, the purpose of the website. 

### Font
The font style is the default Bootstrap 5 native sans-serif font stack for cross platform usability. The font remains consistent throughout the website, aside from being rendered in italic or font style for emphasis.

![Bootstrap Native Font](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643901837/Spaceport/font_xbuoff.jpg)

### Colours
- The colours of the website are kept to basic white, black and a light blue/grey background colour (rgb(177, 177, 177)).

![Main background colour](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643900779/Spaceport/177177177_tt8ngq.jpg)

- A similar blue/grey hue is used in table headings (#5c6885). 

![Table headings](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643900779/Spaceport/92104133_v295zu.jpg)
![Results table](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643902229/Spaceport/tableheadings_gulfv8.jpg)

- Form field validation is noticeable against these similar colours with a pink/orange hue to raise attention. 
![Form field invalid](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643900779/Spaceport/250209185_zrohcm.jpg) 
![Form field not filled in](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643902229/Spaceport/invalidform_wrirn0.jpg)

- The form progress panel uses an unremarkable turquoise (#04aa6d) to show the user's form progress.
![Progress indicator](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643900779/Spaceport/4170109_euap9y.jpg)
![Progress indicator](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643902228/Spaceport/progressindicator_ty89po.jpg)


- The high definition photos provide splashes of colour against a simple background.

![Image next to text](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643902011/Spaceport/images_yckrmm.jpg)

### Layout
- The informative pages, such as the Homepage and Discover page, remain consistent with attractive images alongside short sections of text.

- Bootstrap cards are used to display information in a clear and consise manner along with a complementary image. 

![Discover Card](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643900948/Spaceport/card2_ocaal8.jpg)

- For several pages, the content is rendered in a section of white background with a box-shadow in front of the normal light blue background.

![Form with box shadow](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643902342/Spaceport/boxshadow_owigi7.jpg)

- Most pages offer a sub navigation list to easily jump to the relevant section of the page.

![Sub navigation on Pipelines page](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643901899/Spaceport/nav1_nwz0ix.jpg)

## Scope

### Site User Stories

## User Story 1
As a **Site User** I can **create a pipeline**

- 1.1: As a **New/returning Site User** I can **see an introduction page to creating a pipeline** so that **I understand the restrictions**
- 1.2: As a **New/returning Site User** I can **see an advice on how to maximise my chance of my pipeline returning images** so that **I can choose my parameters accordingly**
- 1.3: As a **New Site User** I am **provided with a list of examples** so that **I have a starting point for my first pipeline**
- 1.4: As a **New/returning Site User** I am **made aware that submitting a pipeline does not guarantee results** so that **I am not disappointed if my pipeline does not receive images**
- 1.5: As a **New/returning Site User** I can **see a progress indicator on the form** so that **I know what my progress in the form is, and which sections I have completed**
- 1.6: As a **New/returning Site User** I can **see inline feedback on my form** so that **I know if the parameter I entered was incorrect**
- 1.7: As a **New/returning Site User** I can **see visual representations of relevant parameters** so that **I have a more accessible understanding of what I am selecting**
- 1.8: As a **New/returning Site User** I can **see descriptions/placeholders of parameters** so that **I know what this parameter means for my pipeline**
- 1.9: As a **New/returning Site User** I can **navigate forwards and backwards in the form** so that **I can change details before I submit**
- 1.10: As a **New/returning Site User** I can **review the details of the pipeline I have created** so that **I can review the details before I submit**
- 1.11: As a **New/returning Site User** I can **see which parameters can be changed after submission** so that **I am aware what can be edited**
- 1.12: As a **New/returning Site User** I have **feedback on submission** so that **I have confirmation that the pipeline was submitted**
- 1.13: As a **New/returning Site User** I am **redirected to the detail view of the pipeline after submission** so that **I can view the details of the pipeline I submitted**
- 1.14: As a **New/returning Site User** I am **encouraged to allow for the website to process the pipeline when first redirected** so that **I understand why the pipeline detail is initially sparse**

## User Story 2
As a **Site User** I can **view a list of all my pipelines**

- 2.1: As a **Returning Site User** I can **see the My Pipelines link on the navbar when I am logged in** so that **I can easily refer back to this at all times**
- 2.2: As a **Returning Site User** I can **see all my pipelines ordered by active status** so that **I am aware which pipelines are still active**
- 2.3: As a **Returning Site User** I can **see all my pipelines ordered by completed status** so that **I am aware which pipelines have completed all intervals**
- 2.4: As a **Returning Site User** I can **see all my pipelines ordered by pending status** so that **I am aware which pipelines I should update**
- 2.5: As a **Returning Site User** I can **see a status link section at the top of My Pipelines** so that **I can see how many pipelines are in each category, and navigate to each list separately**
- 2.6: As a **Returning Site User** I can see **a card displaying important information about each pipeline** so that **I can identify which pipeline it refers to**
- 2.7: As a **Returning Site User** I can see **a featured image on the pipeline card** so that **I know if that pipeline has found any images**
- 2.8: As a **Returning Site User** I can see **an interactive style change when I hover over a pipeline** so that **I know I can click on the pipeline card and view pipeline details**
- 2.9: As a **New Site User** I am **shown a message at the top of My Pipelines, directing me to create a pipeline** so that **when first signing up, I am linked to the next logical step**

## User Story 3
As a **Site User** I can **view all details of a specific pipeline**

- 3.1: As a **Returning Site User** I can **see that the detail view is separated into sections** so that **I can scroll to the section I am interested in**
- 3.2: As a **Returning Site User** I can **see all important and general information at the top of the detail view** so that **I can identify which pipeline it refers to**
- 3.3: As a **Returning Site User** I can **click an Update button** so that **I can refresh the details of the pipeline**
- 3.4: As a **Returning Site User** I can **see a zoomable map of the AOI in the detail view** so that **I can see the area on the Earth this pipeline refers to**
- 3.5: As a **Returning Site User** I can **see a timeline chart of my pipeline** so that **I can visualise the pipeline period, completed intervals, incomplete intervals, today's date and if/when images were found**
- 3.6: As a **Returning Site User** I can **see a table of all interval dates** so that **I can see the status of each interval**
- 3.7: As a **Returning Site User** I can **see a table of results** so that **I can easily see if images have been delivered**
- 3.8: As a **Returning Site User** I am **directed to a separate tab when I click on a found image** so that **I can view it in detail and download it**
- 3.9: As a **Returning Site User** I am **directed to a separate tab when I click on image metadata** so that **I can read it or use it in post production of the image**
- 3.10: As a **Returning Site User** I can **view the parameters I selected when creating the pipeline** so that **I am reminded of the parameters I set**
- 3.11: As a **Returning Site User** I can **see a timestamp on 'last edited'** so that **I know if/when I edited the pipeline**
- 3.12: As a **Returning Site User** I can **see buttons to edit/delete my pipeline** so that **I know how to access these functions**
- 3.13: As a **Returning Site User** I am **told if I cannot edit/delete my pipeline** so that **I am aware why these functions are/are not available**

## User Story 4
As a **Site User** I can **create an account** so that **I can log in to create pipelines, and view my pipelines**

- 4.1: As a **New Site User** I can **sign up to Spaceport** so that **I can create pipelines**
- 4.2: As a **Returning Site User** I can **log in to my account when revisiting the page** so that **I view details of my pipelines**
- 4.3: As a **Site User** I can **see the login/signup/logout link in the nav bar** so that **I am always aware of my log in state**
- 4.4: As a **Site User** I am **redirected to my pipelines when I log in** so that **my account information is immediately visible to me**
- 4.5: As a **Site User** I can **logout from my account on Spaceport** so that **my account information is kept safe and private**

User story 5: As a **Site User** I can **view all details of a specific pipeline**
- 5.1: As a **Returning Site User** I can **see that the detail view is separated into sections** so that **I can scroll to the section I am interested in**
- 5.2: As a **Returning Site User** I can **see all important and general information at the top of the detail view** so that **I can identify which pipeline it refers to**
- 5.3: As a **Returning Site User** I can **click an Update button** so that **I can refresh the details of the pipeline**
- 5.4: As a **Returning Site User** I can **see a zoomable map of the AOI in the detail view** so that **I can see the area on the Earth this pipeline refers to**
- 5.5: As a **Returning Site User** I can **see a timeline chart of my pipeline** so that **I can visualise the pipeline period, completed intervals, incomplete intervals, today's date and if/when images were found**
- 5.6: As a **Returning Site User** I can **see a table of all interval dates** so that **I can see the status of each interval**
- 5.7: As a **Returning Site User** I can **see a table of results** so that **I can easily see if images have been delivered**
- 5.8: As a **Returning Site User** I am **directed to a separate tab when I click on a found image** so that **I can view it in detail and download it**
- 5.9: As a **Returning Site User** I am **directed to a separate tab when I click on image metadata** so that **I can read it or use it in post production of the image**
- 5.10: As a **Returning Site User** I can **view the parameters I selected when creating the pipeline** so that **I am reminded of the parameters I set**
- 5.11: As a **Returning Site User** I can **see a timestamp on 'last edited** so that **I know if/when I edited the pipeline**
- 5.12: As a **Returning Site User** I can **see buttons to edit/delete my pipeline** so that **I know how to access these functions**
- 5.13: As a **Returning Site User** I am **told if I cannot edit/delete my pipeline** so that **I am aware why these functions are/are not available**

User story 6: As a **Site User** I can **create a pipeline**
- 6.1: As a **New/returning Site User** I can **see an introduction page to creating a pipeline** so that **I understand the restrictions**
- 6.2: As a **New/returning Site User** I can **see an advice on how to maximise my chance of my pipeline returning images** so that **I can choose my parameters accordingly**
- 6.3: As a **New Site User** I am **provided with a list of examples** so that **I have a starting point for my first pipeline**
- 6.2: As a **New/returning Site User** I am **made aware that submitting a pipeline does not guarantee results** so that **I am not disappointed if my pipeline does not receive images**
- 6.2: As a **New/returning Site User** I can **see a progress indicator on the form** so that **I know what my progress in the form is, and which sections I have completed**
- 6.3: As a **New/returning Site User** I can **see inline feedback on my form** so that **I know if the parameter I entered was incorrect**
- 6.4: As a **New/returning Site User** I can **see visual representations of relevant parameters** so that **I have a more accessible understanding of what I am selecting**
- 6.5: As a **New/returning Site User** I can **see descriptions/placeholders of parameters** so that **I know what this parameter means for my pipeline**
- 6.6: As a **New/returning Site User** I can **navigate forwards and backwards in the form** so that **I can change details before I submit**
- 6.7: As a **New/returning Site User** I can **review the details of the pipeline I have created** so that **I can review the details before I submit**
- 6.8: As a **New/returning Site User** I can **see which parameters can be changed after submission** so that **I am aware what can be edited**
- 6.9: As a **New/returning Site User** I have **feedback on submission** so that **I have confirmation that the pipeline was submitted**
- 6.10: As a **New/returning Site User** I am **redirected to the detail view of the pipeline after submission** so that **I can view the details of the pipeline I submitted**
- 6.11: As a **New/returning Site User** I am **encouraged to allow for the website to process the pipeline when first redirected** so that **I understand why the pipeline detail is initially sparse**

User story 7: As a **Site User** I can **edit, update and delete pipelines**
- 7.1: As a **New/returning Site User** I can **access the edit form on the pipeline detail page** so that **I edit the pipeline**
- 7.2: As a **New/returning Site User** I can **see which parameters I can change for my pipeline** so that **I am aware of the limitations once my pipeline has been submitted**
- 7.3: As a **New/returning Site User** I can **change the name and description of my pipeline** so that **I can correct if needed, or add details about results in the description**
- 7.4: As a **New/returning Site User** I can **update/refresh the pipeline** so that **I can see if any new images have been delivered/update interval statuses**
- 7.5: As a **New/returning Site User** I know **that I have to update the pipeline myself** so that **I am not confused why the status/interval/results have not changed**

User Story 12: As a **Site User** I can **edit details of my pipelines**
- 12.1: As a **New/returning Site User** I can **access the edit form on the pipeline detail page** so that **I edit the pipeline**
- 12.2: As a **New/returning Site User** I can **see which parameters I can change for my pipeline** so that **I am aware of the limitations once my pipeline has been submitted**
- 12.3: As a **New/returning Site User** I can **change the name and description of my pipeline** so that **I can correct if needed, or add details about results in the description**
- 12.4: As a **New/returning Site User** I can **see if my pipeline is able to be edited** so that **I am aware if I can edit the pipeline and, if not, the reason why**
- 12.5: As a **New/returning Site User** I am **redirected back to the detail view of the pipeline** so that **I can see the changes I made reflected**
- 12.6: As a **New/returning Site User** I am **shown a timestamp of when the pipeline was last edited** so that **I am aware if and when I last edited my pipeline**

### Admin


# Features

## Homepage
The Spaceport homepage presents the purpose of the website to the user in a clear and concise manner, with attractive images and minimalist design.

### Navbar
The navigation bar at the top of the webpage is featured on all pages, and remains fixed at the top in order for the user to be able to navigate to other pages easily, demonstrate the page the user is on, and provide a general overview of the website content.  The content of the navigation bar changes depending on the user's log in state in order to reflect the relevant pages.

To the left is the website title and featured icon.  The user can use either of these to navigate back to the homepage.
Offset from the left is a collection of other pages - Discover, Create and Pipelines - the latter two of which are only available for signed up and logged in users.
Fixed to the right is the link to login/signup/logout, for the user to change their login state.  If the user is logged in their username is also displayed here, clearly showing they are logged in. 

The navigation bar links are underlined to show the active page and also display this style on mouse hover.  The navigation bar responds to smaller screens by removing all links aside from the homepage link and icon, placing these in a drop down bar.

![Spaceport logo](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643905019/Spaceport/spaceport_lps0pr.jpg)

Title and icon for website

#### Desktop
|![Nav logged out](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643904778/Spaceport/nav_4_lj2eie.jpg)|
|:--:|
|Navigation bar when not logged in|

|![Nav logged in](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643904778/Spaceport/nav_qtdp1g.jpg)|
|:--:|
|Navigation bar when logged in|

#### Mobile & tablets
|![Nav collapsed](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643904778/Spaceport/nav_2_vl8gcb.jpg)|
|:--:|
|Navigation bar collapsed|

|![Nav expanded](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643904778/Spaceport/nav_3_jpnzxi.jpg)|
|:--:|
|Navigation bar expanded|

### Banner image
The homepage image is chosen specifically because of the attractive colours and content.  It displays an imaging satellite and in the background is a high resolution render of Earth taken from space, both of which are of most relevance to the purpose of the website.  Alongside this image is a concise website description - "Access satellite imagery in minutes" - to further reinforce the purpose of the website, and demonstrate the simplicity of the process of creating a pipeline.

|![Website banner](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643902011/Spaceport/images_yckrmm.jpg)|
|:--:|
|Website banner image|

### Introduction to website
The rest of the homepage attempts to capture the concept of the website in a concise and understandable way, by explaining in four simple steps what their experience using the website will be - simply put, to choose an area on Earth, allow the platform to set up their pipeline and await results, continually track the progress, and ultimately view and use the collected images.

|![Website introduction](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643905166/Spaceport/introtowebsite_ae4xtz.jpg)|
|:--:|
|One of the four steps|

### Calls to action
After reading the website introduction, the user is directed to either the Discover page or (if logged in) to create a pipeline, or (if not logged in) create an account.  This section is designed to encourage the user to either learn more about satellite imagery and pipelines, namely for new users, or if they are returning they can move directly to creating a pipeline. 

|![Homepage CTAs](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643905214/Spaceport/ctas-homepage_hybuby.jpg)|
|:--:|
|Homepage calls to action|

## Discover
The Discover page is named aptly to encourage users to explore more about satellite imagery before jumping in to creating their own pipelines.  The purpose of the page is to provide more technical information and context about the site's purpose.  This information is kept separate from the homepage as it holds a lot of information, and the user is directed to this page at several places on other pages, as the developer feels it is beneficiery to explore this page before using the site.  In short, as the website is based on a very specific, technical concept, the developer wants the user to have a comprehensive understanding of the purpose of the site. 

|![Discover banner](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643905293/Spaceport/discover_fzkqjq.jpg)|
|:--:|
|Discover banner|

### Discover links
As the Discover page is long, a sub navigation section is rendered to display the information the user can expect to find on this page, and to allow the user to jump to the page section of most interest.

### Applications
The applications section of the Discover page convey to the user the industry uses of satellite imagery.  This section is intended to provide the user with more context to the site's purpose.  The section details three common uses of satellite imagery, with a relevant image and short description attached to each use. 

### Examples
The examples section is an extension of the applications section, explaining in more detail an example of how and why satellite imagery is collected.  These 'real-life' examples provide context to the user about why they might want to use the site.

### News
The news section further reinforces the importance of access to satellite imagery, providing a couple of topical examples which the user may have recently come across to provoke the user's interest.

### Glossary
The glossary section defines any technical or unfamiliar terms the user may come across on the site.

### FAQ
The frequently asked questions section provides access to some questions the user may ask when using the site, and attempts to provide a clear answer.

## Pipelines
The Pipelines/My Pipelines page lists all the pipelines the user has created.  This page can be used to review the status of current pipelines, and click on each to see the detailed view.

### Pipelines links
There is sub navigation section which categorises the pipelines by their status.  There is also a brief description beneath each link to convey what each status means in the context of satellite imagery pipelines.

### Pipelines cards
Each pipeline is represented by a Bootstrap card, identified by the name of the pipeline.  The description, start and end dates, number of images collected, and a link to view the pipeline detail are also displayed.  The latest image the pipeline has collected is displayed in the card, or a placeholder image if there are none. 

## Detail
The detail view of the pipeline displays all information about the pipeline object.  The user can view not only the parameters they set, but information the platform gathers about intervals, and any results created.  The information is ordered specifically to render the identifying information first, then the information of most interest to the user (intervals/results), then the information the user already knows (the parameters selected by the user).

### Calls to action
There are two calls to action at the top of the page.  One to navigate back to the user's list of all pipelines.  The second calls the 'Update' function, which is placed at the top of the page in the immediate view of the user as it is an important function.  User's must update their pipelines manually, reasons for which are outlined in the 'Limitations' section of this document.  The time of the last update is rendered beneath this button.

### General
The general section conveys the most important, identifying and summarising information about the pipeline - the name, status, AOI, date created and number of images collected.  The AOI is displayed in a map, which automatically locates to the area and renders the user's drawn area.

### Interval
The interval section provides a table of all intervals in the pipeline, colour coded to represent the status of that interval (current, complete, future) and if they successful in collecting an image.  The overall start and end dates of the pipeline are also rendered, as well as the interval period (1d/daily, 7d/weekly etc) and number of intervals.

If the pipeline is active, a timeline graph is shown to provide a visual representation of the interval table data.  This timeline is not displayed under a screen width of 1200px.  As this information is duplicated in the interval table, albeit in a less visually appealing way, the omitting of the timeline below certain screen sizes should not hamper the user's experience on the site and understanding of the progress of their pipeline. 

### Results
The pipeline results are also displayed in a table.  The user can see:

- the status of the interval
- dates of the interval the result relates to
- an selectable image which opens a separate tab showing a preview of the image
- the time the image was captured by the satellite
- the satellite the image was captured by
- a link to the metadata which opens a separate tab displaying technical data of the image in JSON format 

The user can expand the table by clicking the drop down, which will open all rows to display further technical data about the image, as well as a link which downloads the full size image.

### Parameters
The parameters the user selected are displayed towards the bottom of the detail page for the user to review.

### Edit/Delete

## Create a Pipeline
The 'Create a Pipeline' form is an interactive form divided into multiple tabs, so the user can progress and regress as they need.  Each tab represents different categories in the form, as well as a definition of the parameters being asked, restrictions, and visual aids if required.  The form concludes with a review section, for the user to review all the parameters they set.

### Intro Page
THe introduction page on the form describes the purpose of the form, as well as prompting the user to visit the 'Discover' page if they are new.  A short sub navigation is provided on this page for convenience to scroll through the sections.

#### How it works
The users are provided with a short and punchy three step process of creating a pipeline.

#### Restrictions
The restrictions in terms of setting up their pipeline are displayed here, so the user knows to expect these in the form.  These are repeated on the relevant form section. 

#### Satellite Aquisition
The user is provided with some advice on how to maximise their chance of receiving an image, as well as ensuring the user understands that not all pipelines deliver results, depending on if a suitable satellite was found for their pipeline. 

#### AOI Selection
A map is used to select the AOI, so a basic set of instructions of drawing an area are provided to the user with pictures.

#### Getting Started
Users are provided with some suggestions of what kind of pipeline to create.  This is to give new users especially a starting point for creating a pipeline.

### General Page
The general section requires the user to input a name for their pipeline and they can also provide a short description to further identify it if required.

![General form page](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643884237/Spaceport/general_go11c0.jpg)

### AOI Page
The AOI section requires the users to use the interactive map to select points to form a polygon.  The definition and restrictions of AOI are provided.  The user is given feedback on the size of AOI they chose.

![AOI form page](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643884237/Spaceport/aoi_huwk3g.jpg)

### Interval Page
The interval section asks the users to select their pipeline start and end date, and the interval in which to capture images.  The restrictions of the interval, and validation errors are also on this page.

![Interval form page](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643884434/Spaceport/interval_yxaofq.jpg)

### Parameters Page
Users can adjust the cloud cover settings if they wish.  Visual representations of low, medium and high cloud cover are provided for reference.  If the form field is left at the default value of 1%, they are allowing images to be delivered with any percentage of cloud cover.

![Cloud cover form page](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643884518/Spaceport/cloudcover_izmve7.jpg)

### Output Page
Users can select from six output image types, set to a default of True Colour type.  Users can hover over the image to see a description of what the image type is. 

![Output form page](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643884848/Spaceport/output_zhmmfz.jpg)

### Review Page
Users can review all the parameters they set. They have the option to submit the pipeline, or go back and adjust parameters.  They are encouraged to review all the details before they submit. 

![Review form page](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643884982/Spaceport/review_dynivc.jpg)

### Submitting Page
The last form page presents a loading screen to the user, to let the user know the pipeline has been submitted and is being set up.  There are no calls to action on this page.

![Submitting form page](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643885204/Spaceport/submitting_dajpkl.jpg)

# Languages

## HTML/CSS
## Javascript
Javascript is included on most pages.  The main functions are:

### Display a 'Back to Top' button
On pages which have a lot of content, the user is provided with a button to allow them to scroll back to the top of the page for convenience.  This is [external library code](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp).

### Highlight the website active page
The three selectable pages in the navigation bar display different styling when the page is active.

### Create a map to draw the AOI
*function createMap()*

In the Create a Pipeline form, JS code renders a Mapbox map of the world and allows users to select points to form a polygon for choosing their AOI.

The code is derived from the 'draw' function in [Mapbox](https://docs.mapbox.com/mapbox-gl-js/example/mapbox-gl-draw/).

### Render the map to review the AOI
*function reviewMap() & function detailMap()*

Reviewing the map requires a reverse function of the above, collecting the user's selected AOI in geoJSON format and drawing this on the map.

The code is derived from the 'addSource' function in [Mapbox](https://docs.mapbox.com/mapbox-gl-js/api/map/#map#addsource).

### Create a progressive form to create a pipeline
For improved UX, the Create a Pipeline form is seperated into relevant tabs to allow the user to move forwards and back as desired.  The form provides additional form field validation.

The code is derived from [W3S](https://www.w3schools.com/howto/howto_js_form_steps.asp), adapted and enhanced to fit the requirements of the project.

### Perform form field validation
*function validateCloudCover(), function validateDate()*

Additional validation methods are required for the form, aside from the above and Django Forms validation. The user is provided with inline feedback for their parameters, so they are aware if and why they are valid/invalid.  The two main uses of this are to validate the interval dates and the AOI size.

### Create form review
*function createReview()*

This function renders the pipeline parameters as a final step for the user to review before submitting.  

### Create a chart to shown a timeline of the pipeline
*function timelineChart()*

This function creates a ChartJS graph, displaying relevant pipeline dates in a more visually appealing manner.

The code is derived from a simple example from the ChartJS [documentation](https://www.chartjs.org/docs/latest/charts/line.html).


## Python
## Django

# Limitations

## API Limitations

- The developer has a limited account with the Skywatch API.  During development, many pipelines were created for testing purposes under the accounts 'admin' and 'testing_account' and 'testing_account2'.  As the account is limited to 100 pipelines, all of these pipelines were deleted from the API before deployment.  The objects remain in the website database, but cannot be edited, updated or deleted as there is no longer a model in the API which represents these objects.

# Additional Features
This section details some additional features which could be added to further develop the website.

## UX
- Map zoom
Additional code could be added to the map renders, to create a short zoom animation towards their AOI

- 

## User Features

### Default pipelines
Several 'public' pipelines could be added which all users would have access to when they initially create an account  with Spaceport.  The developer feels it would be beneficial to see some 'live' examples of one active, complete, and pending pipeline, as well as an successful and unsuccessful pipeline.  

This would allow them to peruse these pipelines in order to understand the concept better, before they create their own.  

In reality this may be tricky to manage in terms of what access they have in terms of editing, updating and deleting, moreover there would be complexities with the API model being accessible by more than one person.  

### Save incomplete pipeline
A feature could be added within the code to allow users to save an incomplete pipeline form and return to it at a later date.  The developer feels this would be a useful feature, as the Create a Pipeline form is lengthy, and the user may want to refer back to the Discover page (Glossary, FAQs) during the completion of the form.

### Edit pipeline
The Edit form for changing parameters of the pipeline can be extended. 

The API does allow to 'patch' the AOI, ie add or remove from the AOI.  This is a complex function, and was not explored during the development of the project. 

The pipeline status can also be changed to allow the user to 'deactivate' the pipeline, ie when it is 'active', set it to 'inactive'.  This is an insignificant function for the project, as it is only practical for purchased imagery.

### Pipelines update automatically
The code could be improved by updating pipelines automatically, either via a timed request every few hours to update all pipelines in the database, or updating automatically when the pipeline detail view is selected.  In order to limit the number of API calls and maintain a responsive website, users can update individual pipelines manually.  Furthermore, the details of pipelines do not change dramatically on an hour to hour basis, therefore while an automatic update may be more convenient, it is not a necessity.

Similarly, when the user has created a new pipeline, there is a short period while the API gathers the information before the pipeline can be created.  In order to avoid the user being 'stuck' on a loading screen for five minutes, user experience is greater when they are directed straight to the detail view and instructed to wait a few minutes then update themselves.

### Upload AOI in different format
In order to provide an accessible, user friendly selection of the AOI, a map feature is rendered to allow the user to select their AOI in a polygon shape.  There are instances whereby this is not the most effective selection technique. The user may wish to select a very specific area which is based on geographical features which are not rendered in detail on a map. 

For example: if the user would like to pick an AOI based on a very specific section of forest area, the forestry commision or land owner can provide a digital file containing the coordinates of the area, as opposed to what may be a very fiddly process of selecting this area on the map.  In this instance, a preferred method may be to upload a .KML or .geoJSON file. 

The form could be improved by giving the user the choice to either select from the map, or upload a file.  The AOI file would have to be read, verified and validated in terms of AOI size and the JSON format before proceeding (this could be done with a separate API, DjangoJSON, or via Skywatch itself.)  

### Additional model to include API key
The API key used to create all pipelines references the developer's own account with Skywatch.  The Sign Up form could include a field to allow users to input their own API key.  This feature would be more practical for users who are already in the satellite imagery industry, and own an account with Skywatch.  For the purposes of this project, this feature did not seem necessary.

## API
The Skywatch API is very in-depth and there are many additional technical parameters which could be added to explore it further (dependent on the scope of the developer's account with Skywatch). See the [Skywatch API documentation](https://api-docs.skywatch.co/) for more information. 

### Latency
Latency describes the acceptable number of days between interval end date and delivery of the image.   The latency is currently set to the full interval period to increase the probability of image delivery. As an example: if the user chooses an interval of 1 week, and one of the interval start and end dates are 1st Jan 22 and 7th Jan 22 respectively,  images can be delivered in the week after that interval i.e. 8th Jan 22 to 15th Jan.  The images are still captured within the specified interval; the latency refers to the acceptable delivery dates. 

Users may desire to change this, and only accept images if they can be delivered within the interval itself, but they would have to have specific reasons to do so, and this did not seem relevant for the purposes of the project.

The technical understanding behind why there is this latent period of delivery is determined by how frequently satellites communicate with ground stations.  A satellite may capture an image of the AOI within the interval, but does not pass over a ground station for a few days afterwards.

A simplistic representation of this is shown [here](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1644147808/latency2_rbelk3.png).

### Resolution
The resolution for all images is set to 'low' (8 - 15 metres).  The Skywatch account of the developer is limited to this resolution so as to only allow delivery of free images.  A feature could be added to allow users to refine this (for example, to between 8 and 9 metres), but this did not seem advantageous or relevant for the website, and would further reduce the probability of receiving an image.

### AOI Coverage
For Spaceport users, the AOI coverage is set to a minimum of 50%, therefore only images which have covered at least 50% of the AOI selected will be delivered.  An additional tab on the Create a Pipeline form could allow for the user to control this parameter and accept images with lesser coverage, or only accept images with higher coverage.

### Alternative Images
Taking into account the AOI Coverage parameter as above, a feature could allow users to view alternative images with an AOI coverage of below their selected percentage.  For example, if the AOI coverage is set to 50%, there may be 10 images found which captured less than 50% of the AOI.  This feature would allow users to still view these images as they may still be of use.

### Mosaicking
Mosaicking is a term which essentially means 'stitching' together images taken at different times or from different satellites.  If this feature was allowed, this would increase the probability of an interval delivering an image.  This parameter is not permitted to be changed under the developer's account.

[Moasicking image from Skywatch EarthCache](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1644146972/mosacking_gvily9.jpg)

### Calculate Probability

# Unfixed Bugs

## Dates on pipeline timeline
The developer feels the timeline of the interval dates in the pipeline detail view would be improved only showing dates on the x axis where there is a data point, ie an interval start or end date, or image captured date.  This would appear cleaner and clearer to the user.  The 'autoskip' function of the ChartJS timeline should perform this function - to only render data points on the axis - but could not be displayed the way the developer desired.  After some tutor support, this bug was left unfixed since although the timeline was a bit clunky, it did not show incorrect information.