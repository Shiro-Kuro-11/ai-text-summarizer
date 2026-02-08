# AI Text Summarizer

## Description
OpenAI APIを使った簡単なテキスト要約ツールです。
コマンドライン引数で要約モードを切り替えられます。

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
python main.py input.txt

## Usage

```bash
python main.py input.txt
python main.py input.txt short
python main.py input.txt long
python main.py input.txt bullet
python main.py input.txt emoji