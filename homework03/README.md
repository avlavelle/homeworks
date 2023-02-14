# Analyzing Water Quality and Issuing Statements about its Safety

This project is compiled of one script, analyze\_water2.py, and its tester script, test\_analyze\_water1.py. The script reads in water quality data, calculates the current turbidity as the average of the five most recent data points, issues a statement about the safety of the water, and calculates the time it will take for the water to become safe. 

This is important because it quickly determines if the water quality is safe, so our Mars samples can be analyzed. If the water is not safe, it can provide a time estimate for when the water will be safe again.

## Installation and Running the Code

Install this project by cloning the repository. Each script uses a shebang, so the scripts should be executable after using the Linux command chmod. Then, the scripts can be called with a standalone executable. The tester script can also be called with the pytest executable.

```bash
git clone ...
chmod u+x ...
...
```
The script also pulls the water quality data from this link: https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity\_data.json . This data is a JSON dictionary with one key, "turbidity\_data", whose value is a time series list of dictionaries. The script uses the Python3 requests library to import the JSON data.

## Code Description 

#### analyze\_water2.py

This script uses the requests library to import the JSON data. Then, it uses keys in the dictionary to find the needed values to calculate turbidity as the average of the five most recent data points. After calculating the turbidity, the script issues a statement regarding the water quality and calculates the time it will take for the water to return to a safe turbidity level if it is currently unsafe. 

## Interpreting Results

Some sample output might be:

```bash
Average turbidity based on most recent five measurements = 0.7076 NTU
Info: Turbidity is below the threshold for safe use
Minimum time required to return below a safe threshold = 0 hours
```

This sample output demonstrates the information that the script displays when the water is below the safe threshold, so it will take 0 hours for it to become safe. When the water is above the safe threshold, the script issues a "Warning" and gives the number of hours until the water becomes safe. 
