# Gene Party 2.0: Parsing HGNC Data and Using Kubernetes

This project is compiled of one script that builds a Flask application and provides different routes for the user to query that return different pieces of information about the HGNC data, using the HGNC data from HUGO. The project also includes a Dockerfile that allows any user to pull the image from Docker Hub and run an instance of the image into a container on their personal machine, as well as a Docker-compose file that allows a user to start the container easily and succinctly.

The Flask application routes are important because the HGNC data contains loads of information that may not be interesting to the user. The Flask application and the routes allow users to quickly query the information that they may be looking for without having to comb through the data manually. The application also utilizes the Redis database, making it possible to store and come back to the data. The Dockerfile allows any user to have access to these capabilities through running an instance of the image on their own machine, plus the Docker compose file automates the deployment of the application, so the container is easy to start. 

Thr project also includes five .yml files that include a Redis service, deployment, and pvc, as well as a Flask service and deployment. These files allow the project to be used with Kubernetes.

## Accessing and Describing the Data
 
The HGNC data is loaded in from this link, https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc\_complete\_set.json , where the data is in json format. The application uses requests to access the data, and the POST route puts the data into the Redis database. The data contains lots of unique and interesting information about every hgnc\_id that the HGNC knows exists.

## Flask App and Its Routes

The Flask application contains a function that loads the data into the Redis database and different routes that return all of the information, only hgnc\_id's, or all of the information about a specific hgnc\_id. There is also a route that clears the data from the database.

## Pulling the Image and Running the App

Install the project by cloning the repository. 

Use ```docker pull avlavelle/gene_api``` to pull a copy of the container.
Then, ```docker-compose up``` will get the container running using the compose file, build the image, and bind the appropriate port inside the container to the appropriate port on the host.

In a separate window, you can use ``` curl localhost:5000 ``` to call the routes.

## Building a New Image from the Dockerfile

In order to build a new image from the Dockerfile, use the same ```docker pull``` command from above. 
Then, use ```docker-compose build``` to build the image and use ```docker images``` to check that a copy of the image has been built.

## Using Kubernetes

Clone the repository and pull the image using instructions from above. No changes should be required for the Kubernetes file, but the Python script might require a change to the host of the Redis client. Using ```kubectl get services```, users should be able to find the IP address of their Redis service. This will be the new host for the Redis service in the Python script.

After adjusting the Python script, build a new image from the Dockerfile using the instructions from above. 

## Example Queries and Interpretation of Results

For the ```/data``` POST route which puts the data into Redis:
```
Data loaded
```

For the ```/data``` DELETE route which deletes the data in Redis:
```
Data deleted, there are 0 keys in the db
```

For the ```/data``` GET route which returns all the data from Redis:
```
[{"version": ..., "alias_symbol": [...], "data_approved_reserved": ...}...]
```

For the ```/genes``` route which returns a json-formatted list of all hgnc_ids:
```
[..., "HGNC:13195", ..., "HGNC:24523"]
```

For the ```/genes/<hgnc_id>``` route which returns all the data associated with <hgnc_id>:
```
{["hgnc_id": "HGNC:24523", "location": ..., ...]}
```
