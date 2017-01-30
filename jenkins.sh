#!/bin/bash
[ -d env ] || virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
# Pylint: style and syntax error
pylint -f parseable --ignore-patterns="env/" * | tee pylint.out
# Radon: metrics code
radon cc . -i "env" --xml > ccm.xml
# Test and coverage
./manage.py test --with-xunit --with-coverage --cover-xml
