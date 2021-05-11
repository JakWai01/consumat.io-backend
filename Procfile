web: FLASK_APP=./consumatio/external/api.py flask db upgrade && gunicorn -b :$PORT --chdir ./consumatio/external api:api
