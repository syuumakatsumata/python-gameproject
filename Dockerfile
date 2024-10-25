# Python 3.9の公式イメージを使用
FROM python:3.9-slim

# 作業ディレクトリを /app に設定
WORKDIR /app

# requirements.txt をコンテナにコピー
COPY requirements.txt .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクト全体をコンテナにコピー
COPY . .

# ポートの指定（もしWebアプリなら必要です）
# EXPOSE 5000  # 例: Flaskアプリの場合

# デフォルトで実行するコマンド
CMD ["python", "main.py"]
