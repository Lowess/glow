### Local developement

.PHONY: dev tests lint checkstyle coverage docs

build:
	python setup.py sdist
run:
	@echo 🚀 Starting application...
	FLASK_ENV=development FLASK_APP=lib/glow flask run -h 0.0.0.0

dev:
	@echo ⚙️ Setting up dev environment and dependencies...
	pip install -r dev/requirements.txt

tests:
	$(MAKE) lint
	$(MAKE) checkstyle
	$(MAKE) coverage

lint:
	@echo 💠 Linting code...
	tox -e lint

checkstyle:
	@echo ✅ Validating checkstyle...
	tox -e checkstyle

coverage:
	@echo 🔍️  Run test coverage...
	tox -e coverage

docs:
	@echo 📚 Generate documentation using sphinx...
	$(MAKE) -C ./docs/sphinx html
