## The Fusca

This project is under MIT License and has the pourpose to educate about the tecnologies:

- Django
- Docker
- Flutter

### About the goal

The goal in this project is to have a backend in Django and a App in Flutter to keep track of "everything" i did to my Beetle, things like when i buyed, technical characteristics, mechanics, when i need to change oil, what is the gás consume and more.

### How to run

- First create a file ```.env``` that is based of ```.env.template```
- Create a virtualenv using the pipenv, to install it:
    - ```pip install --user pipenv```
    - ```pipenv install``` to install all packages needed
- Run docker to use postgres (see the section bellow how to do it)
- Run ```make run-migrate``` if it is the first time running, because it will run the ```migrations ```and ```collectstatic``` too
    - If it's not the first time running, run ```make run```

### How to connect to postgres in docker

- Create a docker container with ```make run-db```
    - You must have Docker and docker-compose installed
- Got to http://localhost:5051/ in your browser:
    - Login with the user as ```pgadmin@root.com``` and password as ```root```
        - You can change it on ```.env.template``` on the variables ```PGADMIN_DEFAULT_EMAIL``` and ```PGADMIN_DEFAULT_PASSWORD```
    - Click on ```Add New Server```
    - Put a name of your project and click on ```Connection```
    - In the host field place ```db``` or the name of service in ```docker-compose.yml``` that is related to ```postgres```
    - In the username field place ```django``` and password ```lookatthat```
        - You can change it on ```.env.template``` on the variables ```DATABASE_USER``` and ```DATABASE_PASSWORD```

## Versioning

- ```git checkout main && git pull```
- ```git merge --no-ff develop```
- ```git tag -a 0.0.0.0```
- ```git checkout develop && git merge --no-ff 0.0.0.0```
- ```git push origin develop main 0.0.0.0```
