#!/usr/bin/env python3

#Anna Victoria Lavelle
#AVL578
#February 21, 2023

from flask import Flask, request
import requests
import xmltodict
import math

app = Flask(__name__)

def get_data() -> dict:
    """
    Loads in the data from the ISS Trajectory Data website and puts it into a 
    dictionary.

    Args:
        None.

    Returns:
        data (dict): ISS Trajectory Data in a dictionary.
    """

    response = requests.get(url = 'https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
    data = xmltodict.parse(response.text)
    return data

@app.route('/', methods = ['GET'])
def all_data() -> list:
    """
    A route that allows users to return the entire data set from the ISS Trajectory
    Data.

    Args:
        None.

    Returns:
        epochs (list): List of the entire data set.
    """

    data = get_data()
    epochs = data['ndm']['oem']['body']['segment']['data']['stateVector']
    return epochs

@app.route('/epochs', methods = ['GET'])
def get_epochs() -> list:
    """
    A route that allows users to return a list of all of the Epochs in the data set.

    Args:
        None.

    Returns:
        sol (list): List of all of the Epochs in the data set.
    """

    data = get_data()
    epochs = data['ndm']['oem']['body']['segment']['data']['stateVector']
    sol = []
    for epoch in epochs:
        sol.append(epoch['EPOCH'])
    return sol

@app.route('/epochs/<int:epoch>', methods = ['GET'])
def get_vector(epoch: int) -> dict:
    """
    A route that allows the users to return the state vectors for a specific Epoch
    in the data set.

    Args:
        epoch (int): The specified Epoch.

    Returns:
        (dict): Dictionary with the state vectors for the specified Epoch.
    """

    data = get_data()
    epochs = data['ndm']['oem']['body']['segment']['data']['stateVector']
    return epochs[epoch]

@app.route('/epochs/<int:epoch>/speed', methods = ['GET'])
def get_speed(epoch: int) -> dict:
    """
    A route that allows the users to return the instantaneous speed for a specific 
    Epoch.

    Args:
        epoch (int): The specificed Epoch.

    Returns:
        speed (dict): Dictionary with the instantaneous speed of the Epoch.
    """

    data = get_data()
    epochs = data['ndm']['oem']['body']['segment']['data']['stateVector']
    xdot = float(epochs[epoch]['X_DOT']['#text'])
    ydot = float(epochs[epoch]['Y_DOT']['#text'])
    zdot = float(epochs[epoch]['Z_DOT']['#text'])
    speed = math.sqrt(xdot**2+ydot**2+zdot**2)
    return {'speed': str(speed) + ' km/s'}

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')


