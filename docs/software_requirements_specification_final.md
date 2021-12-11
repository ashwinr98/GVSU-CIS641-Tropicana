# Overview:
The objective of the document is to provide the list of requirements for assisting in the development process of the application at each stage. The list will keep changing at each step of the development process depending upon the possible improvements and constraints. The documents also provides the user the features available and directions to use them.

# Software Requirements

The section describes the features of the application. Functional requirements describe the basic features that the user should have access to. Nonfunctional requirements are requirements which describe the quality of the system.
 
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
| FR8 | The image classifier shall be able to send the classification results back to the user. |
| FR9 | The image classifier shall be able to integrate with the backend. |
| FR10 | The image classifier shall be accurate in predicting insects. |

### Backend
| ID | Requirement |
| :-------------: | :----------: |
| FR11 | The backend shall be able to integrate seamlessly with the frontend. |
| FR12 | The backend shall be able to retreive results from the image classifier. |
| FR13 | The backend shall have APIs for admin dashboard, showing image data and predicting images. |
| FR14 | The backend shall be able to connect and update the database. |
| FR15 | The backend shall function efficiently without crashing. |

### Admin Interface
| ID | Requirement |
| :-------------: | :----------: |
| FR16 | The admin shall be able to login to the admin interface using their credentials. |
| FR17 | Other users shall not be able to login to the admin interface. |
| FR18 | The admin shall be able to view image search data of users from the admin interface. |
| FR19 | The admin shall be able to modify and delete image search data of users from the admin interface. |
| FR20 | The admin shall have an option to change the password of the login. |

### Database
| ID | Requirement |
| :-------------: | :----------: |
| FR21 | The database shall be able to store data of the image title and description. |
| FR22 | The database shall be able to integrate with the backend. |
| FR23 | The database shall allow only the admin to view and modify the data. |
| FR24 | The database shall allow the admin to delete the data. |
| FR25 | The database shall be fast in retreiving queries. |


## Non-Functional Requirements

### Operational Requirements
| ID | Requirement |
| :-------------: | :----------: |
| NFR1 | The application shall be able to work on Firefox, Chrome and Edge. |
| NFR2 | The application shall be able to run on Windows and Linux. |
| NFR3 | The application shall not require internet to operate. |
| NFR4 | The application shall be able to work smoothly without crashing. |
| NFR5 | The application shall not consume too much resources of the system. |

### Performance Requirements
| ID | Requirement |
| :-------------: | :----------: |
| NFR6 | The image classifier shall be able to classify images within 3 seconds. |
| NFR7 | The Django backend shall send the image to the image classifier within a second. |
| NFR8 | The React frontend shall display the results within a second after receiving the prediction result from Django. |
| NFR9 | The React frontend shall start within 3 minutes of starting it. |
| NFR10 | The image classifier shall be able to predict insects correctly. |

### Design Requirements
| ID | Requirement |
| :-------------: | :----------: |
| NFR11 | The backend of the application shall be designed using Django. |
| NFR12 | The frontend of the application shall be designed using React. |
| NFR13 | SQLite shall be used as the database for the application. |
| NFR14 | Tensorflow shall be used to create the image classifier. |
| NFR15 | REST APIs shall be used in the application for data communication between the frontend and backend. |

### Security Requirements
| ID | Requirement |
| :-------------: | :----------: |
| NFR16 | Only the admin shall be able to access the admin interface. |
| NFR17 | Only the admin shall be able to view the database. |
| NFR18 | Only the admin shall be able to delete data from the database. |
| NFR19 | The admin password shall be held confidential. |
| NFR20 | The application shall make sure to prevent any external breach in the data. |

### Reliability Requirements
| ID | Requirement |
| :-------------: | :----------: |
| NFR21 | The application shall be able to handle multiple concurrent requests at a time. |
| NFR22 | The application shall have less downtime. |
| NFR23 | The application shall be updated to a new version once every three months. |
| NFR24 | The application shall be tested for bugs and debugged frequently. |
| NFR25 | The application shall have a user feedback portal, where the users recommend new features and bug fixes. |

# Change Management Plan

A change management plan will be done for the implementation of the Insect Identification System. The plan will 
help new users understand how the application works and how to utilize its 
features. 

## Training

For training, the users will be initially given a demo of the application.
After the demo, a Q&A session will be conducted to address users doubts.
The following week the users will be getting the application to use.
The users will be trained on how to upload the image to the React frontend and how to get the result of the prediction.
The admin user will also be trained on how to login to the admin interface and access the search data from the database.
The users will have an another Q&A session after they have used the application for a week. 

## Integration

The application is designed to be operational on Windows and Linux and can be used on browsers such as Firefox, Chrome and Edge. This makes the application easy to integrate with any ecosystem.
The system administrators will be given instructions on how to deploy the Django backend and React frontend and how to set up the production environment. A Q&A session will be organized with the system administrators to make sure they don't have any problems.

## Issue Resolution

There will be a user feedback portal, in which the user can report bugs and request features.
The issues in the feedback portal will be resolved in a new version of the application which will be released once every three months.
If the user has any immediate issues  or doubts they can email the system administrator for help. 

# Traceability Links

The section provides the link between the artifacts created for the development of the project and the software requirements of the project.

## Use Case Diagram Traceability
| Artifact ID | Artifact Name | Requirement ID |
| :-------------: | :---------- | :---------- |
| [Use Case 1](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/functional-models/usec_checkimage.drawio.png) | Check image format | FR1, FR5 |
| [Use Case 2](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/functional-models/usec_sendprediction.drawio.png) | Sending prediction data and storing image data | FR1, FR3, FR5, FR18, FR21, NFR17 |
| [Use Case 3](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/functional-models/usec_login.drawio_v2.png) | View search history and admin login | FR16, FR17, NFR16-18 |
| [Use Case 4](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/functional-models/usec_adminoperations.png) | Admin operations | FR18, FR19, NFR17, NFR18 |

## Class Diagram Traceability
| Artifact Name | Requirement ID |
| :-------------: |:----------: |
| [Image classifier class diagram](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/class_diagram.drawio.png) | FR1, FR2, FR6, FR21|

## Activity Diagram Traceability
| Artifact ID | Artifact Name | Requirement ID |
| :-------------: | :----------: | :----------: |
| [Activity Diagram 1](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/functional-models/act_storingdata.drawio.png) | Store Data | FR1-5, FR21 |
| [Activity Diagram 2](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/functional-models/act_checkimage.drawio.png) | Check Image | FR1, FR4, FR5, FR7|

# Software Artifacts
The artifacts listed below help understand the features and functions of the Insect identification system.
* [Use Case 1](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/functional-models/usec_checkimage.drawio.png)
* [Use Case 2](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/functional-models/usec_sendprediction.drawio.png)
* [Use Case 3](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/functional-models/usec_login.drawio.png)
* [Use Case 4](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/functional-models/usec_adminoperations.png)
* [Class Diagram](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/class_diagram.drawio.png)
* [Activity Diagram 1](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/functional-models/act_storingdata.drawio.png)
* [Activity Diagram 2](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/functional-models/act_checkimage.drawio.png)
* [Windows Navigation Diagram](https://github.com/ashwinr98/GVSU-CIS641-Tropicana/blob/master/artifacts/hci/Windowsnavigationdiagram.drawio.png)