FROM python:2.7

RUN apt-get update
RUN apt-get install -y \
        gcc \
        gettext \
        sqlite3

RUN pip install Django==1.8.18

# Copy the application folder inside the container
ADD . /usr/src/app

# set the default directory where CMD will execute
WORKDIR /usr/src/app


# Expose ports
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]