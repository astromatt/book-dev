#!/usr/bin/env python2

import httplib
import ldap
import urllib
import logging
import re


"""
Basic configuration
"""

class Config(object):
    host = 'localhost:8000'
    token = '...'
    jsessionid = '...'
    entities_file = '/Users/matt/Projects/clitools/entities.xml'
    entities_attrs = ['author', 'caller', 'lead', 'name', 'newstring', 'reporter', 'roletypeparameter', 'updateauthor', 'user', 'username', 'userName', 'lowerUserName', 'childName', 'lowerChildName']
    ldap_addr = 'ldap://localhost:3268'
    ldap_user = '...'
    ldap_pass = '...'
    ldap_dc = '...'
    fallback_domains = []


class DoNotDelete(object):
    groups = ["jira-administrators", "jira-users"]
    custom_fields = [11152, 10507, 11210, 10068, 11240, 10773, 11190, 10086, 10105, 10797, 11063, 11064, 10356]
    projects = [10605, 11600, 10607, 10800, 10600]
    permission_schemes = [0]
    workflow_schemes = []
    workflows = []
    issue_types = [1, 2, 3, 4, 5, 9, 107, 146, 126, 127, 128, 157, 237]
    issue_type_schemes = []
    statuses = []
    notification_schemes = []
    project_roles = [10002, 10001, 10000]

"""
You shouldn't change anything below this point,
unless you know what are you doing.
"""

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime).19s] %(levelname)s: %(message)s'
)

class Http(object):
    """ Http request class """

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


class Delete(object):
    """ Delete Abstract Class """

    pretty_name = None
    list_url = None
    list_re = None
    safe_data = []
    delete_url = None
    delete_param = "id"

    def __init__(self):
        if not self.pretty_name:
            self.pretty_name = self.__class__.__name__

        if self.__class__.__name__ == "Delete":
            raise NotImplementedError

        logging.warning("Deleting %ss" % self.pretty_name)

    def get_delete_data(self):
        html = Http.GET(self.list_url, {"start": 0, "max": 10000})
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


"""
Migration procedures
"""

class DeleteGroups(Delete):
    pretty_name = "Group"
    list_url = "/GroupBrowser.jspa"
    list_re = r'DeleteGroup!default.jspa(.*);name=(.*)"'
    safe_data = DoNotDelete.groups
    delete_url = "/DeleteGroup.jspa"
    delete_param = "name"

class DeleteCustomFields(Delete):
    pretty_name = "Custom Field"
    list_url = "/ViewCustomFields.jspa"
    list_re = r'DeleteCustomField!default.jspa\?(.*)id=([0-9]*)"'
    safe_data = DoNotDelete.custom_fields
    delete_url = "/DeleteCustomField.jspa"

class DeletePermissionSchemes(Delete):
    pretty_name = "Permission Scheme"
    list_url = "/ViewPermissionSchemes.jspa"
    list_re = r'DeletePermissionScheme!default.jspa\?schemeId=([0-9]*)"'
    safe_data = DoNotDelete.permission_schemes
    delete_url = "/DeletePermissionScheme.jspa"
    delete_param = "schemeId"

class DeleteNotificationSchemes(Delete):
    pretty_name = "Notification Scheme"
    list_url = "/ViewNotificationSchemes.jspa"
    list_re = r'DeleteNotificationScheme!default.jspa\?(.*)schemeId=([0-9]*)'
    safe_data = DoNotDelete.notification_schemes
    delete_url = "/DeleteNotificationScheme.jspa"
    delete_param = "schemeId"

class DeleteOutgoingMailServers(Delete):
    pretty_name = "Outgoing Mail Sever"
    list_url = "/OutgoingMailServers.jspa"
    list_re = r'DeleteMailServer!default.jspa\?id=([0-9]*)'
    delete_url = "/DeleteMailServer.jspa"

class DeleteProjectRoles(Delete):
    pretty_name = "Project Role"
    list_url = "/ViewProjectRoles.jspa"
    list_re = r'DeleteProjectRole!default.jspa\?id=([0-9]*)'
    safe_data = DoNotDelete.project_roles
    delete_url = "/DeleteProjectRole.jspa"

class DeleteProjects(Delete):
    pretty_name = "Projects"
    list_url = "/ViewProjects.jspa"
    list_re = r'DeleteProject!default.jspa\?pid=([0-9]*)'
    safe_data = DoNotDelete.projects
    delete_url = "/DeleteProject.jspa"
    delete_param = "pid"

