import os, json
from dotenv import load_dotenv
from tqdm import tqdm
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

GEN_MODEL = os.getenv("GEN_MODEL", "gpt-4o-mini")

def read_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)

def write_jsonl(path, rows):
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

def generate_response(prompt: str) -> str:
    resp = client.responses.create(
        model=GEN_MODEL,
        input=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return resp.output_text

def main():
    prompts = list(read_jsonl("data/prompts.jsonl"))
    out_rows = []
    for p in tqdm(prompts, desc="Generating"):
        text = generate_response(p["prompt"])
        out_rows.append({
            "id": p["id"],
            "category": p.get("category"),
            "prompt": p["prompt"],
            "model": GEN_MODEL,
            "response": text
        })
    write_jsonl("results/responses.jsonl", out_rows)
    print("Wrote results/responses.jsonl")

if __name__ == "__main__":
    main()
