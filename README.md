# django-mysql-nginx-docker-productionready
Django 2.1 + Mysql 8 + Nginx + Letsencrypt + Docker (Production Ready)

## Documentation ##

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

The command before will remove the `.git` folder so you will have to initialize git:
```
git init
git remote add origin <repository-url>
```

> Info: Make is required, for mac run `brew install make`

### How to run the project ###

The project use docker, so just run:

`docker-compose up`

> If it's first time, the images will be created.
> Sometimes the project doesn't run at first time because the init of mysql, just run again `docker-compose up` and it will work.

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
