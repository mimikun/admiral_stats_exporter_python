# Simple admiral stats exporter from kancolle-arcade.net for Python3
import requests
from datetime import datetime as dt
import os
import sys
import configparser
# import yaml

# Read configurations
config = configparser.ConfigParser()
config.read('config.txt')
login_id = config['login']['id']
login_pass = config['login']['password']
output_dir = config['output']['dir']
upload_token = config['upload']['token']
login_data = config['param']['data']

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
]

# Create new directory for latest JSON files
time = dt.now()
timestamp = time.strftime('%Y%m%d_%H%M%S')
json_dir = output_dir + "/" + timestamp
os.makedirs(json_dir, exist_ok=True)


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
            filename = api_name + timestamp + '.json'
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
            print('インポートします')
            #ココ以降に処理を書く
