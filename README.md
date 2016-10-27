# cutthecheck

A Django app to track the nerdiest fantasy basketball league.

Requirements:

* Python (2.7)
* virtualenv
* git
* files with the keys and tokens needed to interact with the Yahoo! Fantasy API

## Getting started

Create a virtualenv for all of the python packages needed, then install those packages.

```bash
$ virtualenv cutthecheck
$ cd cutthecheck
$ . bin/activate
$ git clone git@github.com:ryanvmenezes/cutthecheck.git repo
$ cd repo
$ pip install -r requirements
```

This app populates a small sqlite database. It will be created with all the necessary database tables like so:

```bash
$ python manage.py migrate
```

## Management commands

### Starting from scratch

`python manage.py load_salaries`
* Downloads the freshest cap hits from [spotrac](http://www.spotrac.com/nba/cap/) using a BeautifulSoup scraper

`python manage.py load_squads --blank`
* Populates teams from the Yahoo league and attempts to merge it with existing cap data. The `--blank` flag creates empty teams. To be able to read from the Yahoo API, you must have `keyfile.txt` and `tokenfile.txt` in the base folder.

`python manage.py load_draft_file`
* Update the draft results from a flat file

`python manage.py sum_squad_salaries`
* A manual push to save the salaries for each team

### Saving work

`python manage.py dump_salaries`
* Save the "Salary Bible"

`python manage.py dump_draft_file`
* Save the progress of the draft




## Updates

To populate or update the database, run the load command. This shoves data on rosters from the league (using the Yahoo Fantasy API) and cap hits from Spotrac.com (using a BeautifulSoup scraper) into the database. To be able to read from the Yahoo API, you must have `keyfile.txt` and `tokenfile.txt` in the base folder.

```bash
$ python manage.py load_all
```

Then fire up the local server. (Ctrl-C to quit it.)
```bash
$ python manage.py runserver
```

Navigate to [http://localhost:8000/](http://localhost:8000/) to see the site in action and ensure the pages are loaded properly.

**Features**
* A salary audit for the entire league
* Profile pages for all 10 teams
* The Salary Bible

## Creating flat files

To build the dozen or so pages as flat files, run the following [django-bakery](http://django-bakery.readthedocs.org/en/latest/) command:

```bash
$ python manage.py build
```

This should create a `build/` directory that will hold flatfiles. Running `python manage.py buildserver` should allow you to navigate the baked-out files.

### TK

AWS deployment
