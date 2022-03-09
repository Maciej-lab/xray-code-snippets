import requests
from base64 import urlsafe_b64encode as b64e   

jira_base_url = "http://192.168.56.102"
jira_username = "admin"
jira_password = "admin"
personal_access_token = "OTE0ODc2NDE2NTgxOnrhigwOreFoyNIA9lXTZaOcgbNY"


# endpoint doc for importing Xray JSON reports: https://docs.getxray.app/display/XRAY/Import+Execution+Results+-+REST#ImportExecutionResultsREST-XrayJSONresults
report_content = open(r'xray_dc.json', 'rb')

# importing results using HTTP basic authentication
# response = requests.post(f'{jira_base_url}/rest/raven/2.0/import/execution', params=params, data=report_content, auth=(jira_username, jira_password), headers=headers)

# importing results using Personal Access Tokens 
headers = {'Authorization': 'Bearer ' + personal_access_token, 'Content-Type': 'application/json'}
response = requests.post(f'{jira_base_url}/rest/raven/2.0/import/execution', data=report_content, headers=headers)

print(response.status_code)
print(response.content)
