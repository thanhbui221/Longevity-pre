# Longevity-pre

<p align="center">
  

  <h3 align="center">Longevity prediction</h3>

</p> 



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

It is a machine learning research that looks at lifespan factors to predict longevity. 
The data sets include older persons who have survived to be 90 years old and have maintained physical and social engagement. 
The data shown in the datasets is simulated, however it is based on genuine data. 
The data represent information about older persons aged 70 to 80 years for whom the class of active longevity 
(dependent parameter Longevity) in the future is known (whether they will reach the age of 90).

The datasets provide the following information (object attributes) about the elderly:
- Longevity - Classification of active longevity: 1 - a person can expect to live for up to 90 years; 0 - no Id - identifier for an elderly individual;
- Education - Education: 1 - superior; 2 - medium; 3 - insufficient;
- Gender - Sex;
- Age – Age
- Pet - An elderly person is caring for pets: the phone number is given;
- Children - the elderly person lives with children / grandkids / close relatives: the number of elderly people who live together is mentioned;
- Region refers to one's place of residence.
- Activity - The level of physical activity (number of steps per day) as measured by a particular application.
- MedExam - Attendance at the polyclinic (for the last year): coding of visits based on the completed medical card;
- Sport - Physical exercise: '+' an elderly person goes in for sports (walking, running, swimming); '-' is not engaged.

### Built With
- Jupyter notebook
- Pandas
- Scikit
- Flask
- Python



<!-- GETTING STARTED -->
## Getting Started

Demo: https://long-pre.herokuapp.com/


The data is first 'purified.' Then I'll be able to train the model and forecast the desired solution. 
There are more than 60 predictive modeling methods available. 
In order to reduce our options, I need to grasp the type of problem and the needs of the solution. 

First and foremost, we must acknowledge that ours is a classification and regression problem. We wish to define the connection between the output (Longevity) and other variables or functions (Sex, Age, Activity and others). Second, we employ supervised learning to train our model on a labeled dataset. 
We can reduce the number of models to the following using these two approaches (supervised learning and classification / regression):
- Logistic regression
- KNN or k-Nearest Neighbors
- Support Vector Machine
- Naive Bayesian Classifier
- Decision tree
- Random forest
- Persepton
- Artificial neural network
- Relevant vector method

After testing all the above models, the Decision Tree Model is the best option.

### Prerequisites


### Installation

## Usage


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

