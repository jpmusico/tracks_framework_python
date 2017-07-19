import requests
from xml.etree import ElementTree


class ProjectsAPI(object):

    def get_all():
        r = requests.Session()
        r.auth = ('admin', 'admin')
        response = r.get('http://192.168.0.6:8080/projects.xml')
        tree = ElementTree.fromstring(response.content)
        return tree.find('.//project[2]/name').text
