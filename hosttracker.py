import requests
import logging

log = logging.getLogger(__name__)

server_url = 'https://host-tracker.com'
api_version = 'v1'

class HostTracker(object):
    """ Main object to connect with host-tracker
    
    Before use this you should activate API for your account.
    See https://www.host-tracker.com/api/web/help.html

    """
    def __init__(self, url=server_url, username=None, password=None):
        self.url = '%s/api/web/%s' % (server_url, api_version)
        data = {'login':username,'password':password}
        r = requests.post(self.url+'/users/token', data=data)
        if r.status_code != 200:
            log.error('ERROR from %s: %d' %(r.url, r.status_code))
            log.error('Returned data: %s\n' % r.json())
            r.raise_for_status()

        token = r.json()['ticket']
        self.auth_headers = {'Authorization:' 'bearer ' + token}
    

    def get_tasks(self):
        """ Get list of all tasks """
        r = requests.get(self.url+'/tasks', headers=self.auth_headers)
        if r.status_code != 200:
            log.error('ERROR from %s: %d' %(r.url, r.status_code))
            log.error('Returned data: %s\n' % r.json())
            r.raise_for_status()
        return r.json()


    def get_task(self, task_id):
        """ Get information about specified task """
        r = requests.get(self.url+'/tasks/+'task_id, headers=self.auth_headers)
        if r.status_code != 200:
            log.error('ERROR from %s: %d' %(r.url, r.status_code))
            log.error('Returned data: %s\n' % r.json())
            r.raise_for_status()
        return r.json()


    def new_task(self, name, url, type='http', **kwargs):
        """ Create new task with settings specified by provided parameters """
        if type == 'http':
            """ Documentation about parameters is there https://www.host-tracker.com/api/web/v1/tasks/help#createHttp """
            parameters = {'name':name, 'url':url}
            for key, value in kwargs.iteritems():
                parameters[key] = value

            r = requests.post(self.url+'/tasks/http', data=parameters, headers=self._auth_headers)
            if r.status_code != 201:
                log.error('ERROR from %s: %d' %(r.url, r.status_code))
                log.error('Returned data: %s\n' % r.json())
                r.raise_for_status()
        else:
            raise Exception("Type %s is not supported yet. Please fill free to send pull requests to support it" % type)
        return r.json()['id']

    def delete_task(self, task_id):
        """ Remove specified task """
        r = requests.delete(self.url+'/tasks/'+task_id, headers=self.auth_headers)
        if r.status_code != 200:
            log.error('ERROR from %s: %d' %(r.url, r.status_code))
            log.error('Returned data: %s\n' % r.json())
            r.raise_for_status()
        return r.json() 
