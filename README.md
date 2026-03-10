# PDD Meta Evaluator & Mainstream Prompt Library

Dieses Repository ist die zentrale Prompt‑, Analyse‑ und Bewertungsbibliothek für die ersten 8 PDD‑Projekte.

Es enthält:
- eine Mainstream Prompt Library
- wissenschaftlich motivierte Metriken
- Drift‑ und Halluzinations‑Analyse
- didaktische Erklärungs‑Prompts (10 Jahre, Junior, Senior)
- Background‑Story‑Prompts
- Projekt‑Start‑ und Projekt‑Analyse‑Prompts
- Evaluationsmodule
- Tests

Dieses Repository ist das methodische Fundament der PDD‑Serie.

Dieses Repository generiert selbst **keine** Prompts, sondern stellt sie bereit.

## Ziele

- LLMs testen
- Drift erkennen
- Halluzinationen sichtbar machen
- Feedback generieren
- Didaktische Erklärungen ermöglichen
- PDD-Projekte auf LLM-Readiness prüfen

## Projektstruktur

/prompts  
    project_start.md  
    project_analysis.md  
    drift_check.md  
    hallucination_check.md  
    improvement_suggestions.md  
    explain_like_10.md  
    explain_like_junior.md  
    explain_like_senior.md  
    background_story.md  

/docs  
    prompt_design_principles.md  
    architecture.md  

/src  
    loader.py  
    evaluator.py  
    metrics.py  
    drift_detector.py  
    hallucination_detector.py  
    agent.py  

/tests  
    test_prompts.md  
    test_evaluator.md  
    test_metrics.md  
    test_drift_detector.md  
    test_hallucination_detector.md  

hardware-requirements.md  
instructions.md  
README.md  
credits.md

## Hardware Requirements

Dieses Projekt ist vollständig lokal ausführbar und benötigt keine spezielle Hardware.
Siehe `hardware-requirements.md`.

## Lizenz

MIT License.

## Credits

Siehe `credits.md`.
