import pickle
import numpy as np

def pickle_load(filename):
    """
    Loads the pickled file and returns a model ready to use

    Parameters
    ----------
    filename : path to pickled model

    Returns
    -------
    a_object : a model
    """
    with open(filename, 'rb') as inputfile:
        a_object = pickle.load(inputfile, encoding='bytes')

    return a_object

def transformations(input_data):
    """
    Transforms user-input, ready to make prediction

    Parameters
    ----------
    input_data : an array of user-input values

    Returns
    -------
    processed : A dataframe object
    """
    weighted_ratio = np.sqrt(input_data[1]**2/input_data[0])
    rated = input_data[4]
    age = 2020 - input_data[2]
    track_no = input_data[3]
    
    processed = pd.DataFrame({'weighted_ratio':[weighted_ratio],
              'rated':[rated],
              'age':[age],
              'track_no':[track_no]
            })
    return processed


