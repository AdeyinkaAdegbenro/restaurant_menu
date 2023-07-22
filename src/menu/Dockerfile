# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /app


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN apk add curl


# copy project
COPY . .
EXPOSE 8000

# RUN python manage.py migrate 
# RUN python manage.py migrate api

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "menu.wsgi"]