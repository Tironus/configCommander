install:
	pip3 install --upgrade pip && \
	pip3 install -r requirements.txt && \
	export APP_DIR=$(pwd)

test:
	python3 -m pytest -vv --cov-report term-missing --cov=tests \
	tests/testCommandGenerator.py \
	tests/testConfigCommander.py

lint:
	pylint --disable=R,C,E1120 commandGenerator.py
	pylint --disable=R,C,E1120 configCommander.py
	pylint --disable=R,C,E1120 deviceCommander.py

upgrade:
	sudo su
	sudo helm upgrade -f helm/values.yaml ccommander ./helm

all:
	install lint test