# Querying and Returning ISS Trajectory Data

This project is compiled of one script that builds a Flask application and provides four different routes to query and return different information from the ISS Trajectory Data.

This is important because the data that users are probably looking for is at least five to six dictionaries deep in the set. The Flask application and the routes allow for users to quickly query the information that they may be looking for without having to comb through the dictionaries manually.

## Accessing the Data
 
The data is loaded in from this link, https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS\_OEM/ISS.OEM\_J2K\_EPH.xml , where the data is in XML format. The application loads it into a dictionary, and each route combs through the many dictionaries embedded in the data set to return what the user is looking for. The data mainly contains state vectors, {X, Y, Z} and {X\_DOT, Y\_Dot, Z\_DOT} for different time stamped Epochs in reference to Earth and the J2000 reference frame.

## Flask App and Its Routes

The Flask application contains a function that loads in the data and four routes that return calculations or different information from the data set. The routes return information from the entire data set to the instantaneous velocity of a specified Epoch.

## Running the App

Install the project by cloning the repository. 
The Flask library must be installed using ``` pip3 install --user flask ```. 
To run the Flask app, use ``` flask --app iss_tracker1 --debug run ```. 

In a separate window, you can use ``` curl localhost:5000 ``` to call the routes.

## Example Queries 

For ```/``` which returns the entire data set:
```
{"EPOCH": ..., "X": {"#text": ..., "@units": ...}, "X_DOT": {"#text": .../ "@units": ...},...}
```
This continues for the entire data set and also includes {Y, Z} and {Y_DOT, Z_DOT} in the state vectors. Those were excluded in this example for simplicity purposes.

For ```/epochs``` which returns a list of all Epochs in the data set:
```
["2023-048T12:00:00.000Z", ... ,"2023-063T12:00:00.000Z"]
```

For ```/epochs/<epoch>``` which returns the state vectors for a specific Epoch:
```
{"EPOCH": ..., "X": {"#text": ..., "@units": ...}, "X_DOT": {"#text": .../ "@units": ...}}
```
This returns only one Epoch and its state vectors, including {Y,Z} and {Y_DOT, Z_DOT}, which are excluded here.

For ```/epochs/<epoch>/speed``` which returns the instantaneous speed for a specific Epoch:

```
{"speed": "... km/s"}
```


