#!/usr/bin/env python3

#Anna Victoria Lavelle
#April 5, 2023

from flask import Flask, request
import requests
import redis
import json
import os

app = Flask(__name__)


def get_redis_client():
    redis_ip = os.environ.get('REDIS_IP')
    if not redis_ip:
        raise Exception()
    red = redis.Redis(host=redis_ip, port=6379, db=0)
    return red

rd = get_redis_client()

#def get_data():
#    response = requests.get(url = 'https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
#    return response

#gdata = get_data()

@app.route('/data', methods = ['POST', 'GET', 'DELETE'])
def handle_data():
    """
    A route that posts the data, deletes the data, or outputs the data depending on 
    the user's query.

    Args:
        None.

    Returns:
        output_list (list): Returns the redis data.
    """
    if request.method == 'GET':
        output_list = []
        try:
            rd.keys()
        except KeyError:
            return ("No data available")
        for item in rd.keys():
            output_list.append(json.loads(rd.get(item)))
        return output_list
    elif request.method == 'POST':
        response = requests.get(url='https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
        for item in response.json()['response']['docs']:
            key = f'{item["hgnc_id"]}'
            rd.set(item.get('hgnc_id'),json.dumps(item))
        return f'Data loaded\n'
    elif request.method == 'DELETE':
        rd.flushdb()
        return f'Data deleted, there are {len(rd.keys())} keys in the db\n'
    else:
        return 'The method you tried does not work\n'

@app.route('/genes/<string:hgnc_id>', methods = ['GET'])
def get_gene(hgnc_id: str) -> dict:
    """
    A route that returns all data associated with a hgnc_id.

    Args:
        hgnc_id (str): The specified hgnc_id.

    Returns:
        items (dict): Dictionary with all data for the hgnc_id.
    """
    try:
        rd.keys()
    except KeyError:
        return ("No data available")
    items = json.loads(rd.get(hgnc_id))
    return items

@app.route('/genes', methods = ['GET'])
def get_genes() -> list:
    """
    A route that returns a json-formatted list of all hgnc_ids.

    Args:
        None.

    Returns:
        output (list): List of all hgnc_ids.
    """
    output = []
    try:
        rd.keys()
    except KeyError:
        return ("No data available")
    response = requests.get(url = 'https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
    response = response.json()['response']['docs']
    for item in response:
        output.append(item['hgnc_id'])
    return output












if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
