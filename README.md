
# ImageClassificationCIFAR-10
In this project, the goal is to classify images from the CIFAR-10 dataset into 10 distinct object categories using various AI models. We focus on preprocessing the dataset, building AI models, and evaluating their performance using standard metrics.

### Team members:
   - Dominique Isbister, 40210056
   - Mohamed Mahmoud, 40283160
   - Kenny Luo-Li, 40237402

---

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
├── data/                                               # Folder for CIFAR-10 dataset (Please install it locally by following the project guidelines)
├── models/                                             # Contains saved models 
│   ├── cnn_vgg11.pkl        
│   ├── dt_scratch_25.pkl    
│   ├── ...               
├── predictions/                                        # Contains saved predictions
│   ├── y_predictions_cnn_vgg11.npy        
│   ├── y_predictions_dt_scratch_25.npy    
│   ├── ...  
├── COMP472_CIFAR_10_Image_Classification.ipynb         # Main jupyter notebook to process data, train and evaluate all models, and show confusion matrices and classfication reports
├── file_processing.py                                  # Contains helper functions for I/O file processing such as Save/Load functions
├── requirements.txt                                    # List of dependencies for the project
├── README.md                                           # Documentation for the project
├── .gitattributes                                      # Version control configs
├── .gitignore                                          # Version control configs
```
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
