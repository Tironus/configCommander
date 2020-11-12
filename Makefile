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

helm_install:
	helm install -f helm/values.yaml ccommander ./helm

helm_upgrade:
	helm upgrade -f helm/values.yaml ccommander ./helm

helm_uninstall:
	helm uninstall ccommander

all:
	install lint test