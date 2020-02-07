FROM django

ADD . /Django-Mongo-keyur

WORKDIR /Django-Mongo-keyur

RUN pip install -r requirements.txt

CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]
