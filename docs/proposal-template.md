Team name: Tropicana

Team members: Ashwin Rajasankar

# Introduction

Insects are pesky pests that cause nuisance to people who garden and farm. Some insects could destroy entire gardens and fields, if left unchecked. The first step to efficiently eradicate them is to identify them. But identifying them manually is not an easy task for a person who is not an entomologist (a scientist who studies insects) or doesn't have prior knowledge about insects, as there are around [900,000 species of insects in the world](https://www.si.edu/spotlight/buginfo/bugnos) (80% of world's species). The project aims to assist farmers, gardeners, bug enthusiasts and nature lovers who want to find the ID of a bug.

In the project, Django will be used for creating the frontend and backend. The user will have an interface with an option to upload an image. Once the image is uploaded, the image classifier will give a prediction of the insect's name along with the accuracy of the prediction. Details about the insect's favorite plants and ways to repel the insect will also be displayed to the user.

# Anticipated Technologies

* Python
* Django
* TensorFlow

# Method/Approach

* Initially collect image data of insects and add them to a dataset.
* Clean the data and remove redundant data.
* Create an image classifier model in TensorFlow and train it using the gathered data.
* Create a website using Django and an interface for uploading images.
* Improve the prediction results by continuous testing on the image classifier and updating data.

# Estimated Timeline

* Gathering data and preprocessing (1 Week)
1. Analyze online insect image datasets.
2. Gather and compile data from online datasets and create a new dataset.
3. Clean the data and remove inconsistencies in the dataset.

* Backend and Frontend development (2 Weeks)
1. Create a Django website.
2. Develop backend APIs to get the input and to give users the result.
3. Design a frontend user interface with the option to upload an image.
4. (Optional, depends on time) Create a login page and save data of user's searches.

* Image classifier training and testing (3 Weeks)
1. Create image classifier in TensorFlow.
2. Train the image classifier with the created dataset.
3. Test the image classifier with multiple data and analyze the accuracy of the predictions.
4. Using the data acquired from testing the classifier, make changes to the model and the training data to improve accuracy.

* Integration (1 Week)
1. Integrate the image classifier to the Django site.
2. Run the image classifier using the Django site to see if it functions properly.

* Fine-tuning (3 Weeks)
1. Perform multiple tests on the site and the classifier and check for bugs.
2. Start debugging the code.
3. Try different methods to improve speed and performance of the code.

# Anticipated Problems

* Data gathering (data gathered might not be sufficient)
* Data imbalance in the dataset.
* Overfitting and underfitting.
* Integration difficulties between Django and TensorFlow.