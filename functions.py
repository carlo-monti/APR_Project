import random
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def filename_to_annotation_list(filename, as_dictionary = False):
    '''
    This function parses the filename and returns all the annotations as a list.
    If get_column_names is True it will return the names of the columns.
    '''
    parsed_info = []
    column_names = []
    if filename.endswith(".mp3"):
        column_names =  ["Date_time",
                        "Intensity",
                        "Temperature",
                        "Humidity",
                        "Pressure",
                        "Wind_speed",
                        "Video",
                        "Duration",
                        "Surface",
                        ]
        parsed_info = filename[:-4].split("_")
        if len(parsed_info) == 10:
            # some files have 10 columns. It can be either:
            # - Because we are dealing with split audio (./audio/split/....)
            # - An error in the dataset (./audio)
            if parsed_info[9].find("segment") != -1:
                column_names.append("Segment")
            else:
                parsed_info.pop(7)
    if as_dictionary:
        dictionary = dict(zip(column_names, parsed_info))
        return dictionary
    else:
        return parsed_info
    
def extract_feature(filename, feature_type=3, as_dictionary=True):
    '''
    This function extract the selected feature of the filename
    It will return a list
    '''
    features = []
    # Get features

    features.append(random.random())
    features.append(random.random())
    if as_dictionary:
        return {"cadsa": [43,33],"dsfa": 50}
    else:
        return features

def build_df(folder,feature_type):
    '''
    This function will build the whole dataframe by extracting features from all the files on the folder
    It will return a pandas dataframe
    '''

    audio_files = os.listdir(folder)
    list_of_dict = []

    for filename in audio_files:
        # Get file annotations
        annotations = filename_to_annotation_list(filename,as_dictionary=True)
        features = extract_feature(filename,feature_type,as_dictionary=True)
        annotations.update(features)
        list_of_dict.append(annotations)

    df = pd.DataFrame().from_dict(list_of_dict)
    return df






