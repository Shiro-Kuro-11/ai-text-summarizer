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

## 学習ログ（Day1〜Day4）

### Day1
- Python環境構築（venv）
- OpenAI APIキーの設定
- 最初のAPI呼び出し

### Day2
- テキストファイル入力
- 要約モードの切り替え
- 関数化

### Day3
- sys.argvによるCLI対応
- モード指定（short / long / bullet / emoji）

### Day4
- argparse対応
- --helpの自動生成
- 関数の責任分離
- 実行順・スコープの理解