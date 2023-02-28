# Containerizing the Querying and Returning ISS Trajectory Data

This project is compiled of one script that builds a Flask application and provides four different routes to query and return different information from the ISS Trajectory Data, as well as a Dockerfile that allows any user to pull the image and run an instance of the image into a container on their personal machine.

This is important because the data that users are probably looking for is at least five to six dictionaries deep in the set. The Flask application and the routes allow for users to quickly query the information that they may be looking for without having to comb through the dictionaries manually. The Dockerfile allows any user to have access to these capabilities 

## Accessing and Describing the Data
 
The data is loaded in from this link, https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS\_OEM/ISS.OEM\_J2K\_EPH.xml , where the data is in XML format. The application loads it into a dictionary, and each route combs through the many dictionaries embedded in the data set to return what the user is looking for. The data mainly contains state vectors, {X, Y, Z} and {X\_DOT, Y\_Dot, Z\_DOT} in km/s for different time stamped locations of the ISS in reference to Earth and the J2000 reference frame.

## Flask App and Its Routes

The Flask application contains a function that loads in the data and different routes that return calculations or different information from the data set. The routes return information from the entire data set to the instantaneous velocity of a specified Epoch.

## Pulling the Image and Running the App

Install the project by cloning the repository. 

Use ```docker pull avlavelle/iss_tracker:1.0``` to pull a copy of the container.
Then, ```docker run -it --rm -p 5000:5000 avlavelle/iss_tracker:1.0``` will get the container running and will connect the container's port 5000 to the host's port 5000.

In a separate window, you can use ``` curl localhost:5000 ``` to call the routes.

## Building a New Image from the Dockerfile

In order to build a new image from the Dockerfile, use the same ```docker pull``` command from above. 
Then, use ```docker build -t <username>/iss_tracker .``` to build the image and use ```docker images``` to check that a copy of the image has been built.

## Example Queries 

For ```/``` which returns the entire data set:
```
{"EPOCH": ..., "X": {"#text": ..., "@units": ...}, "X_DOT": {"#text": .../ "@units": ...},...}
```
This continues for the entire data set and also includes {Y, Z} and {Y_DOT, Z_DOT} in the state vectors. Those were excluded in this example for simplicity purposes.

For ```/epochs``` which returns a list of all Epochs in the data set or ```/epochs?limit=int&offset=int``` which returns a modified list of Epochs given query parameters:
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
For ```/help``` which returns help text describing the routes:
```
These are the routes for iss_tracker.py.

return elements from the data set
   / (GET)                          Return entire data set
```
The rest of the route descriptions are excluded here.

For ```/delete-data``` which deletes all data from the dictionary object:
```
Data has been deleted
```

For ```/post-data``` which reloads the dictionary object with data from the ISS Trajectory link:
```
Data has been restored
```

