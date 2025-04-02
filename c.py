import requests
import zipfile,os 
import pandas as pd
import shutil,json
from bs4 import BeautifulSoup
from datetime import datetime

token = "LwzK5VMfg-MfyRHBJ8Nx"

url = "https://gitlab.anbetrack.com/api/v4/projects/5152/jobs/artifacts/master/download?job=stage_regression_python_tests"

headers = {
    'Authorization': 'Bearer '+ token
}
response = requests.get(url, headers=headers, verify=False)

print(response.status_code)
with open("praveen2.zip",'wb') as file:
    file.write(response.content)

extract_folder = "praveen2"

 if not os.path.exists(extract_folder):
     os.makedirs(extract_folder)
 with zipfile.ZipFile('praveen2.zip','r') as file:
     file.extractall(extract_folder)

try:
    d = os.listdir(extract_folder)
except Exception as e:
    print(str(e))
c=[]
for i in os.listdir(''.join(d)):
    if i.endswith('.html'):
        c.append(i)
print("extract folder", extract_folder)
print(extract_folder)


all_data=[]
ed = [i for i in os.listdir('reports') if i.endswith('.html')]
for i in ed:
    dirName = os.path.join(os.path.dirname(__file__),'reports',i)
    with open(dirName,'r',encoding='utf-8') as file:
        d = file.read()
    soup = BeautifulSoup(d, "html.parser")
    table = soup.find("table")
     print(table)
    df = pd.read_html(str(table))[0]
    aa = i.split('_')[-1]
    author_name = aa.split('.')[0]
    date = datetime.now()
    f = date.strftime('%m-%d-%Y')
    df['author']=author_name
    df['date']=f
    all_data.append(df)
combined_values = pd.concat(all_data,ignore_index=True)
combined_values.to_excel('API report generation(1).xlsx',index=False,engine='openpyxl')

if extract_folder:
    if os.path.exists(extract_folder) and os.path.isdir(extract_folder):
        shutil.rmtree(extract_folder)
    else:
        print("file not found")


