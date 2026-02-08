import pandas as pd

def main():
    df = pd.read_csv("results/merged_for_analysis.csv")

    total = len(df)
    pass_rate = (df["failure_type"] == "pass").mean()
    top_failures = df[df["failure_type"] != "pass"]["failure_type"].value_counts().head(5)

    worst = df.sort_values(["instruction_following","helpfulness","clarity"]).head(5)[
        ["id","category","failure_type","severity","instruction_following","helpfulness","clarity","prompt"]
    ]

    by_constraints = pd.read_csv("results/failure_rate_by_constraints.csv")

    lines = []
    lines.append("# LLM Output Audit Report\n")
    lines.append(f"- Total prompts audited: **{total}**\n")
    lines.append(f"- Pass rate: **{pass_rate:.0%}**\n\n")

    lines.append("## Top Failure Types\n")
    for k, v in top_failures.items():
        lines.append(f"- **{k}**: {v}\n")
    lines.append("\n")

    lines.append("## Failure Rate vs Prompt Constraints\n")
    lines.append(by_constraints.to_markdown(index=False))
    lines.append("\n\n")

    lines.append("## Worst Cases (Lowest Scores)\n")
    lines.append(worst.to_markdown(index=False))
    lines.append("\n")

    with open("results/summary_report.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("Wrote results/summary_report.md")

if __name__ == "__main__":
    main()
