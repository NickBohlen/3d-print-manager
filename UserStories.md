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
