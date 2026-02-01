import yaml
from networksecurity.exception import NetworkSecurityException
import sys
from networksecurity.logging.logger import logging
import os 
import numpy as np
# import dill
import pickle

def read_yaml_file(file_path:str)->dict:
    """Reads a yaml file and returns the contents as a dictionary.

    Args:
        file_path (str): The path to the yaml file.
    """
    try:
        with open(file_path,'rb') as  yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e
    

def write_yaml_file(file_path:str,content:dict,replace:bool=False)->None:
    """Writes a dictionary to a yaml file.

    Args:
        file_path (str): The path to the yaml file.
        content (dict): The content to write to the yaml file.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'w') as yaml_file:
            yaml.dump(content,yaml_file)

    except Exception as e:
        raise NetworkSecurityException(e,sys) from e