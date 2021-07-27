# Suggestic-Challenge

### Getting Started
* Install docker and docker compose
* Set in project directory
* Run `docker-compose up -d` command
* Try to Request to Endpoints:
    * `POST`- `http://localhost:8000/api/flattnes/sequence/
        ````
        Body:
        {
            "sequence": [1, 2, [3, 4, [5, 6], 7], 8]
        }
    * `GET`- `http://localhost:8000/api/sequence/
