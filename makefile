# venv name
VENV_NAME = venv

# FastAPI entry
APP_PATH = app.main:app

# start env and app
run: $(VENV_NAME)/bin/activate
	@echo "Running FastAPI server..."
	. $(VENV_NAME)/bin/activate && uvicorn $(APP_PATH) --reload

# create venv and install dependencies
$(VENV_NAME)/bin/activate: requirements.txt
	@echo "Setting up virtual environment..."
	python3 -m venv $(VENV_NAME)
	. $(VENV_NAME)/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	@touch $(VENV_NAME)/bin/activate