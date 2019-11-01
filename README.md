# restcaperoom

restcaperoom is a REST API Escape room.

## Starting

Running as a Python program:
```
$ python3 -m openapi_server
```

The environment variable BASE_URL should contain the endpoint url where the API can be reached. When not set, it will default to http://localhost:8080

Running as a docker container:
```
$ docker build -t restcaperoom .
$ docker run -p 8080:8080 -t restcaperoom
```

To run as a Google Cloud App Engine, change the BASE_URL environment variable in app.yaml and deploy the app:
```
$ gcloud app deploy . --project=<your project id>
```

## Entering the escape room

When the app is running, several resources can be requested from the API through HTTP(S). The API specification is at ${BASE_URL}/ui (e.g. http://localhost:8080/ui)
The root of the API (e.g. http://localhost:8080) will return you the door through which you enter the escape room.


