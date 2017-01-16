import requests

FORUM_URL = 'https://misago-project.org/'

USERNAME = 'username'
PASSWORD = 'password'

# make a GET request to the token API endpoint
url = '{}/api/auth/token/'.format(FORUM_URL)
r = requests.get(url)

# extract the CSRF token
csrftoken = r.cookies['csrftoken']

print(csrftoken)

# make a POST request to the auth API endpoint
url = '{}/api/auth/'.format(FORUM_URL)
data = {'username': USERNAME, 'password': PASSWORD}
headers = {'X-CSRFToken': csrftoken}

r = requests.post(url, data=data, headers=headers)

print(r.text)
