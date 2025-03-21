import requests, json, base64
import zipfile

# url = "https://api-plus-stage.anbetrack.com/core/api/v1/documentInstances/67dba12e3a37a578a7da3205/content"
# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY1MWU4NmRjMmM4Nzg2YjNjMjgzN2QyNCIsImZpcnN0TmFtZSI6IlByYXZlZW5rdW1hciIsImxhc3ROYW1lIjoiUyIsImVtYWlsIjoicHJhdmVlbnNhaXA5OUBnbWFpbC5jb20iLCJvcmdhbml6YXRpb24iOiJBTkIgU3lzdGVtcyIsInRlbmFudCI6IkluaG91c2VfUmVwb3J0Iiwicm9sZXMiOlsiU3VwZXJ1c2VyIl0sImxvZ2luIjoicHJhdmVlbl9JbmhvdXNlIiwicHJvZHVjdCI6ImVUcmFja1BsdXMiLCJkZWZhdWx0Um9sZSI6IlN1cGVydXNlciIsImhhc1JlcG9ydEFjY2VzcyI6ZmFsc2UsInNvdXJjZSI6InVpIiwiZW52aXJvbm1lbnQiOiJzdGFnZSIsImdyb3VwIjoicWFfdGVzdCIsImFwcGx5R2V0QWNsIjp0cnVlLCJpYXQiOjE3NDI0NDY0NTQsImV4cCI6MTc0MjQ1MDY1NH0.eSFU5ungIB5X3nzy93VoqE1zsOqKZ4cDCYXykaw1Y8M"
# typ = {
#     "Content-Type":"application/octet-stream",
#     "Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY1MWU4NmRjMmM4Nzg2YjNjMjgzN2QyNCIsImZpcnN0TmFtZSI6IlByYXZlZW5rdW1hciIsImxhc3ROYW1lIjoiUyIsImVtYWlsIjoicHJhdmVlbnNhaXA5OUBnbWFpbC5jb20iLCJvcmdhbml6YXRpb24iOiJBTkIgU3lzdGVtcyIsInRlbmFudCI6IkluaG91c2VfUmVwb3J0Iiwicm9sZXMiOlsiU3VwZXJ1c2VyIl0sImxvZ2luIjoicHJhdmVlbl9JbmhvdXNlIiwicHJvZHVjdCI6ImVUcmFja1BsdXMiLCJkZWZhdWx0Um9sZSI6IlN1cGVydXNlciIsInNvdXJjZSI6InVpIiwiZW52aXJvbm1lbnQiOiJzdGFnZSIsImdyb3VwIjoicWFfdGVzdCIsImFwcGx5R2V0QWNsIjp0cnVlLCJpYXQiOjE3NDI0NTU0NDMsImV4cCI6MTc0MjQ1OTY0M30.OeJK6gEYxHhusg4o03FFMEqFcCaXJITMCpyvBDEtyxc"}
# a = requests.get(url, headers = typ)
# if a.status_code == 200:
#     # dd112 = base64.b64decode(a.content).decode('urf-8')
#     dd = base64.b64encode(a.content).decode('utf-8')
#     json_data = {
#         "file_data": dd
#     }
#     with open("dd12.json",'w') as file:
#         json.dump(json_data, file, indent=4)
#     print("completed")


# decoded_data = base64.b64decode(dd)
# print("decords", decoded_data)

# with open('data.ext', 'wb') as f:
#     f.write(dd112)

# with open('data.zip', 'wb') as f:
#     f.write(decoded_data)

# with zipfile.ZipFile('data.zip', 'r') as zip_ref:
#     zip_ref.extractall('extracted_files')
# xml_file_path = 'extracted_files/xl/worksheets/sheet1.xml'
# with open(xml_file_path, 'r', encoding='utf-8') as f:
#     xml_data = f.read()
# print(xml_data)



# with open("Dashboard - Parameter.pdf","rb") as file:
#     test = file.read()
# dd = base64.b64encode(test).decode('utf-8')
# print("dd",dd)

# jj={
#     "test":dd
# }
# ff =json.dumps(jj)
# with open('333.json','w') as file:
#     file.write(ff)


import requests
url = "https://api-plus-stage.anbetrack.com/bsq/api/v1/query"
headers = {
    "Content-Type":"application/json",
    "Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY1MWU4NmRjMmM4Nzg2YjNjMjgzN2QyNCIsImZpcnN0TmFtZSI6IlByYXZlZW5rdW1hciIsImxhc3ROYW1lIjoiUyIsImVtYWlsIjoicHJhdmVlbnNhaXA5OUBnbWFpbC5jb20iLCJvcmdhbml6YXRpb24iOiJBTkIgU3lzdGVtcyIsInRlbmFudCI6IkluaG91c2VfUmVwb3J0Iiwicm9sZXMiOlsiU3VwZXJ1c2VyIl0sImxvZ2luIjoicHJhdmVlbl9JbmhvdXNlIiwicHJvZHVjdCI6ImVUcmFja1BsdXMiLCJkZWZhdWx0Um9sZSI6IlN1cGVydXNlciIsImhhc1JlcG9ydEFjY2VzcyI6ZmFsc2UsInNvdXJjZSI6InVpIiwiZW52aXJvbm1lbnQiOiJzdGFnZSIsImdyb3VwIjoicWFfdGVzdCIsImFwcGx5R2V0QWNsIjp0cnVlLCJpYXQiOjE3NDI1MzY2MzEsImV4cCI6MTc0MjU0MDgzMX0.WCPCPMQ73rcDkn_qcAsJTpjgZb1OOWbqjPF-GXCZDO4"
}
payload = {
    "name": "eTrackPlus",
    "model": "eeProjectsinhouse",
    "product": "eTrackPlus",
    "filters": {
        "_context.entityType": "model",
        "_context.entity": "programsTest",
        "_context.instance": "Direct Install"
    },
    "fields": [],
    "page": 1,
    "limit": 24,
    "sort": [],
    "isAggregation": False,
    "asStream": True,
    "applyMask": True,
    "mode": "view",
    "columnsMap": {
        "contextEntity": "Programs Test",
        "eeName": "Name",
        "dataLoadId": "Load Id",
        "accountNumber": "Account Number",
        "address": "Address",
        "calculatedKw": "Calculated Kw",
        "hasResubmissionRequired": "Requires Document Resubmission(s)",
        "createdBy": "Created By",
        "createdAt": "Created At",
        "updatedBy": "Updated By",
        "updatedAt": "Updated At"
    },
    "options": {
        "convertBooleanAs": "yesNo"
    },
    "queryType": "list",
    "preDefinedFilter": "allRecords"
}
req = requests.post(url=url,headers=headers, json=payload)
data={
    "data":json.dumps(req.text)
}
with open("eeee.json",'w') as file:
    json.dump(data,file, indent=4)
    print("wrotes")