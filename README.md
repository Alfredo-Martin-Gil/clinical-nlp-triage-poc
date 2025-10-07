# Clinical NLP Triage (Rules-First POC)

Author: Alfredo Martín Gil, MD  
Fields: Emergency Medicine | Dialysis | AI Applied to Healthcare  
Location: Spain | Open to Remote / Toronto-ON, Canada

---

## Summary
Prototype that identifies cardiovascular red flags in short triage notes using rule-based NLP.  
Built as a transparent and PHI-free baseline to test clinical safety automation before moving to ML models.

---

## Method
- Input: synthetic triage notes (data/notes_synthetic.csv)
- Lexicon: weighted red-flag terms (data/lexicon_redflags.csv)
- Negation: ignores terms if preceded by "no", "niega" or "sin" within 4 tokens
- Scoring and risk bands:
  - HIGH ≥ 7
  - MODERATE ≥ 3
  - LOW < 3
- Output: outputs/predictions.csv (ranked by risk and score)

---

## Sample Output
| id | chief_complaint       | score | risk_band | hits                                 | triage_note                                  |
|----|-----------------------|-------|-----------|--------------------------------------|----------------------------------------------|
| 4  | chest pain            | 20    | HIGH      | arm pain; dyspnea; diaphoresis       | 58-year-old male with chest pain...          |
| 3  | shortness of breath   | 12    | HIGH      | dyspnea; chest pain; palpitations    | 66-year-old female...                        |
| 5  | syncope               | 5     | MODERATE  | ECG; syncope                         | Brief standing syncope episode...            |

---

## Quick Run (Google Colab)
``python
!unzip -q clinical-nlp-triage_step2.zip -d .
%cd clinical-nlp-triage_step2
!python scripts/score_rules.py
import pandas as pd
pd.read_csv('outputs/predictions.csv').head(10)
## Next Steps
- Add positional / pleuritic descriptors
- Temporal & uncertainty context handling
- Bilingual EN/ES pipeline using FHIR text fields

## Disclaimer
Educational proof-of-concept — uses only synthetic data.
Not intended for clinical decision making.

## Contact
Alfredo Martín Gil, MD  
LinkedIn: https://www.linkedin.com/in/alfredo-martin-gil  
GitHub: https://github.com/Alfredo-Martin-Gil
