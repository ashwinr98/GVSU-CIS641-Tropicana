# Overview:
The objective of the document is to provide the list of requirements for assisting in the development process of the application at each stage. The list will keep changing at each step of the development process depending upon the possible improvements and constraints. The documents also provides the user the features available and directions to use them.

# Table of contents
* [Functional Requirements](#functional-requirements)
* [Nonfunctional Requirements](#non-functional-requirements)
* [Change Management Plan](#change-management-plan)
* [Traceability Links](#traceability-links)
* [Software Artifacts](#software-artifacts)

## Functional Requirements

### Frontend
| ID | Requirement |
| :-------------: | :----------: |
| FR1 | The frontend shall allow users to upload images. |
| FR2 | The frontend shall allow users to set a title and content (description) to the image. |
| FR3 | The frontend shall show the prediction result of the image to the user along with its accuracy. |
| FR4 | The frontend shall have a browse button for the user to select an image from the local system. |
| FR5 | The frontend shall only allow images to be uploaded. |

### Image Classifier
| ID | Requirement |
| :-------------: | :----------: |
| FR6 | The image classifier shall be able to classify different insects. |
| FR7 | The image classifier shall be able to receive the image from Django. |
| FR8 | The image classifier shall be send the classification results back to the user. |
| FR9 | The image classifier shall be created using Tensorflow. |
| FR10 | The image classifier shall be accurate in predicting insects. |

### Django Backend
| ID | Requirement |
| :-------------: | :----------: |
| FR5 | The backend shall be able to integrate with the React frontend. |
| FR5 | The backend shall be able to retreive results from the image classifier. |
| FR5 | The backend shall be built using REST APIs. |
| FR5 | The backend shall be able to connect and update the database. |
| FR5 | The backend shall be able to  |
| FR5 |  |

### Admin Interface
| ID | Requirement |
| :-------------: | :----------: |
| FR5 | The admin shall be able to login to the admin interface. |
| FR5 | Other users shall be unable to login to the admin interface. |
| FR5 | The admin shall be able to view image search data of users from the admin interface. |
| FR5 | The admin shall be able to modify and delete image search data of users from the admin interface. |
| FR5 | The admin shall have an option to change the password of the login. |

### Database
| ID | Requirement |
| :-------------: | :----------: |