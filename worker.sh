#!/bin/bash

django-admin createsuperuser --username admin --email email
django-admin makemigrations
heroku run bash -a lifedjango


