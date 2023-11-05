# FastAPI+PostgreSQL on Docker
## ホスト側の環境
- NAME="Ubuntu"
- VERSION="20.04.6 LTS (Focal Fossa)"
- Docker version 20.10.25+azure-2
- docker-compose version 1.29.0
    - https://docs.docker.jp/v1.12/compose/install.html

# 手順
- PostgreSQLとApp（メイン処理）のコンテナを作成
    - docker-composeに記述
    https://qiita.com/sey323/items/a4875408a67cea6a8c52
    - すでにPostgreSQL(5432)があるとうまくいかなかった
    - ユーザーは最初postgreしかないので、postgreで必要なロール・DBを作っておく
        - postgresqlの再起動はコンテナ内だとコマンド無くてできないので、コンテナ自体を再起動する(docker restart [container-name])
    - 上記設定後、docker-compose.ymlのEnvironmentを更新する
- ホスト⇔コンテナ間のポートフォーワード「Connection reset by peeC」
    - https://qiita.com/vaporwavedog/items/b6ea4294215f1b34cc07

# Tips
## sqliteが使えない・・・
- https://copyprogramming.com/howto/sqlalchemy-and-sqlite-database-is-locked

## psycopg2のインストール
sudo apt install python3-dev libpq-dev
pip3 install psycopg2

## DBログイン
psql -h localhost -d {db_name} -U {user_name}


- 
