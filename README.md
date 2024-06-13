
# AI-Powered Hotel Ranking: Streamlining Your Booking Experience

## Project Description
Expedia Group, a prominent online travel agency, streamlines trip planning by providing a platform where users can compare prices, review amenities, and book accommodations through sophisticated recommendation and ranking systems. This project evaluates various machine learning models to efficiently prioritize the most relevant search results, enhancing user satisfaction and booking efficiency.

## Table of Contents
1. [Problem Statement](#problem-statement)
2. [Project Goal](#project-goal)
3. [Dataset Description](#dataset-description)
4. [Approach and Methodology](#approach-and-methodology)
   - [Machine Learning Models](#machine-learning-models)
   - [Deep Learning Models](#deep-learning-models)
5. [Results](#results)
6. [Future Work](#future-work)
7. [Acknowledgments](#acknowledgments)
8. [Team Members](#team-members)
9. [Blog Post](#blog-post)

## Problem Statement
When searching for accommodations, users face an overwhelming number of choices. For example, searching for a "4-star hotel for three adults in Geneva in early May 2024" can yield hundreds of results. Without sorting options based on user-specified features like star rating or number of guests, search times can extend, and bookings can decrease, countering the platform’s objective to simplify travel arrangements.

## Project Goal
The goal of this project is to develop and evaluate supervised machine learning and deep learning models that can rank hotel search results by relevance, thereby improving user satisfaction and booking rates.

## Dataset Description
The Expedia RecTour research dataset used in this project includes 1 million searches over two months in 2021. It contains detailed information on booking details, hotel ratings, review counts, and amenities such as WiFi and parking. We focused on searches that led to clicks or bookings for the top 500 destinations, which helped us significantly reduce the training dataset size.

## Approach and Methodology
To address the ranking challenge, we employed various machine learning and deep learning models, evaluated using the Normalized Discounted Cumulative Gain (NDCG) metric, which prioritizes user satisfaction by rewarding models that place the most relevant properties higher.

## Machine learning libraries used
- __ XGBoost
- __ LightGBM
- __ allRank

### Machine Learning Models
We began with decision tree-based models such as LightGBM and XGBRanker. These models helped us identify key features relevant to the ranking task.

### Deep Learning Models
We then explored the allRank model, an open-source transformer-based model that enhances ranking by understanding the context of other properties. This model demonstrated the best performance on the Expedia RecTour dataset, leveraging a self-attention mechanism to learn item scores in the context of all other items present in the list.

## Results
Our evaluation showed the following:
- **Decision Tree-based Models:** These models effectively identified key features for the ranking task but did not achieve the highest NDCG scores.
- **AllRank Model:** This model performed best in our tests, though it did not yet match the NDCG score of the previously used model.

The results are summarized as follows:
- **NDCG Scores:** The allRank model showed superior performance in placing the most relevant properties higher in the search results.

## Future Work
We have outlined several future steps to enhance our model:
- **Larger Dataset Training:** Expanding the dataset size for training to improve model generalization.
- **Ranking Similarity Comparison:** Comparing the ranking outputs of different models to understand performance variations.
- **Feature Engineering:** Implementing various relevance metrics aligned with business objectives to improve model accuracy further.


#### **Contributing Members**

- __[Guillem Montoya](https://www.linkedin.com/in/guillem-montoya-bb0284195/)__
- __[Kunal Sharma](https://www.linkedin.com/in/drkunalsharma/)__
- __[Lorenz Schmid](https://www.linkedin.com/in/lorenz-schmid-40801b22b/)__
- __[Asterios Raptis](https://www.linkedin.com/in/asterios-raptis-46824a31/)__

## Blog Post
For more details, please read our [blog post](https://academy.constructor.org/blog/data-science-capstone-projects-batch-25).

Thank you for reading! For more details, please refer to the project documentation and additional resources included in this repository.


Day 0, 8th of April
======================
Folder Structure, initial setup

## Partners
- __ Expedia Group
- __ Constructor Academy















## Create GitLab folder structure

## Data Exploration, 


### 1. Clone project repo to your desired destination

### 2. Navigate to a project repo and create a .gitignore file (see instructions below), push your changes to remote    


### 3. Make an environment with conda
 
`conda create --name myenv`

Change the environment\:

`conda env list`\
`conda activate myenv`\
`conda list`

### 4. Save an environment as .yml to be able to transfer it to the other person

Export your active environment to a new file (in the end of the project or once you need to share it with other person):

`conda env export > environment.yml`

Create the environment from the environment.yml file:

`conda env create -f environment.yml`

Remove environment if needed:

`conda remove --name myenv --all`


### 5. Folder structure

`pip install cookiecutter`\
`cookiecutter https://github.com/drivendata/cookiecutter-data-science`

Clean the folder structure (remove unnecessary files).   
Or create your own custom one. 

### 6. Git

#### 6.1 Gitignore 

Create `.gitignore` file for the following keywords: `python`, `jupyter`, `data` and whatever is required.    
`https://www.toptal.com/developers/gitignore`  

Add *.csv, *.json, etc. 

#### 6.2 push to the gitlab before you add any data to your folder.

`Git add .`\
`Git commit -m ”added folder structure”`\
`Git push `

#### 6.3 push info about data

Create separate txt file with the description where to get this data. Put the file into the `Data` folder.  
If the data are very light  ~5 mb or so, you can push it, Otherwise just description. 

#### 6.4 branching 

`Git branch vis`\
`Git checkout vis `

Work on `vis`, if you like the result => then merge \
Merging is happening on the target branch (master)\
Delete the branch after completing the task.

`git branch -d <branch-name>` \
`git push --delete <remote name> <branch name>` 

`<remote name>` == origin


**Do not work on the same file at the same time.**

If you work on the same branch - always pull first. 

Actually, always start with a PULL. \
This reduce a chance to get a conflict. Work ideally on different files. If working on the same file - always PULL first. 

#### 7. Example Student Projects  


- Brain MRI: https://github.com/SIT-Academy/brain-mri-classification/blob/master/README.md

- Super Resolution Satellite: 
https://github.com/SIT-Academy/satellite-image-super-resolution/tree/master/notebooks (SIT version)  
https://github.com/egronskaya/Super-Resolution-for-Satellite-Imagery (Students' version)

Both projects were done in Colab. 




