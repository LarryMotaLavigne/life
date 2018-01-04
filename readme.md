# Life 

[![Build Status](https://travis-ci.org/Squalex/life.svg?branch=master)](https://travis-ci.org/Squalex/life)

This projet has for goal to provide a responsive website for life management.
It is made with Django 2.0 and severals tools I will describe later...

cf. [todolist](https://github.com/Squalex/life/blob/master/todo.md)

## Continuous Delivery
Travis CI, Heroku and Sentry


## Dependencies

<b>Django 2.0</b> : [link](https://docs.djangoproject.com/en/2.0/)
* Python Backend framework

<b>psycopg2 2.7</b> : [link](http://initd.org/psycopg/docs/)
* PostgreSQL connector for python

<b>gunicorn 19.7.1</b> : [link](http://gunicorn.org/)
* Python http server

<b>dj-database-url 0.4.2</b> : [link](https://github.com/kennethreitz/dj-database-url)
* Usefull for database configuration (handle MySQL, PostgreSQL, Oracle)

<b>whitenoise 3.3.1</b> : [link](http://whitenoise.evans.io/en/stable/django.html)
* Allow handling static files

<b>raven 6.2.1</b> : [link](https://raven.readthedocs.io/en/stable/integrations/django.html)
* Allow hooking a Django project for report on Sentry

<b>django-allauth 0.34.0</b> : [link](http://django-allauth.readthedocs.io/en/latest/index.html)
* Social Authentication for python project and account management

<b>Pillow 3.1.2</b> : [link](https://python-pillow.org/)
* Image management for Python (PIL fork)

<b>django-debug-toolbar 1.9</b> : [link](https://django-debug-toolbar.readthedocs.io/en/stable/)
* Usefull debug toolbar