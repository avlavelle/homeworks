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

gdata = get_data()

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

    try:
        epochs = gdata['ndm']['oem']['body']['segment']['data']['stateVector']
    except KeyError:
        return ("No data available")

    return epochs

@app.route('/epochs', methods = ['GET'])
def get_epochs() -> list:
    """
    A route that allows users to return a list of all of the Epochs in the data set.
    Offset and limit parameters can be used to return a specific list of Epochs.

    Args:
        offset (int): Results are offset by this integer.
        limit (int): Maximum number of results returned.

    Returns:
        sol (list): List of all of the Epochs in the data set.
    """

    
    offset = request.args.get('offset', 0)
    limit = request.args.get('limit', len(all_data()))
    if offset:
        try:
            offset = int(offset)
        except ValueError:
            return ("Enter a positive integer for offset.", 400)
    if limit:
        try:
            limit = int(limit)
        except ValueError:
            return ("Enter a positive integer for limit.", 400)
    try:
        epochs = gdata['ndm']['oem']['body']['segment']['data']['stateVector']
    except KeyError:
        return ("No data available")

    sol = []
    counter = 0
    for epoch in epochs:
        if counter == limit:
            break
        if epochs.index(epoch) >= (offset):
            sol.append(epoch['EPOCH'])
            counter = counter + 1

    return sol

@app.route('/epochs/<string:epoch>', methods = ['GET'])
def get_vector(epoch: str) -> dict:
    """
    A route that allows the users to return the state vectors for a specific Epoch
    in the data set.

    Args:
        epoch (str): The specified Epoch.

    Returns:
        item (dict): Dictionary with the state vectors for the specified Epoch.
    """

    try:
        epochs = gdata['ndm']['oem']['body']['segment']['data']['stateVector']
    except KeyError:
        return ("No data available")

    for item in epochs:
        if item['EPOCH'] == epoch:
            return item


@app.route('/epochs/<string:epoch>/speed', methods = ['GET'])
def get_speed(epoch: str) -> dict:
    """
    A route that allows the users to return the instantaneous speed for a specific 
    Epoch.

    Args:
        epoch (str): The specificed Epoch.

    Returns:
        speed (dict): Dictionary with the instantaneous speed of the Epoch.
    """

    try:
        epochs = gdata['ndm']['oem']['body']['segment']['data']['stateVector']
    except KeyError:
        return ("No data available")
    for item in epochs:
        if item['EPOCH'] == epoch:
            xdot = float(item['X_DOT']['#text'])
            ydot = float(item['Y_DOT']['#text'])
            zdot = float(item['Z_DOT']['#text'])

    speed = math.sqrt(xdot**2+ydot**2+zdot**2)
    return {'speed': str(speed) + ' km/s'}

@app.route('/help', methods = ['GET'])
def get_help() -> str:
    """
    A route that provides help text for the user that describes each route.

    Args:
        None

    Returns:
        help (str): Help text for the user.
    """

    intro = "\nThese are the routes for iss_tracker.py.\n"
    
    head1 = "\nreturn elements from the data set\n"
    head2 = "\nedit or update the data set\n"
    head3 = "\nto receive help\n"
    one ="   / (GET)                                Return entire data set\n"
    two ="   /epochs (GET)                          Return list of all Epochs in the data set\n"
    thr ="   /epochs?limit=int&offset=int (GET)     Return modified list of Epochs given query parameters\n"
    fou ="   /epochs/<epoch> (GET)                  Return state vectors for a specific Epoch from the data set\n"
    fiv ="   /epochs/<epoch>/speed (GET)            Return instantaneous speed for a specific Epoch in the data set\n"
    six ="   /delete-data (DELETE)                  Delete all data from the dictionary object\n"
    sev ="   /post-data (POST)                      Reload the dictionary object with data from the web\n"
    eig ="   /help (GET)                            Return help text for the user\n\n"
    return intro + head1 + one + two + thr + fou + fiv + head2 + six + sev + head3 + eig

@app.route('/delete-data', methods = ['DELETE'])
def delete_data() -> str:
    """
    A route that deletes all data from the dictionary object.

    Args:
        None

    Returns:
        (str): Statement about state of data.
    """
    global gdata
    gdata.clear()
    return ("Data has been deleted")

@app.route('/post-data', methods = ['POST'])
def post_data() -> str:
    """
    A route that reloads the dictionary object with data from the web.

    Args:
        None

    Returns:
        (str): Statement about state of data.
    """

    global gdata
    gdata = get_data()
    return ("Data has been restored")


if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')


