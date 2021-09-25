# Cartloop Demo

## Contains docker based django application with celery, redis and postgres.

## Installation

Cartloop Demo requires [docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/) to run.

First of all, clone the repo and go inside the root folder
If running application first time
```sh
docker-compose up --build
```
If running application not first time
```sh
docker-compose up ( -d optinal for keeping in background )
```
To create superuser once all containers are running in next tab
```sh
docker-compose exec web python manage.py createsuperuser
```
Now you can access the application on http://localhost

## Process to test

Dillinger uses a number of open source projects to work properly:

- create two users in django admin panel using http://localhost/admin
- Make one record for that as client in client table in django admin panel using http://localhost/admin
- Make another record another user as operator in operator table in django admin panel using http://localhost/admin
- Similarly create store and discount code in respective tables from django admin panel using http://localhost/admin
- Now make one conversation by selecting client and operator in django admin panel using http://localhost/admin
- Start creating chat from root path which is django rest framewor browser api http://localhost/chat.
- Make sure to login http://localhost/api/login/?next=/chat
- You can see celery task results in django admin panel task results using http://localhost/admin.
- You can see logs and all data inside docker container.


> The application contains bare minimum code, does not contain
> any login and logout api and no permission
> class implemented. The idea is that to
> focus more on the assigned required 
> task.