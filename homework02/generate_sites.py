#!/usr/bin/env python3

#Anna Victoria Lavelle
#AVL578
#January 29,2023

import random
import json

def choose_site() -> str:
    """
    Chooses a random meteorite composition for a landing site.

    Args:
        None
    
    Returns:
        result(str): String of one meteorite composition.
    """
    compositions = ["stony", "iron", "stony-iron"]
    site_type = compositions[random.randrange(3)]
    return site_type

def create_entry(entry_num: int) -> dict:
    """
    Creates a dictionary with site_id, latitude, longitude, and composition as keys. 
    Returns this dictionary.

    Args:
        entry_num (int): Entry number as an integer.

    Returns:
        entry_dict (dict): Dictionary with the site_id, latitude, and composition keys        
        and their assigned values.
    """
    entry_dict = {}
    entry_dict["site_id"] = entry_num
    entry_dict["latitude"] = random.uniform(16.0, 18.0)
    entry_dict["longitude"] = random.uniform(82.0, 84.0)
    entry_dict["composition"] = choose_site()
    return entry_dict


def main():
    meteorite_list = []
    meteorite_info = {}

    for x in range(5):
        meteorite_list.append(create_entry(x+1))

    meteorite_info["sites"] = meteorite_list
    print(meteorite_info)

    with open('meteorite_sites.json', 'w') as out:
        json.dump(meteorite_info, out, indent = 2)

if __name__ == '__main__':
    main()
