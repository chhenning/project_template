.PHONY: help test say shout repeat

# Variables

# "source" allows setup.sh to export env vars to the Python script
SETUP_CMD := . ./scripts/setup.sh
PYTHON    := python
SCRIPT    := app_name/app.py
PRE       := $(SETUP_CMD) &&

help:
	@$(PYTHON) $(SCRIPT) --help

test:
	$(PRE) pytest -q

say:
	$(PRE) $(PYTHON) $(SCRIPT) say --msg "$(MSG)"

shout:
	$(PRE) $(PYTHON) $(SCRIPT) shout --msg "$(MSG)"

repeat:
	$(PRE) $(PYTHON) $(SCRIPT) repeat --msg "$(MSG)" --times $(TIMES)