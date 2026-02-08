# LLM Output Audit Report

- Total prompts audited: **30**

- Pass rate: **67%**


## Top Failure Types

- **instruction_violation**: 9

- **non_answer_or_partial**: 1



## Failure Rate vs Prompt Constraints

|   num_constraints |    failed |
|------------------:|----------:|
|                 0 | 0.0714286 |
|                 1 | 0.666667  |
|                 2 | 0.5       |
|                 3 | 0         |



## Worst Cases (Lowest Scores)

| id   | category    | failure_type          | severity   |   instruction_following |   helpfulness |   clarity | prompt                                                                                              |
|:-----|:------------|:----------------------|:-----------|------------------------:|--------------:|----------:|:----------------------------------------------------------------------------------------------------|
| p07  | length_50   | instruction_violation | medium     |                       1 |             3 |         4 | Explain overfitting in machine learning in under 50 words.                                          |
| p08  | length_50   | instruction_violation | medium     |                       1 |             3 |         4 | Summarize the plot of Cinderella in under 50 words.                                                 |
| p26  | length_50   | instruction_violation | medium     |                       1 |             3 |         4 | In under 50 words, explain what an API is.                                                          |
| p09  | length_30   | instruction_violation | medium     |                       2 |             3 |         4 | Define 'SQL join' in under 30 words.                                                                |
| p03  | format_json | instruction_violation | medium     |                       2 |             4 |         4 | Output ONLY valid JSON with keys: pros (array), cons (array), verdict (string) about electric cars. |

