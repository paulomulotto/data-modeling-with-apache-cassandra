# Data Modeling with Apache Cassandra

## Overview

The goal of this project is to develop a data processing pipeline that extracts, transforms, and loads music app streaming data from CSV files into Apache Cassandra.
The pipeline enables querying and analysis of the music app history to answer specific questions about the artists, songs, and user interactions within the app.
The project demonstrates the use of Apache Cassandra as a powerful database solution for handling large-scale data with high availability and performance, providing valuable insights for music app analytics and decision-making.

# Data Description

This repository contains a CSV file named `data.csv` that contains information about user activities on a music streaming app. The file has the following columns:

- `artist`: The name of the artist who performed the song.
- `auth`: The authentication status of the user.
- `firstName`: The first name of the user.
- `gender`: The gender of the user.
- `itemInSession`: The index of the item within the user's session.
- `lastName`: The last name of the user.
- `length`: The length of the song in seconds.
- `level`: The user's subscription level (paid or free).
- `location`: The location of the user.
- `method`: The HTTP method used in the request.
- `page`: The page or action performed by the user.
- `registration`: The timestamp (miliseconds) of the user's registration.
- `sessionId`: The ID of the session.
- `song`: The title of the song.
- `status`: The HTTP status code of the response.
- `ts`: The timestamp of the user's activity.
- `userId`: The ID of the user.

## Data Sample

Here is a sample of the data in the CSV file:

| artist        | auth       | firstName | gender | itemInSession | lastName | length    | level | location           | method | page     | registration  | sessionId | song                | status | ts            | userId |
|---------------|------------|-----------|--------|---------------|----------|-----------|-------|---------------------|--------|----------|---------------|-----------|---------------------|--------|---------------|--------|
|               | Logged Out |           |        | 0             |          |           | free  |                     | PUT    | Login    | 1.54121E+12   | 52        |                     | 307    | 1.54121E+12   | 1      |
|               | Logged In  | Celeste   | F      | 1             | Williams |           | free  | Klamath Falls, OR   | GET    | Home     | 1.54108E+12   | 52        |                     | 200    | 1.54121E+12   | 53     |
| Mynt          | Logged In  | Celeste   | F      | 2             | Williams | 166.94812 | free  | Klamath Falls, OR   | PUT    | NextSong | 1.54108E+12   | 52        | Playa Haters        | 200    | 1.54121E+12   | 53     |
| Taylor Swift  | Logged In  | Celeste   | F      | 3             | Williams | 230.47791 | free  | Klamath Falls, OR   | PUT    | NextSong | 1.54108E+12   | 52        | You Belong With Me  | 200    | 1.54121E+12   | 53     |


## Prerequisites

Before running the project, make sure you have the following prerequisites installed on your machine:

- Docker

## Setup and Installation

Follow the steps below to set up and install the project:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Navigate to the docker folder
4. Run the command <code>docker compose build</code>

## Usage

1. Navigate to the docker folder
2. Start the Docker containers:
    ```
    docker-compose up
    ```
3. In the console output, you will see logs from the containers. Look for the Jupyter Notebook container's logs. You can use the following command to retrieve the logs in another terminal:
    ```
    docker logs <container_name>
    ```
5. Replace <container_name> with the actual name or ID of the Jupyter Notebook container. The container name can be found by running the command docker ps.
Among the logs, you will find a line similar to:
    ```
    To access the notebook, open this file in a browser:
        file:///home/jovyan/.local/share/jupyter/runtime/nbserver-6-open.html
    Or copy and paste one of these URLs:
        http://127.0.0.1:8888/?token=abcdef1234567890
    ```
6. Copy the URL starting with http://127.0.0.1:8888/ from the logs.
7. Access the Jupyter Notebook by opening a web browser and navigating to the copied URL.
8. Enter the token when prompted. The token can be found after ?token= in the URL.
9. Once inside Jupyter Notebook, navigate to the desired project directory.
Run the provided notebooks or create your own notebooks to interact with the project.
10. Stop the Docker containers when you're finished:
    ```
    docker-compose down
    ```
