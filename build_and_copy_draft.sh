#!/bin/sh

python manage.py load_draft_order
python manage.py build

git add rosters/management/commands/draft_order.csv
git commit -m "auto committing rosters $now"
git push origin master

cp -R -u build/cutthecheck/ ../ryanvmenezes.github.io/

cd ../ryanvmenezes.github.io/

git pull origin master
git add .
git commit -m "auto commit $now"
git push origin master

workon cutthecheck
