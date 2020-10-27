install:
	python3 -m venv ./venv && \
	source ./venv/bin/activate && \
	pip3 install --upgrade pip && \
	pip3 install -r requirements.txt

test:
	python3 -m pytest -vv --cov-report term-missing --cov=tests \
	tests/testCommandGenerator.py \
	tests/testConfigCommander.py

lint:
	pylint --disable=R,C,E1120 commandGenerator.py
	pylint --disable=R,C,E1120 configCommander.py
	pylint --disable=R,C,E1120 deviceCommander.py

all:
	install lint test