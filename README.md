# conference-reservation

Application to rent a conference room. 
Functionalities:
* Rent available conference room.
* Add new conference room.
* Edit conference room.
* List of all conference rooms and information whether it's avalable or not.

## Technology Stack
* Django
* PostgreSQL
* Javascript
* jQuery
* Bootstrap4

## Installation
1. Clone repository
2. Create virtualenv
3. Activate virtualenv `source <venv_name>/bin/activate`
4. Install python dependencies `pip install -r requirements.txt`
5. Setup psql database called `conference_reservation`
6. Change password and user to your credentials in settings.py
7. Migrate - `python manage.py migrate`
8. `python manage.py runserver`

Enjoy!
