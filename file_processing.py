import os
import pickle
import numpy as np

def save_model(model, filename, directory="models"):
    os.makedirs(directory, exist_ok=True)  # Ensure the directory exists
    filepath = os.path.join(directory, filename)

    with open(filepath, "wb") as f:
        pickle.dump(model, f)
    print(f"Model saved successfully: {filename}")

def save_prediction(prediction, filename, directory="predictions"):
    os.makedirs(directory, exist_ok=True)  # Ensure the directory exists
    filepath = os.path.join(directory, filename)

    with open(filepath, "wb") as f:
        np.save(f, prediction)
    print(f"Prediction saved successfully: {filename}")


def load_model(filename, directory="models"):
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


def load_prediction(filename, directory="predictions"):
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