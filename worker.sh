#!/bin/bash

django-admin createsuperuser --username admin --email email
django-admin makemigrations
