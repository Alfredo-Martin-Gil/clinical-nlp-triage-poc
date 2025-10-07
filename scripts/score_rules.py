import pandas as pd, re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
lexicon = pd.read_csv(BASE / "data" / "lexicon_redflags.csv")
notes = pd.read_csv(BASE / "data" / "notes_synthetic.csv")

def tokenize(text):
    return re.findall(r"\w+[áéíóúüñÁÉÍÓÚÜÑ-]*", text.lower())

def negated(text, term, window=4):
    tokens = tokenize(text)
    term_tokens = tokenize(term)
    for i in range(len(tokens) - len(term_tokens) + 1):
        if tokens[i:i+len(term_tokens)] == term_tokens:
            if any(t in ["no","niega","sin"] for t in tokens[max(0,i-window):i]):
                return True
    return False

def score(text):
    s = 0; hits = []
    for _, row in lexicon.iterrows():
        term = str(row["termino"]).lower()
        if term in text.lower() and not negated(text, term):
            s += int(row["peso"]); hits.append(term)
    band = "LOW"
    if s >= 7: band = "HIGH"
    elif s >= 3: band = "MODERATE"
    return s, band, ";".join(sorted(set(hits)))

rows = []
for _, r in notes.iterrows():
    s, band, hits = score(r["triage_note"])
    rows.append({"id": r["id"], "chief_complaint": r["chief_complaint"], "score": s, "risk_band": band, "hits": hits, "triage_note": r["triage_note"]})

out = pd.DataFrame(rows).sort_values(["risk_band","score"], ascending=[False, False])
out_path = BASE / "outputs" / "predictions.csv"
out.to_csv(out_path, index=False, encoding="utf-8")
print(f"Saved {out_path}")