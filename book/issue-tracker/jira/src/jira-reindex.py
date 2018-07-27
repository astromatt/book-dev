from pprint import pprint
from atlassian import Jira


jira = Jira(
    url="http://localhost:8000/",
    username="admin",
    password="admin")

status = jira.reindex().json()
pprint(status)