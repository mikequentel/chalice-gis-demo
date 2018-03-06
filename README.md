# (Chalice GIS Demo)[https://github.com/mikequentel/chalice-gis-demo]
* A reference implementation of a REST-exposed GIS server using AWS Lambda functions generated using Chalice. Includes AWS features such as RDS (for the PostgreSQL database), Lambda (for the FaaS modules), API Gateway for handling requests and responses, VPC (Virtual Private Cloud) which enables proper performance between Lambda and RDS.
* Lambda framework: [Chalice](https://github.com/aws/chalice)
* Database: [PostgreSQL](https://www.postgresql.org)
  * Based on restaurant inspection data, from several years ago (circa 2013), collected by the state of New York and shared at the USA government website [data.gov](https://www.data.gov)
    * This is publicly available information published by the US government.
  * The backend database for this demo does not include PostGIS at this time.
* Connection to database: [psycopg2](http://initd.org/psycopg)


# Interfaces
## Examples of included interfaces--one exists for each field in the database.
* Select top (limit) of items **/restaurants/limit/{limit}** eg: https://a4fpsm6md0.execute-api.us-east-1.amazonaws.com/api/restaurants/limit/100
* Select by object ID **/restaurants/oid/{oid}** eg: https://a4fpsm6md0.execute-api.us-east-1.amazonaws.com/api/restaurants/oid/1441071
* Select by circle (items within the circle), with parameters latitude, longitude, and radius in km **/restaurants/circle/{circle}** eg: https://a4fpsm6md0.execute-api.us-east-1.amazonaws.com/api/restaurants/circle/43.1009,-75.2327,150.5
* Select by bounding box (items within bounding box), with parameters upper left latitude, upper left longitude, lower right latitude, lower right longitude **/restaurants/bbox/43.000000,-79.000000,41.000000,-71.000000** eg: https://a4fpsm6md0.execute-api.us-east-1.amazonaws.com/api/restaurants/bbox/43.000000,-79.000000,41.000000,-71.000000
* Select by facility (restaurant) name **/restaurants/facility/{facility}** eg: https://a4fpsm6md0.execute-api.us-east-1.amazonaws.com/api/restaurants/facility/LITTLE%20ROMA%20PIZZA,%20INC.
* Select by county containing facilities of interest **/restaurants/county/{county}** eg: https://a4fpsm6md0.execute-api.us-east-1.amazonaws.com/api/restaurants/county/ONEIDA
