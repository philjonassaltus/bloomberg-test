# bloomberg-test

### Set up virtual env
`virtualenv --python=python3.13 ./venv`
### Run virtual env
`python3 -m venv ./venv && source ./venv/bin/activate`
### To install yfinance
`python3 -m pip install yfinance`
### Finally
`python3 main.py`

### Make migrations 
`python3 manage.py migrate`
### Run django on localhost:1234
`python3 manage.py runserver 1234`
