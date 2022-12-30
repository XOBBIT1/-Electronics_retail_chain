FROM python:3.10 as base

WORKDIR /erc

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv

RUN pipenv install --system

COPY ./ ./

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]