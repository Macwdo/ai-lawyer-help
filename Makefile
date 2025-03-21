# Lint
lint:
	@echo "Running lint format 🧹"
	-@ ruff format & ruff check --fix

lint_unsafe:
	@echo "Running lint unsafe format 🧹"
	-@ ruff format & ruff check --unsafe-fixes --fix


# Test
test:
	@echo "Cleaning up coverage files 🧹"
	-@ coverage erase

	@echo "Running tests 🧪..."
	-@ coverage run manage.py test

	@echo "\n\n"
	@echo "Test results 📊..."

	-@ coverage html

test_parallel:
	@echo "Cleaning up coverage files 🧹"
	-@ coverage erase

	@echo "Running tests 🧪..."
	-@ coverage run manage.py test --parallel

	@echo "\n\n"
	@echo "Test results 📊..."

	-@ coverage html

# Database
migrate:
	@echo "Running migrations 🚚"
	-@ python manage.py migrate

migrations:
	@echo "Creating migrations 🚚"
	-@ python manage.py makemigrations

remove_migrations:
	@echo "Removing migrations 🚚"
	-@ rm -rf **/migrations/00*

# Admin
createadmin:
	@echo "Creating admin user 🦸"
	-@ python manage.py createsuperuser --email admin@admin.com

createsuperuser:
	@echo "Creating super user 🦸"
	-@ python manage.py createsuperuser

# Static files
collectstatic:
	@echo "Collecting static files 📦"
	-@ python manage.py collectstatic --noinput

collectstatic_container:
	@echo "Collecting static files 📦"
	-@ docker exec -it $(APP_NAME) uv run python manage.py collectstatic --noinput

# Infra
up_dev:
	@echo "Setting up Application Infrastructure... 🚀"
	-@ docker compose -f docker-compose.yml down
	-@ docker compose -f docker-compose.yml up -d

up_dev_build:
	@echo "Setting up Application Infrastructure... 🚀"
	-@ docker compose -f docker-compose.yml down
	-@ docker compose -f docker-compose.yml up -d --build

run_dev:
	@echo "Running the project in development mode 🚀"
	-@ docker compose -f docker-compose.yml down
	-@ docker compose -f docker-compose.yml up

down_dev:
	@echo "Stopping the project 🛑"
	-@ docker compose -f docker-compose.yml down

clean:
	@echo "Cleaning up the project 🧹"
	-@ sudo rm -rf ./.data

attach:
	@echo "Attaching to the project 🚀"
	-@ docker attach $(APP_NAME)

connect:
	@echo "Connecting to the project 🚀"
	-@ docker exec -it $(APP_NAME) /bin/bash

## Build
build:
	@echo "Building the project 🏗️"
	-@ docker build -t $(APP_NAME) .

build_nginx:
	@echo "Building nginx 🏗️"
	-@ cd infra/nginx && docker build -t $(APP_NAME)-nginx .

# Nginx
nginx_log_error:
	@echo "Showing nginx error logs 📜"
	-@ docker exec -it $(APP_NAME)-nginx tail -f /var/log/nginx/error.log

nginx_log_access:
	@echo "Showing nginx access logs 📜"
	-@ docker exec -it $(APP_NAME)-nginx cat /var/log/nginx/access.log

# Run
run:
	@echo "Running the project in development mode 🚀"
	-@ python manage.py runserver

# Setup
setup_dev:
	@echo "Setting up the development environment 🚀"
	-@ uv sync

	@echo "Copying the .env file 🚀"
	-@ cp .env.development .env
