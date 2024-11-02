# Ideas

Main Dashboard: A project overview with thumbnails or names of recent projects, estimated material usage, and quick links to recent logs or error notes.
Project Detail View: Each project’s page showing settings, estimated and actual material usage, print duration, and any logged errors or troubleshooting notes.
Add/Edit Project Form: A form to input new project data or update existing projects with file uploads, print parameters, and material estimates.


Context Diagram:

  The 3D Print Manager app runs locally and is accessible via a web browser. The user interacts with a front-end interface to add, view, and edit projects. The app communicates with a local database where project files, logs, and notes are stored.

Container Diagram:

  Containers include a web server (e.g., Node.js or Django), a front-end (React or Vue.js), and a database (SQLite or PostgreSQL) for storing project details and logs.

Component Diagram:

  Main components include:
        Project Management: For adding/editing projects, uploading files, and tracking settings.
        Material and Duration Tracking: To log and calculate filament usage and time.
        Error Logging: To track and troubleshoot issues encountered during prints.
