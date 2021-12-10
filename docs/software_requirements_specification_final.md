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
| NFR1 | The application shall be able to handle multiple concurrent requests at a time. |
| NFR1 | The application shall have less downtime. |
| NFR1 | The application shall be updated to a new version once every three months. |
| NFR1 | The application shall be tested for bugs and debugged frequently. |
| NFR1 | The application shall have user feedback portal, where the users recommend new features and bug fixes. |


##Change Management Plan
