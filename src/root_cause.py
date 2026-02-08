import json
import pandas as pd
from src.features import extract_prompt_features


def read_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]

def main():
    responses = read_jsonl("results/responses.jsonl")
    audits = read_jsonl("results/audits.jsonl")

    df_r = pd.DataFrame(responses)[["id","prompt","category","model"]]
    df_a = pd.DataFrame(audits)[["id","failure_type","severity","instruction_following","helpfulness","clarity"]]
    df = df_r.merge(df_a, on="id", how="inner")

    feats = df["prompt"].apply(extract_prompt_features).apply(pd.Series)
    df = pd.concat([df, feats], axis=1)

    df["failed"] = (df["failure_type"] != "pass").astype(int)

    by_constraints = df.groupby("num_constraints")["failed"].mean().reset_index().sort_values("num_constraints")
    by_category = df.groupby("category")["failed"].mean().reset_index().sort_values("failed", ascending=False)
    severity_dist = df["severity"].value_counts().reset_index()
    severity_dist.columns = ["severity","count"]

    df.to_csv("results/merged_for_analysis.csv", index=False)
    by_constraints.to_csv("results/failure_rate_by_constraints.csv", index=False)
    by_category.to_csv("results/failure_rate_by_category.csv", index=False)
    severity_dist.to_csv("results/severity_distribution.csv", index=False)

    print("Wrote results/merged_for_analysis.csv and summary CSVs")

if __name__ == "__main__":
    main()
