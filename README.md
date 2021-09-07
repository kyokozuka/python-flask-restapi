# How to run

## docker
今回はMysqlのみをコンテナにデプロイしています。
~~~
$ docker-compose build
$ docker-compose up -d
~~~

## マイグレーション
~~~
$ cd api
# 初期化
$ flask db init
$ flask db migrate
$ flask db upgrade

# rollbackコマンドなのでバージョン戻すときに使用
$ flask db downgrade
~~~

## python実行
~~~
$ cd api
# 仮想環境で行う場合
$ python3 -m venv venv
# mac
$ source venv/bin/activate
# win
$ .venv/Script/activate
# ライブラリのインストール
$ pip3 install -r requirements.txt
# run
$ python3 app.py
~~~