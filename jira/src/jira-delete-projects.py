import logging
import re
import urllib

import httplib

"""
.. todo::
   * Add autodiscovery of token and jsessionid
   * Do not delete projects by porojectkey not id
   * Simplify
   * Remove not used headers and params
"""


class Config(object):
    host = 'localhost:8080'
    do_not_delete_project = [10300] #EKO

    # You can get this from inspecting HTTP request with WebInspector in your Browser
    token = '...'
    jsessionid = '...'


"""
You shouldn't change anything below this point,
unless you know what are you doing.
"""
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime).19s] %(levelname)s: %(message)s'
)


class Http(object):

    @staticmethod
    def GET(url, params={}):
        params["atl_token"] = Config.token
        params = urllib.urlencode(params)
        return Http._request("GET", "%s?%s" %(url, params))

    @staticmethod
    def POST(url, params={}):
        params["atl_token"] = Config.token
        params["Delete"] = "Delete"
        params["confirmedDelete"] = "true"
        params["workflowMode"] = "live"
        params["confirm"] = "true"
        params["confirmed"] = "true"
        return Http._request("POST", url, params)

    @staticmethod
    def _request(method, url, params={}):
        params = urllib.urlencode(params)
        headers = {
            "Cookie": "atlassian.xsrf.token=%s; JSESSIONID=%s" % (Config.token, Config.jsessionid),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        conn = httplib.HTTPConnection(Config.host)
        logging.debug("curl -X %(method)s -d '%(params)s' --cookie '%(cookie)s' http://%(host)s%(path)s" % {
            'method': method,
            'params': params,
            'cookie': headers['Cookie'],
            'host': Config.host,
            'path': url,
        })
        conn.request(method, url, params, headers)
        response = conn.getresponse()
        logging.debug("%s %s" % (response.status, response.reason))
        ret = response.read()
        response.close()
        return ret


class DeleteAbstract(object):
    pretty_name = None
    list_url = None
    list_re = None
    safe_data = []
    delete_url = None
    delete_param = "id"

    def __init__(self):
        if not self.pretty_name:
            self.pretty_name = self.__class__.__name__
        if self.__class__.__name__ == "DeleteAbstract":
            raise NotImplementedError
        logging.warning("%s" % self.pretty_name)

    def get_delete_data(self):
        html = Http.GET(self.list_url, {"start":0, "max":10000})
        matches = re.findall(self.list_re, html)
        try:
            if isinstance(matches[0], tuple):
                matches = [id for string, id in matches]
        except IndexError:
            print("Not authorized or no entries.")

        def clean(matches):
            matches = [urllib.unquote(name).decode('utf8') for name in matches]
            matches = [name.replace('+', ' ') for name in matches]
            return matches
        return clean(matches)

    def run(self):
        for id in self.get_delete_data():
            if str(id) not in [str(x) for x in self.safe_data]:
                logging.info("Deleting %s: %s" % (self.pretty_name, id))
                Http.POST(self.delete_url, {self.delete_param: id})


class DeleteProjects(DeleteAbstract):
    pretty_name = "Deleting Projects"
    list_url = "/ViewProjects.jspa"
    list_re = r'DeleteProject!default.jspa\?pid=([0-9]*)'
    safe_data = Config.do_not_delete_project
    delete_url = "/DeleteProject.jspa"
    delete_param = "pid"


if __name__ == "__main__":
    DeleteProjects().run()
