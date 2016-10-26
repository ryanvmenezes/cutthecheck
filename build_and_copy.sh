#!/bin/sh
python manage.py sum_squad_salaries
python manage.py dump_draft_file
python manage.py build
cp -R -u build/cutthecheck/ ../ryanvmenezes.github.io/

cd ../ryanvmenezes.github.io/
git add .
now="$(date)"
git commit -m "auto commit $now"
git push

workon cutthecheck
