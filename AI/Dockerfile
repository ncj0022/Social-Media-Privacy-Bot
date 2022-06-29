#Create a ubuntu base image with python 3 installed.
FROM python:3.8-buster

#Set the working directory
WORKDIR /AI

#copy all the files
COPY . .

#Install the dependencies
RUN apt-get -y update
RUN pip3 install -r requirements.txt
#Expose the required port
EXPOSE 5001

#Run the command

CMD ["flask", "run", "--port=5001", "--host=0.0.0.0"] 