# Generating Meteorite Sites and Investigating Them

This project is compiled of two scripts, generate\_sites.py and calculate\_trip.py. 
They allow for the random creation of five meteorite sites, allow for that information to be written into a JSON file, and for the data to be read from that JSON file and used in calculations. 

This is important because if we were operating a robotic vehicle on Mars, we could calculate the time it would take us to travel to different locations and to collect samples.

## Installation and Running the Code

Install this project by cloning the repository. Each script using a shebang, so the scripts should be executable after using the Linux command chmod. Then, the scripts can be called with a standalone executable. 


```bash
git clone ...
chmod u+x ...
...
```

## Code Descriptions

#### generate\_sites.py

This script randomly generates five different Mars landing sites. Each site includes an ID, a latitude, a longitude, and a composition. This data is compiled into a dictionary with the key, "sites", whose value is a list of dictionaries. The data is then written into a JSON file.

#### calculate\_trip.py

This script reads the data from the JSON file created in generate\_sites.py and calculates trip information for the robotic vehicle at a speed of 10 km per hour. The script prints the time to travel and the time to sample, along with the corresponding trip leg number. At the end, the script prints a summary of the entire trip, including the total number of legs and the total time elapsed.

## Interpreting Results 

For our randomly generated meteorite sites from generate\_sites.py, calculate\_trip.py calculates that the longest leg of the trip takes 12.22 hrs while the shortest leg only takes 0.47 hrs. After the five legs of the trip, 30.62 hrs have elapsed for the robot.
