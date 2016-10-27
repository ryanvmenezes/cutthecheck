#!/bin/sh

python manage.py sum_squad_salaries
python manage.py dump_draft_file
python manage.py build

git add rosters/management/commands/league_draft.csv
git commit -m"auto committing rosters $now"
git push origin master

cp -R -u build/cutthecheck/ ../ryanvmenezes.github.io/

cd ../ryanvmenezes.github.io/

git add .
git commit -m "auto commit $now"
git push origin master

workon cutthecheck
