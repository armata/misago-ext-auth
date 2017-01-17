# make sure to set SESSION_COOKIE_HTTPONLY to False

import requests

FORUM_URL = 'https://misago-project.org/'

USERNAME = ''
PASSWORD = ''

s = requests.Session()

# make a GET request to the token API endpoint
url = '{}/api/auth/token/'.format(FORUM_URL)
r = s.get(url)

# extract the CSRF token
csrftoken = s.cookies.get('csrftoken')

# update headers
s.headers.update({'X-CSRFToken': csrftoken})

# make a POST request to the auth API endpoint
url = '{}/api/auth/'.format(FORUM_URL)
data = {'username': USERNAME, 'password': PASSWORD}
r = s.post(url, data=data)
