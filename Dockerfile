
FROM python:3.11.8-slim-bullseye

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1


WORKDIR /app

COPY requirements.txt .


RUN pip install -r requirements.txt


COPY . .

EXPOSE 8000
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000

