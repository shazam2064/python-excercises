#!/usr/bin/env bash
python3 manage.py migrate
python3 manage.py loaddata graphql_api/fixtures/users.json
python3 manage.py runserver 0.0.0.0:8000
