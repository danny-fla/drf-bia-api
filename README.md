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