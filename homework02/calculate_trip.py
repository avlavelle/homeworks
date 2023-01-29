#!/usr/bin/env python3

#Anna Victoria Lavelle
#AVL578
#January 29, 2023

import json
import math

with open('meteorite_sites.json', 'r') as f:
    met_data = json.load(f)
    
mars_radius = 3389.5    # km

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    """
    Given the latitude and longitude of points 1 and 2, returns the distance using the 
    great-circle distance algorithm.

    Args:
        latitude_1 (float): Latitude of point 1 in decimal notation.
        longitude_1 (float): Longitude of point 1 in decimal notation.
        latitude_2 (float): Latitude of point 2 in decimal notation.
        longitude_2 (float): Longitude of point 2 in decimal notation.

    Returns:
        distance (float): Distance between points in decimal notation.
    """
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

def calc_time(leg_number: int) -> float:
    """
    Given the leg number, returns the time it takes to cover the distance of that leg's trip.

    Args: 
        leg_number (int) : The trip leg number. 

    Returns:
        time (float) : The time it takes to cover the distance of that leg's trip.
    """
    if (leg_number == 1):
        distance = calc_gcd(16.0, 82.0, met_data["sites"][0]["latitude"], met_data["sites"][0]["longitude"])
    if (leg_number != 1):
        distance = calc_gcd(met_data["sites"][leg_number-2]["latitude"], met_data["sites"][leg_number-2]["longitude"], met_data["sites"][leg_number-1]["latitude"], met_data["sites"][leg_number-1]["longitude"])
    time = distance/10.0;
    return time;

def calc_sample_time(leg_number: int) -> int:
    """
    Given the leg number, returns the time it takes to collect the sample on the final 
    meteorite of that leg.

    Args:
        leg_number (int) : The trip leg number. 

    Returns:
        sample_time (int) : The time it takes to collect the sample on the final meteorite of
        that leg.
    """
    sample_type = met_data["sites"][leg_number-1]["composition"]
    if (sample_type == "stony"):
        sample_time = 1
    elif (sample_type == "iron"):
        sample_time = 2
    elif (sample_type == "stony-iron"):
        sample_time = 3
    return sample_time
 
def main():
    total_time = 0

    for x in range(len(met_data["sites"])):
        print("leg = "+ str(x+1) + ",", end = " ")
        print("time to travel = " + str(round(calc_time(x+1), 2)) + " hr,", end = " ")
        total_time += calc_time(x+1)
        print("time to sample = " + str(round(calc_sample_time(x+1),2)) + " hr")
        total_time += calc_sample_time(x+1)

    print("=======================================================================")
    print("number of legs = " + str(len(met_data["sites"])) +",", end = " ")
    print("total time elapsed = " + str(round(total_time,2)) + " hr")

if __name__ == '__main__':
    main()
