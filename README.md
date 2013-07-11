# Django News
*A hackernews clone built in django for fun*

Complete with:

- Post & Comments scores
- Threaded comments
- GitHub login

## Installation

You need to have:
- Django 1.5
- django-social-auth (for GitHub login)
- django-mptt (for threaded comments)
- python-sqlite3

Then, just do a `.manage.py runserver` as usual and go to /admin/ to connect with:  
>login: admin  
>password: admin  

If you want the github login:  
You need to add a local_settings.py file in djangonews with GITHUB_APP_ID & GITHUB_API_SECRET set


###TODO

- Upvotes are done with a simple GET request, it needs to be a POST request
- calculation of scores are really inefficient, caching them would be better
- pagination of the index
- ordering comments by score