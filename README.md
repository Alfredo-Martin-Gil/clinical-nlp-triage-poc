# clinical-nlp-triage (rules-first POC)
POC educativo sin PHI para detectar *red flags* cardiovasculares en notas de triaje.
- Datos: `data/lexicon_redflags.csv`, `data/notes_synthetic.csv`
- Código: `scripts/score_rules.py` (negación básica, ventana 4 tokens)
- Salida: `outputs/predictions.csv`
Uso: `python scripts/score_rules.py`
Última actualización: 2025-10-07
