# CLI entry point for AI text summarizer

# =========================
# 1. 標準ライブラリ
# =========================
import os
import argparse
import logging

# =========================
# 2. サードパーティライブラリ
# =========================
from openai import OpenAI
from dotenv import load_dotenv


# =========================
# 3. 定数・設定
# =========================
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

# =========================
# 4. グローバル初期化
# =========================
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    logging.error("OPENAI_API_KEY が設定されていません")
    exit(1)

client = OpenAI(api_key=api_key)

# =========================
# 5. 関数定義
# =========================
def parse_args():
    parser = argparse.ArgumentParser(
        description="Summarize text using OpenAI API"
    )

    parser.add_argument(
        "input",
        help="Input text file path"
    )

    parser.add_argument(
        "-m", "--mode",
        choices=["normal", "short", "long", "bullet", "emoji"],
        default="normal",
        help="Summary mode (default: normal)"
    )

    return parser.parse_args()

def summarize_text(text: str, mode: str):
    logging.info(f"要約を開始します (mode={mode})")

    prompt = "次の文章を日本語で要約してください。"

    if mode == "short":
        prompt = "次の文章を一文で日本語要約してください。"
    elif mode == "long":
        prompt = "次の文章を丁寧に日本語で要約してください。"
    elif mode == "bullet":
        prompt = "次の文章を日本語で箇条書き3点にまとめてください。"
    elif mode == "emoji":
        prompt = "次の文章を絵文字を使って楽しく日本語要約してください。"
    else:
        prompt = "次の文章を日本語で要約してください。"

    try:
        response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"{prompt}\n{text}"
    )
    except Exception as e:
        logging.error("OpenAI APIの呼び出しに失敗しました")
        logging.error(e)
        exit(1)

    logging.info("要約が完了しました")

    return response.output_text

# =========================
# 6. エントリーポイント
# =========================
if __name__ == "__main__":
    args = parse_args()

    input_file = args.input
    mode = args.mode

    logging.info(f"入力ファイル: {input_file}")

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
        if not text.strip():
            logging.error("入力ファイルが空です")
            exit(1)
    except FileNotFoundError:
        logging.error(f"ファイルが見つかりません: {input_file}")
        exit(1)

    summary = summarize_text(text, mode)
    print("\n--- 要約結果 ---")
    print(summary)

    name, ext = os.path.splitext(input_file)
    output_file = f"{name}_summary.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(summary)

    logging.info(f"{output_file} に保存しました")