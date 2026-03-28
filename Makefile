# By default, the shell is "/bin/sh" which doesn't implement `source`.
# https://stackoverflow.com/questions/7507810/how-to-source-a-script-in-a-makefile
SHELL := /bin/bash

run:
	@source venv/bin/activate && python3 -u src/main.py

extract-matrices:
	@chmod +x ./resources/scripts/extract-matrices.sh
	@./resources/scripts/extract-matrices.sh

generate-requirements:
	@source venv/bin/activate && pip freeze > requirements.txt

install-requirements:
	@source venv/bin/activate && pip install -r requirements.txt