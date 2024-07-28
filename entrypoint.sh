#!/bin/bash
if $TEST; then
    poetry run python src/database/exec_create_all.py
    poetry run coverage run -m pytest
    poetry run coverage report --fail-under=70
else
    if $GUNICORN; then
        poetry run python src/database/exec_create_all.py
        HOME=/root poetry run gunicorn --bind :80 --workers 1 --threads 1 src.app:gunicorn_app
    else
        poetry run python src/database/exec_create_all.py
        poetry run python src/app.py
    fi
fi