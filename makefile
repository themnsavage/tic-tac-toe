game:
	python3 main.py

setup:
	pip install -r requirements.txt

tests:
	python3 -m pytest

clean:
	rm -rf .pytest_cache module/app/__pycache__ module/test/__pycache__