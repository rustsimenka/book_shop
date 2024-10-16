run:
    sudo docker compose -f docker-compose.yml up --remove-orphans --build

fast-run:
    sudo docker compose -f docker-compose.yml up --remove-orphans

tests: run
    sudo docker -it exec app poetry run python manage.py tests