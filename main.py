from lib.corpcode import corpcode
from lib.request_agent import request_agent
import os.path
import yaml
import json

with open(os.path.dirname(__file__) + '/static/config.yaml', 'r') as file:
    config = yaml.safe_load(file)
api_key = config['api_key']

cc = corpcode()
corpInfo = cc.findWithName('삼성전자')
ra = request_agent(api_key)
ra.add_param("corp_code", corpInfo["corp_code"])
ra.add_param("bsns_year", "2023")
ra.add_param("reprt_code", "11013")
ra.add_param("fs_div", "CFS")
jsonData = ra.get("https://opendart.fss.or.kr/api/fnlttSinglAcntAll.json").content.decode("utf-8")
json_object = json.loads(jsonData)

if json_object['status'] == '000':
    fss = []
    for elem in json_object['list']:
        fs = {}
        fs['fs_type'] = elem['account_nm']
        fs['fs_detail'] = elem['account_detail']
        fs['amount'] = elem['thstrm_amount']
        fss.append(fs)

    print(fss)