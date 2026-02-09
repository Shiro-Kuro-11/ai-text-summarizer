import os
import argparse

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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

def summarize_text(input_file: str, mode: str):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

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

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"{prompt}\n{text}"
    )

    print("\n--- 要約結果 ---")
    print(response.output_text)


if __name__ == "__main__":
    args = parse_args()

    input_file = args.input
    mode = args.mode

    summarize_text(input_file, mode)