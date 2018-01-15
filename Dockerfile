FROM ubuntu:latest
MAINTAINER Abdesslem Amri "amriabdesslem@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
#ENTRYPOINT ["python"]
#CMD ["python project/manage.py runserver 0.0.0.0:8000" ]
CMD ["python", "project/manage.py", "runserver", "0.0.0.0:8000"]
