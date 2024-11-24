
# ImageClassificationCIFAR-10
In this project, the goal is to classify images from the CIFAR-10 dataset into 10 distinct object categories using various AI models. We focus on preprocessing the dataset, building AI models, and evaluating their performance using standard metrics.

### Team members:
   - Dominique Isbister, 40210056
   - Mohamed Mahmoud, 40283160
   - Kenny Luo-Li, 40237402

---

This format is clear and well-structured, perfect for a `README.md`. Let me know if you need further adjustments!
## Table of Contents
1. [Prerequisites](#prerequisites)
2. [File descriptions](#file-descriptions)
3. [Setup](#setup)
4. [Running the code](#running-the-code)
---

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/downloads/) (version 3.9 or higher)
- [pip](https://pip.pypa.io/en/stable/installation/) 
- [git](https://git-scm.com/)

---

## Setup

### Step 1: Clone the Repository with SSH

```bash
git clone git@github.com:Dom-Isbis/ImageClassificationCIFAR-10.git
cd your-repository
```
or normally

```bash
git clone https://github.com/Dom-Isbis/ImageClassificationCIFAR-10.git
cd your-repository
```
### Step 2: Create a Virtual Environment

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

#### Virtual Environment Setup

First, ensure the virtual environment is activated:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`


After activating the virtual environment, install the required dependencies:

```bash
pip install -r requirements.txt
```
---

## File descriptions

This section explains the purpose of the main files and folders in the repository:

```plaintext
ImageClassificationCIFAR-10/
├── _pycache_/                                          # Folder containing compiled bytecode
├── data/                                               # Folder for CIFAR-10 dataset (Please ensure that you install it locally by following the project instruction guidelines from the official Final Project PDF)
├── models/                                             # Contains saved models 
│   ├── cnn_vgg11.pkl        
│   ├── dt_scratch_25.pkl    
│   ├── ...               
├── predictions/                                        # Contains saved predictions
│   ├── y_predictions_cnn_vgg11.npy        
│   ├── y_predictions_dt_scratch_25.npy    
│   ├── ...  
├── COMP472_CIFAR_10_Image_Classification.ipynb         # Main jupyter notebook to train and evaluate all models
├── file_processing.py                                  # Contains helper functions for I/O file processing such as Save/Load functions
├── requirements.txt                                    # List of dependencies for the project
├── README.md                                           # Documentation for the project
├── .gitattributes                                      # Version control configs
├── .gitignore                                          # Version control configs
```

### Detailed Descriptions

- **`data/`**: 
  - This folder is automatically created when downloading the CIFAR-10 dataset. It contains the training and test datasets.
  
- **`models/`**: 
  - Contains Python scripts implementing the AI models:
    - `naive_bayes.py`: Builds a Gaussian Naive Bayes model for CIFAR-10 image classification.
    - `decision_tree.py`: Implements a decision tree classifier to distinguish between CIFAR-10 classes.
    - `mlp.py`: Implements a Multi-Layer Perceptron (MLP), a simple feed-forward neural network.
    - `cnn.py`: Implements a Convolutional Neural Network (CNN) for advanced image classification tasks.

- **`results/`**: 
  - Stores outputs from the model evaluations, such as:
    - Accuracy reports
    - Confusion matrices
    - Training logs

- **`main.py`**: 
  - The primary script that integrates dataset preprocessing, model training, evaluation, and metric visualization.

- **`requirements.txt`**: 
  - Lists the Python libraries and versions needed to run the project.

- **`README.md`**: 
  - The file you're reading now, explaining the project structure and usage.

---
---
## Running the code

Second, ensure that a valid kernel is selected to run the jupyter notebook (ipynb)

##### To run previously saved models/predictions, execute the code snippets under the following sections, in order:
  1. Imports & Configs (all cells)
  2. Dataset Overview (all cells)
  3. Helper Functions (all cells)
  4. Naive Bayes, Decision Tree, Multi-Layer Perceptron, CNN - VGG11 (First cell of each section only)
  5. Analysis Report (all cells)

##### To run and save new predictions, please execute all code snippets from top to bottom sequentially
