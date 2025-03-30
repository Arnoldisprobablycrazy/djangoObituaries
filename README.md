# Obituary Platform

The **Obituary Platform** is a Django-based web application that allows users to submit, view, and share obituaries. It provides a simple and user-friendly interface for managing obituary records.

## Features

- **Submit Obituaries**: Users can submit obituaries with details such as name, date of birth, date of death, content, and author.
- **View Obituaries**: A paginated list of obituaries is available for browsing.
- **Obituary Details**: Each obituary has a dedicated page with detailed information and sharing options.
- **SEO-Friendly**: Includes meta tags and Open Graph properties for better search engine optimization.
- **Sitemap**: Automatically generates a sitemap for search engines.

## Project Structure
obituary-platform/
├── obituary_project/          # Project configuration
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URLs
│   └── wsgi.py                # WSGI config
│
├── obituaries/                # Main app
│   ├── migrations/            # Database migrations
│   ├── templates/             # HTML templates
│   │   └── obituaries/
│   │       ├── base.html      # Base template
│   │       ├── form.html      # Obituary form
│   │       └── list.html      # Obituary listings
│   │
│   ├── admin.py               # Admin config
│   ├── apps.py                # App config
│   ├── forms.py               # Form definitions
│   ├── models.py              # Database models
│   ├── urls.py                # App URLs
│   └── views.py               # View functions
│
├── manage.py                  # Django CLI
└── requirements.txt           # Dependencies

##DATABASE
<img width="960" alt="image" src="https://github.com/user-attachments/assets/6e398873-cb81-49e0-8862-c574acb108c2" />
##SCREENS
<img width="960" alt="image" src="https://github.com/user-attachments/assets/ea8caf9f-398d-4b18-81f4-bd3d549156ae" />

VIEW OBITUARIES
<img width="960" alt="image" src="https://github.com/user-attachments/assets/9fc9b457-5cec-44c4-b10f-4c3d0f63caf6" />

OBITUARY DETAILS
<img width="960" alt="image" src="https://github.com/user-attachments/assets/89cb15e2-6606-43b8-a2fc-e57a610ca638" />





