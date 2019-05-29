[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.2.1-brightgreen.svg)](https://djangoproject.com)

# Django Blog

## Django 2.2.1(LTS)

Run your app in a Virtual Environment: http://python-guide-ru.readthedocs.io/en/latest/dev/virtualenvs.html

Install the requirements:

```bash
pip install -r requirements.txt
```

Run the development server:

```bash
python manage.py runserver
```

Add search plugin for PostgreSQL:

```bash
sudo -u postgres psql blog

CREATE EXTENSION pg_trgm;

```

Site available at **127.0.0.1:8000/blog/**