#!/bin/bash
black .
isort .
flake8
pylint steps/
mypy steps/