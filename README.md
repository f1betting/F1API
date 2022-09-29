# F1API

A more user-friendly way to use [ergast.com](https://ergast.com/mrd/)!

## Docker

Build image using

````shell
$ docker build -t f1api .
````

Alternatively you can use the docker hub [repository](https://hub.docker.com/r/nieko3/f1api) using:

````shell
$ docker pull nieko3/f1api
````

Run container using:

````shell
$ docker run --env-file ./.env -d --name f1api -p 8000:80 f1api
````