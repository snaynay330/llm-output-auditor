import re

def extract_prompt_features(prompt: str) -> dict:
    p = prompt.lower()

    requires_json = int("json" in p or "valid json" in p or "return json" in p or "output only json" in p)
    requires_bullets = int("bullet" in p or "bullet points" in p)
    has_word_limit = int(bool(re.search(r"under\s+\d+\s+words|<=\s*\d+\s*words|exactly\s+\d+\s+words", p)))
    num_steps = len(re.findall(r"\(\d+\)|first|then|finally|do three things|do two things", p))

    # crude “constraint count”
    num_constraints = requires_json + requires_bullets + has_word_limit + int("only" in p) + int("exactly" in p) + int("no extra text" in p)

    return {
        "prompt_len_chars": len(prompt),
        "requires_json": requires_json,
        "requires_bullets": requires_bullets,
        "has_word_limit": has_word_limit,
        "num_steps": num_steps,
        "num_constraints": num_constraints,
    }
