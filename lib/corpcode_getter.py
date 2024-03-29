from request_agent import request_agent
import io
import zipfile
import yaml
import os.path

with open(os.path.dirname(__file__) + '/../static/config.yaml', 'r') as file:
    config = yaml.safe_load(file)
api_key = config['api_key']
url = config['url']

ra = request_agent(api_key)
res = ra.get(url)
if res.status_code == 200:
    with zipfile.ZipFile(io.BytesIO(res.content)) as z:
        z.extractall(os.path.dirname(__file__) + "/../static/")
        print("success")
else:
    print("failed")

