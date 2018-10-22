from atlassian import Confluence
from atlassian import Jira

jira = Jira(
    url='http://localhost:8080',
    username='admin',
    password='admin')

confluence = Confluence(
    url='http://localhost:8090',
    username='admin',
    password='admin')

html = ['<table><tr><th>Project Key</th><th>Project Name</th><th>Leader</th><th>Email</th></tr>']

for data in jira.project_leaders():
    row = '<tr><td>{project_key}</td><td>{project_name}<td></td>{lead_name}<td></td><a href="mailto:{lead_email}">{lead_email}</a></td></tr>'
    html.append(row.format(**data))

html.append('</table><p></p><p></p>')

status = confluence.create_page(
    space='DEMO',
    parent_id=confluence.get_page_id('DEMO', 'demo'),
    title='JIRA Administrators',
    body='\r\n'.join(html))

print(status)
