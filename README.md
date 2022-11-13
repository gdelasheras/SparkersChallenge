# SparkersChallenge

#### Author: [Gonzalo de las Heras](https://www.linkedin.com/in/gdelasheras/)

## Requirements

* `python==3.7`
* `requests==2.28.1`
* `pandas==1.3.5` (another option would be pyspark, but pandas has been used because the dataset is not extremely large and fits in memory.)
* `numpy==1.21.5`
* `pydantic==1.10.2`
* `pytest==7.2.0`

## Docker images

A docker image has been created. Executing these commands will create the image and run it:

* `docker run -it sparkers-dota-stats`
* `docker build --no-cache -t sparkers-dota-stats .`

## Tests

The unit tests are organized following the same structure of the application.

## Future work

### Technical

* Create a REST API to obtain the information.
* Store the stats in a database.
* Store the raw data in an HDFS.
* Create a scheduled task to update the match data to avoid having to call the API on demand.

### Functional

* Calculate win-rates per side and champions.
* Calculate KDA and KP stats per hero.
* Calculate stats oriented to heroes and positions in the map.
* Calculate stats by hero combinations.