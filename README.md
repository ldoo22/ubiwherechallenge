# ubiwherechallenge
Did not complete the challenge :( I would required more time (time spent: saturday afternoon and sunday morning). What I did:
- Postgres + postgis
	- Used prebuilt docker image: mdillon/postgis
- Django + GDAL
	- Used prebuilt docker image with python and GDAL: andrejreznik/python-gdal
	- installed py required packages: django; djangorestframework; djangorestframework-gis; psycopg2
- Created docker-compose with above images and sharing common network
	- Used host mount volume to develop in django+gdal image
- Created diagram model for this exercicie (more on that bellow)
- Create CRUD for each SQL diagram entity, but only with ID lookup.
- Added Admin and Guest Groups

## Sql
On the sql entity relationship diagram I was having trouble defining the AverageSpeed table because of my interpretation of the "intensidade" and "caracterização" fields (more on that on sent e-mail)
- Location (unique)
	- point: PointField
- Segment (with unique combination of fields constrain)
	- start: Location
	- end: Location
- AverageSpeed
	- time: TimeField
	- average_speed: FloatField
	- intensity: PositiveInteger
	- characterization: CharField
	- segment: Segment

## Run
1. Clone repo
2. docker-compose -up d
3. exec into django_dev (ideally would also have a DockerFile image for production with gunicorn and enviroment variables setup instead of hardcoded)
4. python manage.py createsuperuser
5. python manage.py runserver 0.0.0.0:8000
6. got to localhost:admin/ on browser, login, create AdminGroup(with all permission) and GuestGroup(ReadOnly permission). Ideally I would have exported my development docker volume of the DB and shared it here.
7. in folder postman there is collection to interact with the backend, only has Create and Read calls inspite entire CRUD being implemented in views.py (only works by providing ID of related entities).

## TODO
- Create CRUD for Segment and AverageSpeed(meassurements) but instead of providing the foreign keys, the http request would provide a longitude and latitue and the backend would handle on finding them on data base or create if it did not exist. with that, one could more easilly implement a python script to load data from: https://github.com/Ubiwhere/traffic_speed and inject into DB.
- Properly set configuration varaibles instead of being hardcoded (for example the django secretkey is still hardcoded)
- Create production DockerFile for backend
- Add to postman all required CRUD
- Fix all todos and code documentation, clean unused template django files
- And finally, of course, finish the challenge requirements