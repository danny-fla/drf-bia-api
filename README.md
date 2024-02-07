# Bia API
Bia API is the backend server used by the Bia frontend application (inset link)


## Table of Contents
* [Development Aims](#Development-Aims)
* [Agile Planning](#Agile-Planning)
    * [Epics](#Epics)
    * [User Stories](#User-Stories)
* [API End Points](#API-End-Points)
* [Future Features](#Features-Left-to-Implement)
* [Database Design](#Database-Design)
* [Security](#Security)
* [Technologies](#Technologies)
* [Testing](#Testing)
* [Deployment](#Deployment)
    * [Version Control](#Version-Control)
    * [Heroku Deployment](#Heroku-Deployment)
    * [GCP](#Google-Cloud-Platform)
    * [Run Locally](#Run-Locally)
    * [Fork Project](#Fork-Project)
* [Credits](#Credits)
  * [Content](#Content)
  * [Acknowledgements](#Acknowledgements)

# Development Aims

This APi aims to provide a backend service that will enable the frontend application Bia to perform create, read, update, delete (C.R.U.D.) operations through the user interface (UI).
<br>
<hr>

## Agile Planning

This project followed agile methodologies, delivering small features in incremental sprints. There were a total of three sprints, evenly spaced over three weeks.

All user stories were categorized into epics and prioritized with labels such as "Must have," "Should have," and "Could have." The stories were then assigned to specific sprints. The development prioritized "Must have" stories initially, followed by "Should haves," and finally, "Could haves." This sequential approach ensured the completion of essential requirements first, providing a comprehensive project foundation. Additional, desirable features were added based on available capacity.

The project utilized a Kanban board created on GitHub Projects, accessible here(link). For more detailed information on project cards, the Kanban board can be referenced. All stories, excluding documentation tasks, were equipped with a comprehensive set of acceptance criteria, serving as benchmarks to determine the completion status of each story.

(INSERT IMAGE OF KANPAN)

<br>

### Epics

#### Setup:

This Epic encompasses the initial configuration of the Django application and Django REST Framework, laying the groundwork for the commencement of feature development.

#### Recipe:

This Epic focuses on the creation of API endpoints and database connections essential for implementing CRUD functionality related to user recipes. This also encompasses activities such as liking recipes.

#### Comments:

This Epic addresses the creation of API endpoints and database connections necessary for the implementation of CRUD functionality for user comments, specifically in relation to recipes.

#### Profiles:

This Epic entails the creation of API endpoints and database connections required for the CRUD functionality associated with user profiles, including features such as following other users.

#### Chefs:

This Epic involves the creation of API endpoints and database connections essential for implementing CRUD functionality for users registering as Chefs.

#### Reviews:

This Epic covers the creation of API endpoints and database connections related to the CRUD functionality of recipe reviews, including the calculation of average ratings displayed on user profiles.

<br>
<hr>

## User Stories

### Epics

#### Setup

- As a developer, I need to establish the foundational project setup to facilitate further development.

#### User Authenication

- As a user, I want to register for a new account to gain access to all available features

#### Chefs

- As a developer, I aim to implement API views for chefs to ensure their data is accessible from the frontend.

#### Contact

- As a developer, I want to create a contact model and corresponding API view to enable users to reach out to the site owner with any issues or concerns.

#### Recipes

- As a user, I want the capability to view, edit, or delete recipes.
- As a user, I want the ability to create recipes and view a list of existing posts.

#### Profiles

- As a developer, I aim to automatically generate a new profile with a default image for each user upon registration.
- As a user, I want the ability to access a list of profiles registered on the platform.


## API Endpoints

User Story:

`As a developer, I need to establish the foundational project setup to facilitate further development.`

Implementation:

The foundational project was created along with a virtual environment including all neccessary packages which were then frozen into the requirements.

Secret variables were modified to hide any sensitive information and set dev and production environments apart.

User Story:

`As a user, I want to register for a new account to gain access to all available features`

Implementation:

Django Rest Framework and dj_rest_auth were installed and integrated into the project's URL patterns and site packages to leverage their built-in authentication system.

User Story:

`As a developer, I aim to implement API views for chefs to ensure their data is accessible from the frontend.`

Implementation:

Endpoint: /chefs/

Methods:

* POST - Used to create a chef
* GET - Used to retrieve a list of chefs

Endpoint: /chefs/int:pk/

Methods:

* GET - Used to view a single chef's profile
* PUT - Used to update a chefs's profile
* DELETE - Used to delete a chef's profile

User Story:

` As a developer, I want to create a contact model and corresponding API view to enable users to reach out to the site owner with any issues or concerns.`

Implementation:

Endpoint: /contacts/

Methods:

* POST - Used to create contact request
* GET - Used to get a list of contact requests

Endpoint: /contacts/int:pk/

Methods:

* GET - Get a single contact request
* PUT - Used to update a single contact request
* DELETE - Used to delete a contact request

User Story:

`As a user, I want the capability to view, edit, or delete recipes.`
`As a user, I want the ability to create recipes and view a list of existing posts.`

Implementation:

Endpoint: /recipes/

Methods:

* POST - Used to create recipe
* GET - Used to get a list of recipes

Endpoint: /recipes/int:pk/

Methods:

* GET - Get a single receipe
* PUT - Used to update a single recipe
* DELETE - Used to delete a recipe

User Story:

`As a developer, I aim to automatically generate a new profile with a default image for each user upon registration.`

A signal was implemented within the profiles app to automatically generate a new user profile upon registration.

User Story:

`As a user, I want the ability to access a list of profiles registered on the platform.`

Implentation:

Endpoint: /profiles/

Methods:

* POST - Used to create a profile
* GET - Used to get a list of profiles

Endpoint: /profiles/int:pk/

Methods:

* GET - Get a single profile
* PUT - Used to update a single profile
* DELETE - Used to delete a profile

<br>
<hr>

## Database Design

(insert database diagram)

## Security

A permissions class named IsOwnerOrReadOnly was implemented to restrict editing or deletion of content to its creator, ensuring that only users who create the content have the privilege to modify or remove it.

## Technologies

* Django
  * Framework used to create application
* Django REST Framework
  * Framework used for creating the API
* Cloudinary
  * Used to host static images
*  Heroku
  * Used to host the application
* Git
  * Used for verion control
* Github
  * Repository used for storing code and docs

<br>
<hr>

## Python Packages
