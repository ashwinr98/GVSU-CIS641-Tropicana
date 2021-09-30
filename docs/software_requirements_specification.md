# Overview:
The objective of the document is to provide the list of requirements for assisting in the development process of the application at each stage. The list will keep changing at each step of the development process depending upon the possible improvements and constraints.

# Functional Requirements:

1. Frontend:
    1. The application shall allow users to upload images.
    2. The application shall send an error message to the user when the image is not in the following formats (jpg, jpeg, png, bmp).
    3. The application shall send an error message to the user if the uploaded image is over 10 MB.
2. Image Classifier:
    1. The classifier shall return the name of the insect and other related information in JSON.
    2. The classifier shall send a message to the user "Insect unidentifiable", if the accuracy of the prediction is less than 80%.
3. Integration:
    1. The application shall be able to integrate with TensorFlow and retreive results from the image classifier seamlessly.
    2. The application shall return the results of the image search within 10 seconds or an error message is shown.
    3. The application shall be built using REST APIs.

# Non Functional Requirements:

1. Classifier:
    1. The classifier shall be able to predict images accurately.
    2. The classifier shall be able to identify images with no insects.
2. Database:
    1. The application shall be able to log the details of the predictions such as accuracy, time for prediction etc.
    2. The application shall be capable of logging errors, crashes.
3. Performance:
    1. The application shall be able to load fast and perform efficiently without slowing down.
    2. The application shall be able to work on multiple browsers (Firefox, Chrome, Edge)
