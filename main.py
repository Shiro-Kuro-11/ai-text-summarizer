from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ファイルを読む
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

prompt = f"""
以下の文章を、
・箇条書き
・重要なポイント3つ
・エンジニア志望向け
で要約してください。

{text}
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print("\n--- 要約結果 ---")
print(response.output_text)