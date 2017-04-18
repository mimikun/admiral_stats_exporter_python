# admiral_stats_exporter_python
艦これアーケードのプレイデータをエクスポートするツール(Python版)
このツールはmuziyoshizさんの[muziyoshiz/admiral_stats_exporter](https://github.com/muziyoshiz/admiral_stats_exporter)をPythonに移植したものです。

# 注意事項

* このツールは非公式なツールです。本ツールの開発者は、このツールを利用することによるいかなる損害についても一切責任を負いません。

# インストール・実行方法

## インストール手順

### 1. Python のインストール

Python3以上をインストールしてください。Python2では動きません。

### 2. 必要なライブラリのダウンロード

pipなどで`requests`と`PyYaml`を入れてください。

### 3. config.yaml の作成

config.yaml.sample をコピーして、同じディレクトリに config.yaml ファイルを作成してください。

そして、`SEGA_ID`, `PASSWORD`, `API_TOKEN` と書かれた箇所に、以下の情報を記入してください。
`API_TOKEN`を使った自動アップロード機能は後日実装予定です。

- `SEGA_ID`
    - 公式プレイヤーズサイトのログインに使った SEGA ID
- `PASSWORD`
    - 公式プレイヤーズサイトのログインに使ったパスワード
- `API_TOKEN` （※ 自動アップロード機能を使わない場合は設定不要）
    - [Admiral Stats](https://www.admiral-stats.com/) の「設定＞API トークンの設定」で確認できる API トークン

```
login:
  id: SEGA_ID
  password: PASSWORD
output:
  dir: ./json
upload:
  token: API_TOKEN
```

### 4. ソースコードを編集

admiral_stats_exporter.py を開いて、`#param`の`SEGA_ID`、`PASSWORD`と書かれたところに、`config.yaml`で記入したものと同じ`SEGA_ID`、`PASSWORD`を記入してください。

```
# Param
data="{\"id\":\"SEGA_ID\",\"password\":\"PASSWORD\"}"
```

## 実行

### エクスポートのみ実行する場合

admiral_stats_exporter.py のあるディレクトリで、以下のコマンドを実行してください。  
実行に成功すると、 `json/コマンドの実行日時` ディレクトリに、最新のプレイデータがエクスポートされます。  

```
$ python admiral_stats_exporter.py
Succeeded to download Personal_basicInfo_20170309_222344.json
Succeeded to download Area_captureInfo_20170309_222344.json
Succeeded to download TcBook_info_20170309_222344.json
Succeeded to download EquipBook_info_20170309_222344.json
Succeeded to download Campaign_history_20170309_222344.json
Succeeded to download Campaign_info_20170309_222344.json
Succeeded to download Campaign_present_20170309_222344.json
Succeeded to download CharacterList_info_20170309_222344.json
Succeeded to download EquipList_info_20170309_222344.json
Succeeded to download Quest_info_20170309_222344.json
Succeeded to download Event_info_20170309_222344.json
Succeeded to download RoomItemList_info_20170309_222344.json
```

### エクスポート後に自動アップロードする場合

後日実装予定です。
