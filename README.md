# AI Text Summarizer (CLI)

## 概要
OpenAI API を使用して、テキストファイルの内容を要約する
Python製のCLIツールです。

コマンドラインから入力ファイルと要約モードを指定することで、
用途に応じた要約結果を取得できます。

## 機能

- テキストファイルを入力として要約を生成
- 複数の要約モードに対応
  - normal（通常）
  - short（一文要約）
  - long（丁寧な要約）
  - bullet（箇条書き）
  - emoji（絵文字付き）
- 要約結果を標準出力とファイルに保存
- エラー発生時のログ出力

## 使っている技術
- Python
- OpenAI API
- argparse
- logging
- python-dotenv

## 使い方

### 事前準備

OpenAI APIキーを環境変数に設定してください。

```bash
export OPENAI_API_KEY=your_api_key

## 実行手順
```bash
# 初回のみ
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt

# 実行方法
python main.py input.txt

## モード指定（コピペで動きます）

python main.py input.txt --mode short
python main.py input.txt --mode long
python main.py input.txt --mode bullet
python main.py input.txt --mode emoji

出力例：
--- 要約結果 ---
今日はAIエンジニアを目指して勉強を始め、PythonでOpenAIのAPIを使って
AIと対話できた。エラーもあったが、一つずつ原因を調べて解決した。

## 学習ポイント

- PythonによるCLIツールの作成方法
- argparse を用いたコマンドライン引数処理
- OpenAI API の基本的な使い方
- logging を用いたログ出力
- 処理の責務分離（CLI処理と要約ロジックの分離）

## 学習ログ（Day1〜Day4）

### Day1()
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

### Day5
- loggingによるログ出力（INFO / ERROR）
- try / except を使った例外処理
- ファイル未存在・API失敗時のエラーハンドリング
- 要約結果のファイル保存（output.txt）
- 実務を意識したCLIツール改善

## Day6
- if文が何を確認しているかの理解
- if x: は bool(x) を見ていると理解
- None は False 扱いになることを確認
- 空文字 "" も False 扱いになることを確認
- if x is None と if x の違いを理解

## Day7
- OPENAI_API_KEY の存在チェックを追加（未設定時はエラー終了）
- 入力ファイルが空の場合のエラーハンドリングを追加
- 出力ファイル名を自動生成（input_summary.txt形式）
- os.path.splitext を使用してファイル名と拡張子を分離

## Day8
- 入力ファイル読み込み処理を read_input_file 関数に分離
- main の処理フローを整理（処理と実行部分を分離）
- 関数化後の動作確認とエラー修正（タイポ修正含む）

## Day9
- -o / --output オプションを追加し、出力ファイル名を指定可能に
- 出力ファイルが未指定の場合、自動で _summary.txt を付与する処理を実装
- 既存ファイルがある場合に上書きしないよう、os.path.exists() と while を用いた連番付与処理を追加
- 保存処理の動作確認（複数回実行テスト）