<h1 align="center">DJANGO CRM</h1>

<h2 align="center">STEPS</h2>

1. ✅ Create Github Repository **django-crm**. Clone it in the local machine.
2. ✅ Initialize the repo with **Poetry**.
    ```python
    .
    ├── LICENSE
    ├── README.md
    ├── poetry.lock # POETRY PACKAGING & DEPENDENCY MANAGEMENT
    ├── pyproject.toml # POETRY PACKAGING & DEPENDENCY MANAGEMENT
    ```
3. ✅ Create Django Project **config** with: `django-admin startproject config .`.
    ```python
    # django-crm/
    django-admin startproject config .

    .
    ├── LICENSE
    ├── README.md
    ├── config # DJANGO PROJECT
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── poetry.lock
    ├── pyproject.toml

    ```
4. ✅ Create Django App **crm** with: `python3 manage.py startapp crm`.
    ```python
    # django-crm/
    python3 manage.py startapp crm

    .
    ├── LICENSE
    ├── README.md
    ├── config
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── crm # DJANGO APP
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── manage.py
    ├── poetry.lock
    ├── pyproject.toml
    ```
5. ✅ Setup **Github Actions CI/CD**.

    ```python
    .
    ├── .github # GITHUB ACTIONS CI/CD
    │   └── workflows
    │       └── devops.yml
    ├── .gitignore
    ├── LICENSE
    ├── Makefile # GITHUB ACTIONS CI/CD
    ├── README.md
    ├── config
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── crm
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── manage.py
    ├── mydb.py
    ├── poetry.lock
    ├── pyproject.toml
    └── requirements.txt
    ```

6. ✅ Install Mysql Community Server and Workbench.
7. Connect DJANGO with MYSQL
    ```python
    .
    ├── .github
    │   └── workflows
    │       └── devops.yml
    ├── .gitignore
    ├── LICENSE
    ├── Makefile
    ├── README.md
    ├── config
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── crm
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── manage.py
    ├── mydb.py # MYSQL CONNECTION
    ├── poetry.lock
    ├── pyproject.toml
    └── requirements.txt
    ```