class DeleteIssueTypes(Delete):
    pretty_name = "Issue Type"
    list_url = "/ViewIssueTypes.jspa"
    list_re = r'DeleteIssueType!default.jspa\?id=([0-9]*)'
    safe_data = DoNotDelete.issue_types
    delete_url = "/DeleteIssueType.jspa"

class DeleteIssueTypeSchemes(Delete):
    pretty_name = "Issue Type Scheme"
    list_url = "/ManageIssueTypeSchemes.jspa"
    list_re = r'DeleteOptionScheme!default.jspa\?(.*)schemeId=([0-9]*)'
    safe_data = DoNotDelete.issue_type_schemes
    delete_url = "/DeleteOptionScheme.jspa"
    delete_param = "schemeId"

class DeleteWorkflows(Delete):
    pretty_name = "Workflow"
    list_url = "/ListWorkflows.jspa"
    list_re = r'DeleteWorkflow.jspa\?(.*)workflowName=(.*)"'
    safe_data = DoNotDelete.workflows
    delete_url = "/DeleteWorkflow.jspa"
    delete_param = "workflowName"

class DeleteWorkflowSchemes(Delete):
    pretty_name = "Workflow Scheme"
    list_url = "/ViewWorkflowSchemes.jspa"
    list_re = r'DeleteWorkflowScheme!default.jspa\?(.*)schemeId=([0-9]*)'
    safe_data = DoNotDelete.workflow_schemes
    delete_url = "/DeleteWorkflowScheme.jspa"
    delete_param = "schemeId"

class DeleteStatuses(Delete):
    pretty_name = "Status"
    list_url = "/ViewStatuses.jspa"
    list_re = r'DeleteStatus!default.jspa\?id=([0-9]*)'
    safe_data = DoNotDelete.statuses
    delete_url = "/DeleteStatus.jspa"


def rename_users():
    logging.warning("Renaming Users")
    conn = ldap.initialize(Config.ldap_addr)
    conn.simple_bind_s(Config.ldap_user, Config.ldap_pass)

    with open(Config.entities_file) as f:
        logging.info("Looking up for usernames in %s" % Config.entities_file)
        content = f.read()
        userdata = re.compile(r'\n\s{4}<User\s.+?userName="([a-zAZ0-9]+?)".*?emailAddress="([a-zA-Z0-9.+-_@]+?)"')
        unames = userdata.findall(content)
        unames = sorted(unames)

    def get_ldap_username(email, oldname=None):
        oldname = oldname.strip(' ')
        email = email.strip(' ')
        result = conn.search_s(Config.ldap_dc, ldap.SCOPE_SUBTREE, '(proxyAddresses=*%s*)' % email, ['sAMAccountName'])

        try:
            newname = result[0][1]['sAMAccountName'][0]
            logging.debug("User %s matched as %s" % (email, newname))
            return newname
        except Exception:
            logging.debug("User %s not found in LDAP directory" % email)
            try:
                loginname = re.match("(.*?)@(%s)" % "|".join(Config.fallback_domains), email).group(1)
                logging.debug("Will use loginname %s from email addres %s" % (loginname, email))
                return loginname.lower()
            except Exception:
                logging.debug("Domain is not whitelisted, will use old username: %s" % oldname)
                return oldname.lower()

    for oldname, email in unames:
        newname = get_ldap_username(email, oldname)
        logging.info("Substituting username %s with %s" % (oldname, newname))
        replace_from = re.compile(r'="%s"' % oldname)
        content = replace_from.sub(r'="%s"' % newname, content)

    with open(Config.entities_file, "w") as f:
        logging.info("Writing new conent to file %s" % Config.entities_file)
        f.write(content)
        logging.info("Content of %s updated." % Config.entities_file)


if __name__ == "__main__":
    #DeleteOutgoingMailServers().run()
    #DeleteGroups().run()
    #Do not run now new cf added#DeleteCustomFields().run()
    #DeleteProjectRoles().run()
    #DeleteProjects().run()
    #DeleteIssueTypes().run()
    #DeleteIssueTypeSchemes().run()
    #DeleteWorkflowSchemes().run()
    #DeleteWorkflows().run()
    #DeleteStatuses().run()
    #DeletePermissionSchemes().run()
    #DeleteNotificationSchemes().run()

    rename_users()