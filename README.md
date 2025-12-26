# Django To-Do List Application

A complete, feature-rich to-do list web application built with Django 5.x and Bootstrap 5.

## Features

### User Authentication

- **User Registration**: New users can create accounts with username, email, and password
- **Login/Logout**: Secure authentication system using Django's built-in auth
- **User-Specific Tasks**: Each user can only view and manage their own tasks

### Task Management (CRUD Operations)

- **Create Tasks**: Add new tasks with title, description, due date, and priority
- **View Tasks**: See all your tasks in a beautiful card-based layout
- **Update Tasks**: Edit existing tasks to modify any field
- **Delete Tasks**: Remove tasks with confirmation dialog
- **Task Details**: View comprehensive information about each task

### Advanced Features

- **Filter by Status**: View all tasks, only active tasks, or only completed tasks
- **Search Functionality**: Search tasks by title or description
- **Sort Options**: Sort tasks by priority, due date, or creation date
- **Priority Levels**: Three priority levels (Low, Medium, High) with color-coded badges
- **Completion Status**: Mark tasks as completed with visual indicators

### User Interface

- **Bootstrap 5**: Modern, responsive design that works on all devices
- **Responsive Layout**: Optimized for desktop, tablet, and mobile screens
- **Interactive Cards**: Hover effects and smooth animations
- **Color-Coded Priorities**: Visual distinction between priority levels
- **Icons**: Bootstrap Icons for better visual communication
- **Empty States**: Helpful messages when no tasks are found

## Technology Stack

- **Backend**: Django 5.2.9
- **Frontend**: Bootstrap 5.3.0
- **Forms**: django-crispy-forms with Bootstrap 5 template pack
- **Database**: SQLite (default, easily configurable for PostgreSQL/MySQL)
- **Icons**: Bootstrap Icons
- **Python**: 3.8+

## Installation

### Prerequisites

- Python 3.8 or higher
- uv (Ultra-fast Python package installer) - [Install uv](https://github.com/astral-sh/uv)

### Setup Instructions

1. **Clone or navigate to the project directory**

   ```bash
   cd "c:\Manojkumar\development\To-Do List App Using Django"
   ```

2. **Install uv (if not already installed)**

   ```bash
   # Windows (PowerShell)
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Create a virtual environment and install dependencies**

   ```bash
   # uv automatically creates a virtual environment and installs dependencies
   uv venv
   uv pip install -r requirements.txt
   ```

4. **Activate the virtual environment**

   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

5. **Run migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional, for admin access)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and go to: `http://localhost:8000`
   - Admin panel: `http://localhost:8000/admin`

## Usage Guide

### Getting Started

1. **Register an Account**

   - Click "Register" in the navigation bar
   - Fill in username, email, and password
   - You'll be automatically logged in after registration

2. **Create Your First Task**

   - Click "Add New Task" button
   - Fill in the task details:
     - **Title**: Brief description of the task
     - **Description**: Detailed information (optional)
     - **Due Date**: When the task should be completed (optional)
     - **Priority**: Choose Low, Medium, or High
     - **Completed**: Check if the task is already done
   - Click "Save Task"

3. **Manage Your Tasks**

   - **View**: Click "View" to see full task details
   - **Edit**: Click "Edit" to modify task information
   - **Delete**: Click "Delete" to remove a task (with confirmation)

4. **Filter and Search**
   - Use the search bar to find tasks by title or description
   - Click status buttons (All/Active/Completed) to filter tasks
   - Use the sort dropdown to organize tasks by priority, due date, or creation date

## Project Structure

```
To-Do List App Using Django/
├── todo_project/              # Main project directory
│   ├── settings.py           # Project settings
│   ├── urls.py               # Root URL configuration
│   ├── wsgi.py               # WSGI configuration
│   └── asgi.py               # ASGI configuration
├── tasks/                     # Main app
│   ├── migrations/           # Database migrations
│   ├── templates/            # HTML templates
│   │   ├── tasks/           # Task-related templates
│   │   └── registration/    # Auth templates
│   ├── models.py            # Task model
│   ├── views.py             # Class-based views
│   ├── urls.py              # App URL configuration
│   ├── forms.py             # Task and user forms
│   └── admin.py             # Admin configuration
├── static/                   # Static files
│   └── css/
│       └── style.css        # Custom styles
├── manage.py                # Django management script
├── requirements.txt         # Project dependencies
└── db.sqlite3              # SQLite database (created after migrations)
```

## Models

### Task Model

- `user`: ForeignKey to User (owner of the task)
- `title`: CharField (max 200 characters)
- `description`: TextField (optional)
- `due_date`: DateField (optional)
- `priority`: CharField with choices (low/medium/high)
- `completed`: BooleanField (default: False)
- `created_at`: DateTimeField (auto-generated)
- `updated_at`: DateTimeField (auto-updated)

## Views

All views are class-based for better code organization:

- **TaskListView**: Display, filter, search, and sort tasks
- **TaskDetailView**: Show detailed task information
- **TaskCreateView**: Create new tasks
- **TaskUpdateView**: Edit existing tasks
- **TaskDeleteView**: Delete tasks with confirmation
- **RegisterView**: User registration with auto-login

## Security Features

- **User Authentication**: Required for all task operations
- **User Authorization**: Users can only access their own tasks
- **CSRF Protection**: Built-in Django CSRF protection
- **Password Validation**: Strong password requirements
- **SQL Injection Protection**: Django ORM prevents SQL injection

## Customization

### Changing Database

Edit `todo_project/settings.py` to use PostgreSQL or MySQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Modifying Styles

Edit `static/css/style.css` to customize colors, fonts, and layouts.

### Adding Features

The modular structure makes it easy to add new features:

- Add fields to the Task model in `tasks/models.py`
- Create new views in `tasks/views.py`
- Add templates in `tasks/templates/`

## Admin Panel

Access the Django admin panel at `http://localhost:8000/admin` to:

- Manage users
- View and edit all tasks
- Use advanced filtering and searching
- Export data

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Opera

## Responsive Design

The application is fully responsive and works on:

- Desktop computers (1920px and above)
- Laptops (1024px - 1919px)
- Tablets (768px - 1023px)
- Mobile phones (below 768px)

## Future Enhancements

Potential features for future versions:

- Task categories/tags
- Task sharing and collaboration
- Email notifications for due dates
- Task attachments
- Recurring tasks
- Calendar view
- Export tasks to CSV/PDF
- Dark mode toggle
- Task statistics and analytics

## Troubleshooting

### Port Already in Use

If port 8000 is already in use, run the server on a different port:

```bash
python manage.py runserver 8080
```

### Static Files Not Loading

Run the collectstatic command:

```bash
python manage.py collectstatic
```

### Database Errors

Delete `db.sqlite3` and run migrations again:

```bash
python manage.py migrate
```

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, please check:

- Django documentation: https://docs.djangoproject.com/
- Bootstrap documentation: https://getbootstrap.com/docs/

## Credits

Built with:

- Django - The web framework for perfectionists with deadlines
- Bootstrap - The world's most popular front-end toolkit
- Bootstrap Icons - Official open source icon library

---

**Enjoy managing your tasks efficiently! 🚀**
