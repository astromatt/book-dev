from atlassian import Jira

jira = Jira(
    url="http://localhost:8080/",
    username="jira-administrator",
    password="admin")

jira.reindex()
