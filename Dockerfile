#Deriving the latest base image
FROM python:3.12.2-alpine

# set the working directory in the container
WORKDIR /Audit_base_AMS

#Copy requirements.txt to the working directory 
COPY requirements.txt /Audit_base_AMS/requirements.txt 

#Install all requirement and delete the file
RUN pip install -r requirements.txt && rm requirements.txt

#Copy the files below into the container's app directory
ADD fonctions_generiques.py traitement_fichiers.py main.py /Audit_base_AMS/

#Expose the port on which the container is listening
EXPOSE 5000

# command to run on container start
CMD ["python", "main.py"]