# cutthecheck

An app to track the nerdiest fantasy basketball league.

Requirements:

* Python (2.7)
* virtualenv
* Git
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

## Updates

To populate or update the database, run the load command. This shoves data on rosters from the league (using the Yahoo Fantasy API) and cap hits from Spotrac.com (using a BeautifulSoup scraper) into the database. To be able to read from the Yahoo API, you must have `keyfile.txt` and `tokenfile.txt` in the base folder.

```bash
$ python manage.py load_all
```

Then fire up the local server.
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

### TK

AWS deployment
