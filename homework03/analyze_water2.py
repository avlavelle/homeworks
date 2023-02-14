#!/usr/bin/env python3

#Anna Victoria Lavelle
#AVL578
#February 14, 2023

import requests
import math


#response = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')
#turb_data = response.json()


def calculate_turbidity(data: dict) -> int:
    """
    Calculates the average turbidity for the five most recent data points.

    Args: 
        data (dict): The data requested from the url as a dictionary.

    Returns: 
        average (int) : The calculated average turbidity.
    """

    entries = len(data["turbidity_data"])
    turb_sum = 0

    for x in range(5):
        a0 = data["turbidity_data"][entries-x-1]["calibration_constant"]
        I90 = data["turbidity_data"][entries-x-1]["detector_current"]
        T = a0*I90
        turb_sum = turb_sum + T

    average = turb_sum/5

    return average

def is_safe(turb: int) -> str:
    """
    Issues a statement on the safety of the water's turbidity.

    Args:
        turb (int): A value for turbidity.

    Returns:
        (str): Statement that indicates whether or not the turbidity is above or 
        below the safe threshold.
    """

    if (turb < 1):
        return "Info: Turbidity is below the threshold for safe use"
        
    if (turb >= 1):
        return "Warning: Turbidity is above the threshold for safe use"
        

def calculate_time(data: dict) -> int:
    """
    Calculates the timeit will take for the turbidity to return below the safe
    threshold. 

    Args:
        data (dict): The data requested from the url as a dictionary.


    Returns:
        b (int): The calculated number of hours that it will take for the turbidity to
        returb below the safe threshold.
    """

    #T0 = turb_data["turbidity_data"][len(turb_data["turbidity_data"])-1]["calibration_constant"]*turb_data["turbidity_data"][len(turb_data["turbidity_data"])-1]["detector_current"]
    T0 = calculate_turbidity(data)
    Ts = 1
    d = 0.02
    if (T0 < Ts):
        b = 0
        return b
    else:
        b = -math.log(T0, 1-d)
        return b



def main():
    response = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')
    turb_data = response.json()


    print("Average turbidity based on most recent five measurements = " + str(round(calculate_turbidity(turb_data), 4)) + " NTU")
    print(is_safe(calculate_turbidity(turb_data)))
    print("Minimum time required to return below a safe threshold = " + str(round(calculate_time(turb_data), 4)) + " hours")
    



if __name__ == '__main__':
    main()
