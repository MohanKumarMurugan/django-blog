# Django Blog Project

A simple blog application built with Django that allows users to view blog posts and their details.

## Features

- Blog post listing page
- Individual blog post detail pages
- Basic routing system
- Admin interface for content management

## Project Structure

```
django-blog/
├── myapp/                 # Main project directory
│   ├── blog/             # Blog application
│   │   ├── models.py     # Database models
│   │   ├── views.py      # View functions
│   │   ├── urls.py       # URL routing
│   │   └── admin.py      # Admin interface configuration
│   ├── myapp/            # Project settings
│   └── manage.py         # Django management script
└── requirements.txt      # Project dependencies
```

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd django-blog
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and go to `http://127.0.0.1:8000/` to see the blog.

## Development

The project is currently in development with the following features implemented:
- Basic URL routing for blog posts
- View functions for listing and detail pages
- Project structure set up for future feature additions

## Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a new branch
3. Making your changes
4. Submitting a pull request

## License

This project is open source and available under the MIT License. 