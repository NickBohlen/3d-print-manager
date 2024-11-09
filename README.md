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

## License

Copyright (c) Nicholas Bohlen 2024

