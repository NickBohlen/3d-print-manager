# 3D Print Manager
The 3D Print Manager app helps you organize, track, and log each of your 3D printing projects from design to final print. Easily add projects, track estimated material usage and print duration, and log any errors, tweaks, or settings changes. Whether you’re troubleshooting a print, planning filament use, or simply trying to remember which settings worked best, this app centralizes all your printing details in one convenient place.

## Installation
```bash
git clone https://github.com/NickBohlen/3d-print-manager.git
cd 3d-print-manager

docker-compose up --build

docker-compose run backend python manage.py migrate
docker-compose run backend python manage.py createsuperuser
```

## Getting Started

After installing, you can run it with the following command:
```
docker-compose up
```
The App will be hosted locally currently and can be accessed via:

Frontend: http://localhost:3000

Backend API: http://localhost:8000


## User Stories

As a **3D printing enthusiast**, I want to **store my print files and settings** so I can reuse and **improve them over time**.
        Acceptance Criteria: Users can upload files and save specific print settings for each project.

As a **user**, I want to **track material usage for each project** so I can **manage filament inventory and avoid running out mid-print**.
        Acceptance Criteria: Users can input material estimates, and the app provides an alert when a project’s usage exceeds a set threshold.

As a **user**, I want to **log errors or issues I encountered during a print** so I can **avoid similar mistakes in the future**.
        Acceptance Criteria: Users can add detailed error logs and mark them as resolved once a fix is applied.

As a **user**, I want to **track the duration of each print job** so I can **better estimate print times for similar projects**.
        Acceptance Criteria: Users can log estimated and actual print times, with calculations for average duration over similar projects.

## Misuser Stories

As a **malicious user**, I want to **access and modify print logs** so I can **disrupt project tracking**.
        Mitigation Criteria: Implement user authentication to restrict access and provide role-based permissions for sensitive actions.

As a **malicious user**, I want to **delete print projects** to **disrupt data tracking and cause data loss**.
        Mitigation Criteria: Introduce a “soft delete” feature to retain projects in a recoverable state for a set period before permanent deletion.

As an **unauthorized user**, I want to **view project details** so I can **access sensitive information**.
        Mitigation Criteria: Ensure that project access requires secure authentication, and use encryption for sensitive data.

## Mockup

![3dprintmanager](https://github.com/user-attachments/assets/16afeec1-f6d7-46a1-b2ef-063976bd8f6f)

## Diagrams

### Context Diagram:

![ContextDiagram](https://github.com/user-attachments/assets/92d7f0cd-c1d7-4939-b60e-6a3a54cfe1f9)

### Container Diagram:

![ContainerDiagram](https://github.com/user-attachments/assets/620c9172-dbb5-41b1-add3-b7de0dbc322e)

### Component Diagram:

![ComponentDiagram](https://github.com/user-attachments/assets/2ef55d37-aea5-4812-b90b-08615a85a511)
