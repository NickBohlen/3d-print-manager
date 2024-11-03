# Mockup

![3d-printmanager](https://github.com/user-attachments/assets/edbde38c-1a8b-4c6e-b356-a78ae75a230a)

Context Diagram:

  The 3D Print Manager app runs locally and is accessible via a web browser. The user interacts with a front-end interface to add, view, and edit projects. The app communicates with a local database where project files, logs, and notes are stored.

Container Diagram:

  Containers include a web server (e.g., Node.js or Django), a front-end (React or Vue.js), and a database (SQLite or PostgreSQL) for storing project details and logs.

Component Diagram:

  Main components include:
        Project Management: For adding/editing projects, uploading files, and tracking settings.
        Material and Duration Tracking: To log and calculate filament usage and time.
        Error Logging: To track and troubleshoot issues encountered during prints.
