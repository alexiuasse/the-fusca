#!make

DOCKER_PROJECT_NAME := $(DOCKER_PROJECT_NAME)

export COMMIT_TAG=$(shell git describe --tags)
export LAST_VERSION_TAG=$(shell git describe --tags --abbrev=0)
export CODE_VERSION=$(shell git describe --dirty)

_DOCKER_COMPOSE_FILE=docker-compose.yml

clean:
	@docker-compose -f $(_DOCKER_COMPOSE_FILE) -p $(DOCKER_PROJECT_NAME) down
	@$( $(shell docker ps -q --filter="name=$(DOCKER_PROJECT_NAME)") | docker stop )
	@$( $(shell docker ps -a -q --filter="name=$(DOCKER_PROJECT_NAME)") | docker rm )
	@$( $(shell docker images -q --filter="reference=*$(dDOCKER_PROJECT_NAME)*") | docker rmi )

run:
	@docker-compose -f $(_DOCKER_COMPOSE_FILE) -p $(DOCKER_PROJECT_NAME) build
	@docker-compose -f $(_DOCKER_COMPOSE_FILE) -p $(DOCKER_PROJECT_NAME) up -d --force-recreate --remove-orphans
	$(MAKE) logs

db-load-backup:
	docker exec -i fdp_postgres pg_restore --verbose --clean --no-acl --no-owner -h localhost -U django -d django-db < ./database/init/backup

logs:
	@docker-compose -f $(_DOCKER_COMPOSE_FILE) -p $(DOCKER_PROJECT_NAME) logs -f -t

admin:
	./manage.py createsuperuser

update-models:
	./manage.py makemigrations
	./manage.py migrate

test:
	./manage.py test

collectstatic:
	./manage.py collectstatic

# run:
# 	./manage.py runserver 0.0.0.0:8000

run-migrate:
	$(MAKE) update-models
	$(MAKE) collectstatic
	$(MAKE) run

makemessages:
	django-admin makemessages -l pt_BR

compilemessages:
	django-admin compilemessages
