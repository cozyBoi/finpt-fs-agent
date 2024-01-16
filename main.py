from lib.corpcode import corpcode
from lib.request_agent import request_agent
import os.path
import yaml

with open(os.path.dirname(__file__) + '/static/config.yaml', 'r') as file:
    config = yaml.safe_load(file)
api_key = config['api_key']

cc = corpcode()
corpInfo = cc.findWithName('삼성전자')
ra = request_agent(api_key)
ra.add_param("corp_code", corpInfo["corp_code"])
ra.add_param("bsns_year", "2023")
ra.add_param("reprt_code", "11014")
ra.add_param("idx_cl_code", "M210000")
print(ra.get("https://opendart.fss.or.kr/api/fnlttSinglIndx.json").content.decode("utf-8"))