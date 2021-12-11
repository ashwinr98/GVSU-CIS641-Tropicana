# Tropicana

The Insect Identification System is an application to identify insects and pests. The application takes the input of a image from the user and returns the insect name and other information related to the bug. 

## Team Members and Roles

* [Ashwin Rajasankar](https://github.com/ashwinr98/CIS641-HW2-Rajasankar)

## [Artifacts](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/tree/master/artifacts)

* [Use Case 1](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/functional-models/usec_checkimage.drawio.png)
* [Use Case 2](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/functional-models/usec_sendprediction.drawio.png)
* [Use Case 3](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/functional-models/usec_login.drawio.png)
* [Use Case 4](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/functional-models/usec_adminoperations.png)
* [Class Diagram](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/class_diagram.drawio.png)
* [Activity Diagram 1](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/functional-models/act_storingdata.drawio.png)
* [Activity Diagram 2](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/functional-models/act_checkimage.drawio.png)
* [Windows Navigation Diagram](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/hci/Windowsnavigationdiagram.drawio.png)

## [Documents](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/tree/master/docs)

* [Project proposal](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/docs/proposal-template.md)
* [Software requirements specifications](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/docs/software_requirements_specification_final.md)

## Prerequisites

* Node.js
* Python 3.7

To setup the python environment go to src/backend/ and run the command  

> pip install requirements.txt

## Run Instructions

To run the Django server, first create a superuser using the command in the src/backend/ directory
> python manage.py createsuperuser

After creating the superuser, start the Django server using the command
> python manage.py runserver

To install node modules, go to the src/frontend and use the command
> npm install

To start React, use the command
> npm start

This will start the application at localhost:3000


