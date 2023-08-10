# Python-Assignment


Create a RESTful API with:
1. A linked database (use SQLite or some other file database if no database servers are
available) with a user table containing the below fields:

a. id
b. first_name
c. last_name
d. age
e. gender
f. email
g. phone
h. Birth_date

2. Endpoint /api/users with a mandatory query parameter: first_name.
3. Feature for searching the user table for all users with the beginning of first_name
matching the param first_name.
For example: "will" will match both "will" and "william".
a. If users are found then return the list of matching users in a JSON response.
b. Else call the API: https://dummyjson.com/users/search?q=first_name
with the first_name parameter, save the resulting users to the user table and return
them in the response.







Setup:

Start by installing the required packages using pip:

pip install Flask Flask-SQLAlchemy


Run the Flask application


