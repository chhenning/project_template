.PHONY: test run 

test:
	pytest -q

run:
	python app_name/app.py run --param Love

