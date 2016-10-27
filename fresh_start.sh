#!/bin/sh

# rm -f db.sqlite3
python manage.py flush
python manage.py migrate
python manage.py load_salaries
python manage.py load_squads --blank
python manage.py load_draft_file
python manage.py sum_squad_salaries
