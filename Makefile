# By default, the shell is "/bin/sh" which doesn't implement `source`, so it is changed.
# https://stackoverflow.com/questions/7507810/how-to-source-a-script-in-a-makefile
SHELL := /bin/bash

CONFIG ?= resources/configuration.example.yml

run: ## Use examples: make run CONFIG="resources/configurations/".
	@source venv/bin/activate && python3 -u src/main.py --config $(CONFIG)

extract-matrices:
	@chmod +x ./resources/scripts/extract-matrices.sh
	@./resources/scripts/extract-matrices.sh

generate-requirements:
	@source venv/bin/activate && pip freeze > requirements.txt

install-requirements:
	@source venv/bin/activate && pip install -r requirements.txt

git-uncache: ## Unchaches all the files from git.
	@git rm -r --cached .

# =================================================================================================

run-sonar-qube-scanner: ## Run a SonarQube analysis. Requires SonarQube running in a Docker container.
	@source venv/bin/activate && pip install pysonar && \
		pysonar \
			--sonar-host-url=http://localhost:9000 \
			--sonar-token=sqp_aec1e4ebe86606a923c41cc18dcc006fe7a9e1ec \
			--sonar-project-key=quinki && \
		pip uninstall pysonar

docker-compose-up: ## It initializes SonarQube.
	@docker compose up

add-user-to-docker-group: ## Use in case you receive `unable to get image 'x': permission denied while trying to connect to the docker API at unix:///var/run/docker.sock`.
	@sudo usermod -a -G docker $$USER
	@newgrp docker

docker-stop-all-containers:
	@docker stop $$(docker ps -a -q)

docker-remove-all-containers: docker-stop-all-containers
	@docker rm $$(docker ps -a -q)

# =================================================================================================

help: ## Shows the available commands.
	@echo "Comandos disponibles:"
	@grep -hE '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

# =================================================================================================