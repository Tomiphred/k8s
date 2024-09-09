FROM python:3.10

#Create a folder to run your application
RUN mkdir /app

#Define your working directory where i want my app to run
WORKDIR /Tomi

#Copy all requirement for the flask project to docker Workdir
COPY requirement.txt /Tomi/

#Install all dependencies 
RUN pip3 install -r requirement.txt

#Copy all application file into the docker Working directory
COPY . /Tomi/

#Open Port you want your application run
EXPOSE 4000

#
CMD [ "uvicorn", "app:asgi_app", "--host=0.0.0.0", "--port=4000" ]