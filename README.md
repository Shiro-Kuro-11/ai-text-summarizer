# AI Text Summarizer

## これは何？
OpenAI API を使って、テキストファイルの内容を要約する Python スクリプトです。
venv（仮想環境）を使い、プロジェクトごとに依存関係を分離しています。

## 使っている技術
- Python 3.x
- OpenAI API
- python-dotenv
- venv（仮想環境）

## 実行手順
```bash
# 初回のみ
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt

# 毎回
venv\Scripts\activate
python main.py
