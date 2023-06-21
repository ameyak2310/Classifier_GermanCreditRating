all:
	install
	lint

install:
	pip install --upgrade pip 
	pip install -r requirements.txt

lint:
	pylint --disable=R,C main.py

freeze:
	pip freeze > requirements.txt

localapp:
	python3 main.py

corn:
	gunicorn --bind 0.0.0.0:6000 main:app

tryout:
	python3 tests/response.py

senv:
	python3 -m venv .venv
	source .venv/bin/activate

killports:
	sudo lsof -iTCP:8080 -sTCP:LISTEN
	kill 12017(whatever the PID is)