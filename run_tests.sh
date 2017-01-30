#!/bin/bash
[ -d env ] || virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
./manage.py test --with-xunit --with-coverage --cover-xml
