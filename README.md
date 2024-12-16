# 3D Print Manager
The 3D Print Manager app helps you organize, track, and log each of your 3D printing projects from design to final print. Easily add projects, track estimated material usage and print duration, and log any errors, tweaks, or settings changes. Whether you’re troubleshooting a print, planning filament use, or simply trying to remember which settings worked best, this app centralizes all your printing details in one convenient place.

The implementation prioritizes functionality, security, and usability. User authentication is enforced through session-based authentication, with robust user group definitions for administrators, application users, and anonymous users. Each group has distinct permissions, ensuring secure access control to sensitive operations. Custom validators and field sanitation techniques are employed to protect against vulnerabilities such as XSS and SQL injection. HTML is properly escaped, and JavaScript inputs are sanitized to maintain data integrity.

The project adheres to software development best practices, leveraging existing libraries and frameworks for database management and using Docker for containerized deployment. The design emphasizes modularity and reusability, with thorough documentation of code artifacts and processes. The user interface is intuitive and functional, reflecting attention to usability and aesthetic appeal.

Security hardening is a critical aspect of the project, with measures such as input validation, sanitized user inputs, and stringent permissions for various user roles. These features are designed to meet the expected security posture for the application, protecting user data and preventing unauthorized access.

## Installation
```bash
git clone https://github.com/NickBohlen/3d-print-manager.git

cd 3d-print-manager/print_manager
```
Install docker - [Download Docker Desktop](https://www.docker.com/products/docker-desktop/)

Start the Docker application on your device

Build the containers:
```bash
docker-compose build
```

## Getting Started

After installing, you can start the containers with the following command:
```bash
docker-compose up
```
The App will be hosted locally currently and can be accessed via:

http://127.0.0.1:8000/
or
http://localhost:8000/


When complete, you can stop the containers with the following command:
```bash
docker-compose down
```

This application has not been deployed to a cloud service provider.

## License

The MIT License (MIT)

Copyright (c) Nicholas Bohlen 2024

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

