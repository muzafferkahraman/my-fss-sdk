init:
	pip install -r requirements.txt

run_tests:
	PYTHONPATH=./ pytest tests -v


.PHONY: init run_tests

