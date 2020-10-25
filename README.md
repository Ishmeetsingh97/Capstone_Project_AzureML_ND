# Capstone Project - Azure Machine Learning Engineer ND Program

## Overview
This project demostatrates the utilization of two different Microsoft's Machine
Learning tools namely AutoML and Hyperdrive. Two different models have been created
using these tools and the performance of these two models are compared. The best
performing model is then deployed on the Azure Platform and then requested via
a JSON payload.
* **
### Overview of the Dataset
The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. The Dataset includes three iris species with 50 samples each as well as some properties about each flower. One flower species is linearly separable from the other two, but the other two are not linearly separable from each other. <br />
**Predicted attribute: class of iris plant.**
* **
### Method used to get data into Azure ML Studio
First, I explored the UCI machine learning repository to get a Dataset to train
the models on. Once I decided to work with iris dataset, I found the link to download the data. The link was then passed to the `from_delimited_files` method from the Tabular class object from the Dataset class object.
* **
### AutoML parameters and Configurations
The AutoML run has the following parameters :
* *task*: What kind of Machine Learning task has the AutoML has to perform. For example, Classification, Regression etc. In this project, it is a `Classification` problem where the iris_class will be Predicted.

* *primary_metric*: This is the metrics which is optimised during the training of the model algorithm. For example, Accuracy, Area Under Curve(AUC) etc. In this project, `Accuracy` is used as an success metrics.

* *experiment_timeout_minutes*: This is the max time for which the AutoML can use different models to train on the dataset. In this project, the max timeout in minutes is `15`.

* *training_data*: This is the training data on which all the different models are trained on. In this project, it is `80%` of the iris dataset.

* *label_column_name*: This is the variable which is predicted by the model. In this project, it is the `iris class`.

* *n_cross_validations*: This is the n in cross validation process. Cross validation is the process where different data points are put into training and testing dataset (resampling) to ensure that the model does not overfit over certain values. In this project the n is `5`.

**Rubric Point: The submission contains a screenshot of the RunDetails widget that shows the progress of the training runs of the different experiments.**
![alt text](https://github.com/Ishmeetsingh97/Capstone_Project_AzureML_ND/blob/master/screenshots/required_screenshot_1.png)


**Rubric Point: The submitted notebook contains code showing the best model being registered and includes a screenshot of the best model with its run id.**
![alt text](https://github.com/Ishmeetsingh97/Capstone_Project_AzureML_ND/blob/master/screenshots/required_screenshot_2.png)

* **
### Hyperdrive parameters and Configurations
The Hyperdrive run has the following parameters :
* *primary_metric_name*: This is the metrics which is optimised during the training of the model algorithm. For example, Accuracy, Area Under Curve(AUC) etc. In this project, `Accuracy` is used as an success metrics.

* *primary_metric_goal*: This is the parameter which tells Hyperdrive how to optimise the algorithm using the primary_metric_name given. The goal can be anything from Maximize to Minimise the primary_metric_name. In this project, it is `PrimaryMetricGoal.MAXIMIZE`.

* *max_total_runs*: This is the maximum number of runs which Hyperdrive will run using different hyperparameters. In this project, the max_total_runs is `48`.

* *max_concurrent_runs*: This is the maximum number of run which run concurrently over different threads. In this project, the max_concurrent_runs is `8`.

* *hyperparameter_sampling*: This is the Parameter Sampler which specfies the techniques in which the hyperparameters are tuned. In this project, RandomParameterSampling was used to tune the hyperparameter "--C" with `uniform(0.1, 0.9)` and "--max_iter" with `choice(10, 50, 100)`.

* *policy*: This is the early stopping policy used by Hyperdrive which is used to provide guidance as to how many iterations can be run before the model begins to overfit. In this project, BanditPolicy was used with argument evaluation_interval of `3` and slack_factor of `0.1`. BanditPolciy terminates any run whos primary metrics is less than the slack factor of best run.

* *estimator*: This has the sampled hyperparameters data. In this project, A `SKLearn` estimator is used.

**Rubric Point: The submission contains a screenshot of the RunDetails widget that shows the progress of the training runs of the different experiments.**
![alt text](https://github.com/Ishmeetsingh97/Capstone_Project_AzureML_ND/blob/master/screenshots/required_screenshot_3.png)


**Rubric Point: The submission includes a screenshot of the best model with its run id and the different hyperparameters that were tuned. The submitted notebook also contains code showing the best model being registered.**
![alt text](https://github.com/Ishmeetsingh97/Capstone_Project_AzureML_ND/blob/master/screenshots/required_screenshot_4.png)
![alt text](https://github.com/Ishmeetsingh97/Capstone_Project_AzureML_ND/blob/master/screenshots/required_screenshot_5.png)


* **

###  Comparison of the Two Models
 The AutoML generated `38` models among with the `PreFittedSoftVotingClassifier` performed the best with `0.9750` Accuracy. On the other hand, The Hyperdrive generated `48` iterations with the Logistic Regression Model with different hyperparameter tuning of C and max_iter parameters and achieved an Accuracy of `1` (perfect 100%) with C as `0.486374154783502` and max iter as `50` . Therefore the Hyperdrive Model has been deployed.

 * **
### Overview of acccessing the Deployed Model
To access the deployed endpoint we need 4 files, their purpose is explained below :

* *swagger.json*: This is the file is to be downloaded from `Swagger URI` placeholder from the deployment page of the specfic deployment in the Azure ML Studio. This is the file which contains all the specifications of the API for the Swagger to run. Screenshot attached for reference.

[!alt text] (required_screenshot_4.png)

* *config.json*: This file is to be downloaded from Azure ML Studio by clicking on the upper right corner on the `` icon. This is the file which contains the credentails which allow the user to authenticate to the Azure ML Studio. Screenshot attached for reference.

[!alt text] (required_screenshot_4.png)

* *serve.py* (Taken from Udacity's Starter code for the Operationalizing Machine Learning project which I have completed earlier): This script basically exposes the swagger.json file which over the localhost server.

* *Endpoint.py* (Taken from Udacity's Starter code for the Operationalizing Machine Learning project which I have completed earlier):
This script basically helps to send a HTTP Post request to the generated endpoint.

* *swagger.sh* (Taken from Udacity's Starter code for the Operationalizing Machine Learning project which I have completed earlier):
This file basically helps to run swagger in docker container on the local machine.

**Rubric Point: The submission contains a screenshot showing the model endpoint as Healthy.**
![alt text](https://github.com/Ishmeetsingh97/Capstone_Project_AzureML_ND/blob/master/screenshots/required_screenshot_6.png)


### Model Improvement
As the model has peaked it performance by making the Accuracy as 1. There are these things we can try to make it even more better:
* Try different metrics to evalute performance such as Precision, Recall and the Area Under Curve (AUC) etc.


* We can tweak the Parameter Sampler to choose different Regularization strength and Max Iteration to reach the current results (Accuracy = 1) even more faster.
