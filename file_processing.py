import os
import pickle
import numpy as np

# Saves model to a pickle file
def save_model(model, filename, directory="models"):
    """
    Saves the trained model as a pickle file.
    
    Args:
        model: The model to be saved (e.g., a trained neural network).
        filename (str): The name of the file to save the model as (should include file extension).
        directory (str): The directory to store the saved model (default is "models").
    
    Returns:
        None
    """
    os.makedirs(directory, exist_ok=True)  # Ensure the directory exists
    filepath = os.path.join(directory, filename)

    with open(filepath, "wb") as f:
        pickle.dump(model, f)
    print(f"Model saved successfully: {filename}")

# Saves predictions to a numpy file
def save_prediction(prediction, filename, directory="predictions"):
    """
    Saves the predictions as a .npy file.
    
    Args:
        prediction: The prediction data (typically a NumPy array).
        filename (str): The name of the file to save the prediction as (should include file extension).
        directory (str): The directory to store the saved prediction (default is "predictions").
    
    Returns:
        None
    """
    os.makedirs(directory, exist_ok=True)  # Ensure the directory exists
    filepath = os.path.join(directory, filename)

    with open(filepath, "wb") as f:
        np.save(f, prediction)
    print(f"Prediction saved successfully: {filename}")

# Loads model from a pickle file
def load_model(filename, directory="models"):
    """
    Loads a model from a pickle file.
    
    Args:
        filename (str): The name of the model file to load.
        directory (str): The directory where the model is stored (default is "models").
    
    Returns:
        model: The loaded model object.
    
    Raises:
        FileNotFoundError: If the model file is not found in the specified directory.
        ValueError: If the file is not a valid pickle file.
    """
    filepath = os.path.join(directory, filename)
    try:
        with open(filepath, "rb") as f:
            model = pickle.load(f)
        print(f"Model loaded successfully: {filename}")
        return model
    except FileNotFoundError:
        raise FileNotFoundError(f"Model file not found: {filename}")
    except pickle.UnpicklingError:
        raise ValueError(f"File {filename} could not be loaded as a model. Check if it is a valid pickle file.")

# Loads predictions from a numpy file
def load_prediction(filename, directory="predictions"):
    """
    Loads a prediction from a .npy file.
    
    Args:
        filename (str): The name of the prediction file to load.
        directory (str): The directory where the prediction is stored (default is "predictions").
    
    Returns:
        prediction: The loaded prediction data (typically a NumPy array).
    
    Raises:
        FileNotFoundError: If the prediction file is not found in the specified directory.
        ValueError: If the file is not a valid .npy file.
    """
    filepath = os.path.join(directory, filename)
    try:
        with open(filepath, "rb") as f:
            prediction = np.load(f)
        print(f"Prediction loaded successfully: {filename}")
        return prediction
    except FileNotFoundError:
        raise FileNotFoundError(f"Prediction file not found: {filename}")
    except ValueError:
        raise ValueError(f"File {filename} could not be loaded as a prediction. Check if it is a valid .npy file.")