# admiral_stats_exporter_python
艦これアーケードのプレイデータをエクスポートするツール(Python版)
このツールはmuziyoshizさんの[muziyoshiz/admiral_stats_exporter](https://github.com/muziyoshiz/admiral_stats_exporter)をPythonに移植したものです。

# 注意事項

* このツールは非公式なツールです。本ツールの開発者は、このツールを利用することによるいかなる損害についても一切責任を負いません。

# インストール・実行方法

## インストール手順

### 1. Python のインストール

admiral_stats_exporter_pythonを動かすには、Python が必要です。

Windows ユーザで、Python をインストールしたことがない場合は、以下の手順をお勧めします。

* [Python公式サイト](https://www.python.org/) へアクセス
* Downloads > Windows > Python3.x.xを選択
* ダウンロードしたファイルを実行
* インストール中に出てくる「Add Python3.x to PATH」のチェックボックスを ON にする

### 2. admiral_stats_exporter_python のダウンロード

緑色の Clone or download ボタンを押し、Download ZIPを押してください。
ZIPファイルがダウンロードされるので、好きな場所に解凍してください。
git を使える場合は master ブランチを clone してもOKです。

### 3. 必要なライブラリのダウンロード

コマンドプロンプト、またはコンソールを開いて、admiral_stats_exporter_python を解凍したディレクトリに移動してください。
そして、以下のコマンドを実行してください。

```
pip install requests
```

### 4. config.txt の作成

config.txt.sample をコピーして、同じディレクトリに config.txt ファイルを作成してください。

そして、`SEGA_ID`, `PASSWORD`, `API_TOKEN` と書かれた箇所に、以下の情報を記入してください。

- `SEGA_ID`
    - 公式プレイヤーズサイトのログインに使った SEGA ID
- `PASSWORD`
    - 公式プレイヤーズサイトのログインに使ったパスワード
- `API_TOKEN` （※ 自動アップロード機能を使わない場合は設定不要）
    - [Admiral Stats](https://www.admiral-stats.com/) の「設定＞API トークンの設定」で確認できる API トークン

```
[login]
id = SEGA_ID
password = PASSWORD

[output]
dir = ./json

[upload]
token = API_TOKEN
```

## 実行

### エクスポートのみ実行する場合

admiral_stats_exporter.py のあるディレクトリで、以下のコマンドを実行してください。  
実行に成功すると、 `json/コマンドの実行日時` ディレクトリに、最新のプレイデータがエクスポートされます。  

```
$ python admiral_stats_exporter.py
Succeeded to download Personal_basicInfo_20170524_205108.json
Succeeded to download Area_captureInfo_20170524_205108.json
Succeeded to download TcBook_info_20170524_205108.json
Succeeded to download EquipBook_info_20170524_205108.json
Succeeded to download Campaign_history_20170524_205108.json
Succeeded to download Campaign_info_20170524_205108.json
Succeeded to download Campaign_present_20170524_205108.json
Succeeded to download CharacterList_info_20170524_205108.json
Succeeded to download EquipList_info_20170524_205108.json
Succeeded to download Quest_info_20170524_205108.json
Succeeded to download Event_info_20170524_205108.json
Succeeded to download RoomItemList_info_20170524_205108.json
Succeeded to download BlueprintList_info_20170524_205108.json
```

### エクスポート後に自動アップロードする場合

エクスポート後に、Admiral Stats へ JSON ファイルを自動アップロードしたい場合は `--upload` オプションを付けて実行してください。  
Admiral Stats の「設定＞API ログの確認」で、アップロードに成功したかどうかを確認できます。

```
$ python admiral_stats_exporter.py --upload
Succeeded to download Personal_basicInfo_20170524_205807.json
Succeeded to download Area_captureInfo_20170524_205807.json
Succeeded to download TcBook_info_20170524_205807.json
Succeeded to download EquipBook_info_20170524_205807.json
Succeeded to download Campaign_history_20170524_205807.json
Succeeded to download Campaign_info_20170524_205807.json
Succeeded to download Campaign_present_20170524_205807.json
Succeeded to download CharacterList_info_20170524_205807.json
Succeeded to download EquipList_info_20170524_205807.json
Succeeded to download Quest_info_20170524_205807.json
Succeeded to download Event_info_20170524_205807.json
Succeeded to download RoomItemList_info_20170524_205807.json
Succeeded to download BlueprintList_info_20170524_205807.json
Importable file types: ["Personal_basicInfo","TcBook_info","CharacterList_info","Event_info"]
艦娘一覧のインポートに成功しました。 (ファイル名:CharacterList_info_20170524_205807.json)
同じ意味を持つ、過去のイベント進捗情報がインポート済みのため、無視されました。 (ファイル名:Event_info_20170524_205807.json)
基本情報のインポートに成功しました。 (ファイル名:Personal_basicInfo_20170524_205807.json)
艦娘図鑑のインポートに成功しました。 (ファイル名:TcBook_info_20170524_205807.json)
```
