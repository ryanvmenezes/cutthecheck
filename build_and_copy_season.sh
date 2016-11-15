#!/bin/sh

workon cutthecheck

python manage.py load_salaries
python manage.py load_squads
python manage.py build

python manage.py dump_salaries

git add .
git commit -m "auto committing $now"
git push origin master

cp -R -u build/cutthecheck/ ../ryanvmenezes.github.io/

cd ../ryanvmenezes.github.io/

git add .
git commit -m "auto commit $now"
git push origin master

workon cutthecheck
