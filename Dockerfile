FROM python:3.7
ADD / /code
WORKDIR /code
RUN pip install -r requirements.txt
ENV FLASK_APP=restdemo:create_app
#RUN flask db init
#RUN flask db migrate
#RUN flask db upgrade
CMD ["flask", "run", "--host", "0.0.0.0"]
