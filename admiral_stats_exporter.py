# Simple admiral stats exporter from kancolle-arcade.net for Python3
import requests
from datetime import datetime as dt
import os
import sys
import configparser
import json
import glob
import re
import codecs

# Read configurations
config = configparser.ConfigParser()
config.read('config.txt')
# login_id = config['login']['id']
# login_pass = config['login']['password']
login_data = config['param']['data']
output_dir = config['output']['dir']
upload_token = config['upload']['token']
# output_dir = config['output']['test_dir']
# upload_token = config['upload']['test_token']

# TOP
TOP_URL = 'https://kancolle-arcade.net/ac/'

# LOGIN
LOGIN_URL = 'https://kancolle-arcade.net/ac/api/Auth/login'

# API_BASE_URL
API_BASE_URL = 'https://kancolle-arcade.net/ac/api/'

# Param
data = login_data

# HTTP headers
headers = {
    'Content-Type' : 'application/json',
    'Host' : 'kancolle-arcade.net',
    'Referer' : 'https://kancolle-arcade.net/ac',
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:45.0) Gecko/20100101 Firefox/45.0',
    'X-Requested-With' : 'XMLHttpRequest'
}

# API URLs
API_URLS = [
    'Personal/basicInfo',
    'Area/captureInfo',
    'TcBook/info',
    'EquipBook/info',
    'Campaign/history',
    'Campaign/info',
    'Campaign/present',
    # From REVISION 2 (2016-06-30)
    'CharacterList/info',
    'EquipList/info',
    # From 2016-07-26
    'Quest/info',
    # From 2016-10-27
    'Event/info',
    # イベントの開始・終了日とイベントアイコンの表示制御フラグのみを返す
    # 'Event/hold',
    # From 2017-02-14
    'RoomItemList/info',
    # Ranking
    # 'Ranking/monthly/prev',
    # 'Ranking/monthly/current',
    # 'Ranking/total'
    # From REVISION 5 (2017-04-26)
    'BlueprintList/info'
]

# Create new directory for latest JSON files
time = dt.now()
timestamp = time.strftime('%Y%m%d_%H%M%S')
json_dir = output_dir + "/" + timestamp
os.makedirs(json_dir, exist_ok=True)

# Admiral Stats Import URL
AS_IMPORT_URL = 'https://www.admiral-stats.com/api/v1/import'
GET_FILE_TYPES_URL = 'https://www.admiral-stats.com/api/v1/import/file_types'
# User Agent for logging on www.admiral-stats.com
AS_HTTP_HEADER_UA = 'AdmiralStatsExporter-Ruby/1.6.3'

import_headers = {
    'Content-Type' : 'application/json',
    'User-Agent' : AS_HTTP_HEADER_UA,
    'Authorization':'Bearer ' + upload_token
}

# GET Session ID
s = requests.Session()
r = s.get(TOP_URL)
code = r.status_code
if code != 200:
    print('ERROR: Failed to access ' + TOP_URL + ' (status code = ' + code + ')')
else:
    # Login
    req = s.post(LOGIN_URL, data=data, headers=headers)
    code = req.status_code
    if code != 200:
        print('ERROR: Failed to login (status code = ' + code + ')')
    else:
        # Access to APIs
        for api_url in API_URLS:
            api_name = api_url.replace('/','_')
            filename = api_name + '_' + timestamp + '.json'
            file_name = json_dir + '/' + api_name + '_' + timestamp + '.json'
            res = s.get(API_BASE_URL + api_url, headers=headers).text
            f = open(file_name,'w')
            f.write(res)
            f.close()
            print('Succeeded to download ' + filename)

        # Upload exported files to Admiral Stats
        dic={'y':True,'yes':True,'n':False,'no':False}
        while True:
            try:
                inp=dic[input('APIを使ったインポート機能を使用しますか？ [Y]es/[N]o? >> ').lower()]
                break
            except:
                pass
            print('もう一度入力してください')
        if inp and upload_token:
            print('自動アップロードします')
            import_s = requests.Session()
            res = import_s.get(GET_FILE_TYPES_URL, headers = {'Authorization':'Bearer ' + upload_token})
            if res.status_code == 200:
                importable_file_types = res.text
                print('Importable file types: '+importable_file_types)
            else:
                print('ERROR: '+res.text)
                sys.exit()
            # end block
            jsonfiles = glob.glob(json_dir+'/*')
            pattern = output_dir+'/\d{8}_\d{6}/(.*)_(.*)_(.*)\.json'
            for jsonf in jsonfiles:
                m = re.search(pattern, jsonf)
                post_file_type = m.group(1)
                if post_file_type in importable_file_types:
                    post_file_time = timestamp
                    f = codecs.open(jsonf, 'r', 'utf-8')
                    data = f.read()
                    payload = json.loads(data)
                    req_url = AS_IMPORT_URL + '/' + post_file_type + '/' + post_file_time
                    req = import_s.post(req_url, headers=import_headers, data=json.dumps(payload))
                    # print(req.status_code)
                    print(req.json()['data']['message'] + ' ' + 'ファイル名:'+jsonf)
                else:
                    pass
