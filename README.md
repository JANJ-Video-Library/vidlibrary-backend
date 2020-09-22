# vidlibrary-backend
The backend was made with [Django](https://www.djangoproject.com/)

# Setting up the backend
- Ensure you have python3 installed on your machine
- Set up python virtual environment
    - Run pip3 install -r requirements.txt
    - Run python3 manage.py makemigrations 
    - Run python3 manage.py migrate

# Running the backend
- Run python3 manage.py runserver

The backend must be running in order to access it through the API endpoints

# API Endpoints
<h4>
/
</h4>
[POST]<br>
requires API token 
<br>
{<br>
    “title”: “< video title >”,<br>
    “link”: < video link ><br>
    "category": < video category ><br>
}<br>

</h4>
[GET]<br>
requires API token 
<br>
Returns all videos

<h4>
/categories
</h4>
[POST]<br>
requires API token 
<br>
{<br>
    “type”: “< video title >”,<br>
}<br>

</h4>
[GET]<br>
requires API token 
<br>
Returns all video types
