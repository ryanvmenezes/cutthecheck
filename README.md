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

This app populates a small sqlite database. Fire it up.

```bash
$ python manage.py migrate
```

Then run the loader, which shoves data from Spotrac.com and the league into the database.

```bash
$ python manage.py load_all
```

Fire up a test server.
```bash
$ python manage.py runserver
```

Navigate to http://localhost:8000/audit

