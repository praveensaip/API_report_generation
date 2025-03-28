import os,requests,time
a = os.path.join(os.path.dirname(__file__),'API report generation(1)')
print(a)
url = "https://api-plus-stage.anbetrack.com/core/api/v1/jobExecutions"
token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY1MWU4NmRjMmM4Nzg2YjNjMjgzN2QyNCIsImZpcnN0TmFtZSI6IlByYXZlZW5rdW1hciIsImxhc3ROYW1lIjoiUyIsImVtYWlsIjoicHJhdmVlbnNhaXA5OUBnbWFpbC5jb20iLCJvcmdhbml6YXRpb24iOiJBTkIgU3lzdGVtcyIsInRlbmFudCI6IkluaG91c2VfUmVwb3J0Iiwicm9sZXMiOlsiU3VwZXJ1c2VyIl0sImxvZ2luIjoicHJhdmVlbl9JbmhvdXNlIiwicHJvZHVjdCI6ImVUcmFja1BsdXMiLCJkZWZhdWx0Um9sZSI6IlN1cGVydXNlciIsImhhc1JlcG9ydEFjY2VzcyI6ZmFsc2UsInNvdXJjZSI6InVpIiwiZW52aXJvbm1lbnQiOiJzdGFnZSIsImdyb3VwIjoicWFfdGVzdCIsImFwcGx5R2V0QWNsIjp0cnVlLCJpYXQiOjE3NDMxNDE0ODMsImV4cCI6MTc0MzE0NTY4M30.Kgod27Ght4Hh3ke_UcuBDhDk8BfL9cZNLkfF5zhOMO0"
headers={
    'Content-Type':'application/json',
    'authorization':token
}

payload = {
    "job": {
        "id": "67e51323c94a7f570d9ebc6f",
        "name": "API report Generate Job",
        "context": {
            "entityType": "*",
            "code": ""
        },
        "belongsTo": {
            "entityType": "model",
            "entity": "apiReportGeneration"
        },
        "type": "dataTransfer",
        "organization": {
            "_id": "63eb28f3439562479abe1f68",
            "tenant": "Inhouse_Report",
            "product": "eTrackPlus",
            "name": "ANB Systems",
            "code": "ANB",
            "organizationType": "Utility",
            "createdBy": "inhousereportadmin",
            "addresses": [
                {
                    "id": "7ace2100-be6e-11e9-b284-752962b8f1a1",
                    "addressType": "Billing Address",
                    "street": "Chennai",
                    "city": "Chennai",
                    "state": "Tamil Nadu",
                    "country": "India",
                    "zipCode": "99999-9999",
                    "workPhone": "(999) 999-9999",
                    "isPrimary": False,
                    "isActive": True
                }
            ],
            "canCreateUser": True,
            "updatedBy": "inhousereportadmin",
            "isActive": True,
            "createdAt": "2023-02-14T06:23:47.490Z",
            "updatedAt": "2023-02-14T06:23:47.490Z"
        }
    },
    "status": "Uploading File",
    "trigger": "ad-hoc",
    "triggeredBy": "praveen_Inhouse",
    "triggeredAt": "2025-03-28T06:00:41.780Z",
    "executedBy": {
        "tenant": "Inhouse_Report",
        "login": "praveen_Inhouse",
        "firstName": "Praveenkumar",
        "lastName": "S",
        "organization": "ANB Systems",
        "defaultRole": "Superuser",
        "roles": [
            "Superuser"
        ],
        "environment": "stage",
        "product": "eTrackPlus"
    },
    "fileName": "API report generation(1)",
    "isSuppressWarnings": False,
    "filter": {}
}
req = requests.post(url=url,headers=headers,json=payload)
data=req.json()
job_id, execution_id= data['ops'][0]['job']['id'], data['insertedId']

print("executed")


time.sleep(5)

execute = f"https://api-plus-stage.anbetrack.com/core/api/v1/jobs/{job_id}/execute"
execute_payload = {
    "name": "API report Generate Job",
    "triggers": [
        "ad-hoc"
    ],
    "isActive": True,
    "type": "dataTransfer",
    "isOrganizationRequired": False,
    "organizationTypes": [],
    "organizations": [],
    "context": {
        "entityType": "*",
        "code": ""
    },
    "belongsTo": {
        "entityType": "model",
        "entity": "apiReportGeneration"
    },
    "filters": [],
    "isSuppressWarnings": False,
    "suppressWarningList": [],
    "enforceFileUpload": True,
    "info": {},
    "tenantId": "Inhouse_Report",
    "jobExecutionId": execution_id,
    "executedBy": {
        "tenant": "Inhouse_Report",
        "login": "praveen_Inhouse",
        "firstName": "Praveenkumar",
        "lastName": "S",
        "organization": "ANB Systems",
        "defaultRole": "Superuser",
        "roles": [
            "Superuser"
        ],
        "environment": "stage",
        "product": "eTrackPlus"
    }
}

req = requests.post(url=execute,headers=headers,json=execute_payload)
print(req)