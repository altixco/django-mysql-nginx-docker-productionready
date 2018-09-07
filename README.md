# django-mysql-nginx-docker-productionready
Django 2.1 + Mysql 8 + Nginx + Letsencrypt + Docker (Production Ready)

## Documentation ##

### Directory Tree ###
```
├── Dockerfile
├── LICENSE
├── Makefile
├── README.md
├── config
│   ├── nginx
│   │   └── project_name.conf
│   ├── nginx-dev
│   │   └── project_name.conf
│   └── requirements.txt
├── docker-compose.yml
├── docker-production.yml
├── scripts
│   ├── command-dev.sh
│   └── wait-for-it.sh
└── src
    ├── __init__.py
    ├── main
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── fixtures
    │   │   └── dev.json
    │   ├── migrations
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── manage.py
    ├── media
    │   └── Readme.md
    ├── project_name
    │   ├── settings
    │   │   ├── common.py
    │   │   ├── development.py
    │   │   └── production.py
    │   ├── static
    │   │   └── Readme.md
    │   ├── urls.py
    │   └── wsgi.py
    ├── static
    │   └── Readme.md
    └── templates
        └── Readme.md
```

### How to install the template ###

Clone the repository, and update your origin url: 
```
git clone https://github.com/altixco/django-mysql-nginx-docker-productionready project_name
cd project_name
```

Rename your project files and directorys:
```
make name=project_name init`
```
> Info: Make is required, for mac run `brew install make`

The command before will remove the `.git` folder so you will have to initialize git:
```
git init
git remote add origin <repository-url>
```

### How to run the project ###

The project use docker, so just run:

`docker-compose up`

> If it's first time, the images will be created. Sometimes the project doesn't run at first time because the init of mysql, just run again `docker-compose up` and it will work.

*Your app will run in the port 8000: `localhost:8000`*

## Production Deployment: ##

To deploy use `docker swarm` and `docker stack`.

To init a swarm use:
```
docker swarm init --advertise-addr=<ip_address>
```

Create the docker secrets:
```
echo "<secret>" | docker secret create <secret_name> -
```

Current secrets are:

* django_secret_key
* mysql_user
* mysql_password
* email_password

Initialize your app with the command:
```
docker stack deploy -c docker-production.yml --with-registry-auth bb404
```
