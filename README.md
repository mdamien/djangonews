== Installation ==

Use a venv with django 1.5  
pip install django-social-auth  
clone django-mptt && python setup.py install  

put a local_settings.py in djangonews  with:
MEDIA_ROOT 
STATIC_ROOT
SECRET_KEY
GITHUB_APP_ID
GITHUB_API_SECRET

Github keys by registering an application (even a localhost:8000 one)

python-sqlite3  

#TODO: 

POST requests with CRSF  
Comment/post field vote / vote by POST  
Paging
ordering comments by score  
more dynamic score (depends of the time)    