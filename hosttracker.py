import requests

server_url = 'https://host-tracker.com'
api_version = 'v1'

class HostTracker(object):
    def __init__(self, url=server_url, username=None, password=None):
        self.url = '%s/api/web/%s' % (server_url, api_version)
        data = {'login':username,'password':password}
        r = requests.post(self.url+'/users/token', data=data)
        #todo error handling
        self.token = r.json()['ticket']

