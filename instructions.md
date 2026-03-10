# LLM Instructions – PDD Meta Evaluator & Mainstream Prompt Library

Dieses Repository stellt Basis-Prompts bereit, um die ersten 8 PDD-Projekte zu analysieren, zu bewerten, zu erklären und zu verbessern.

Es generiert selbst keine Prompts, sondern stellt sie bereit.

## Ordnerstruktur

/prompts  
    /analysis  
    /didactic  
    /meta  

/docs  
    prompt_design_principles.md  
    metrics.md  
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
# LLM Instructions – PDD Meta Evaluator & Learning Companion (Offline)

Diese Datei definiert alles, was ein LLM benötigt, um dieses Meta-Repository vollständig zu verstehen
und die enthaltenen Prompts korrekt zu nutzen.

---

## 1. Ziel

Dieses Repository stellt Basis-Prompts bereit, um die ersten 8 PDD-Projekte zu:

- analysieren
- bewerten
- verbessern
- auf Drift prüfen
- auf Halluzinationen testen
- didaktisch erklären

Es generiert selbst **keine** Prompts, sondern stellt sie bereit.

---

## 2. Hardware Constraints

Dieses Projekt muss vollständig auf normaler Consumer-Hardware lauffähig sein:

- CPU-only
- keine GPU-Abhängigkeiten
- keine Modelle > 1 GB
- keine externen APIs oder Cloud-Dienste
- alles offline
- Python-Standardbibliothek

---

## 3. Prompt-Spezifikationen

Alle Prompts liegen im Ordner `/prompts`.

Jeder Prompt enthält:
- den Prompt selbst
- eine Dokumentation, warum er so aufgebaut ist
- Hinweise zur Anwendung
- erwartetes Verhalten eines LLMs

### 3.1 Projekt-Start-Prompt (project_start.md)
- Testet, ob ein LLM die instructions.md eines Projekts versteht.

### 3.2 Projekt-Analyse-Prompt (project_analysis.md)
- Lässt ein LLM das Projekt bewerten.

### 3.3 Drift-Check-Prompt (drift_check.md)
- Vergleicht zwei Projekte.

### 3.4 Halluzinations-Check-Prompt (hallucination_check.md)
- Prüft, ob ein LLM Dateien erfindet.

### 3.5 Verbesserungs-Prompt (improvement_suggestions.md)
- Lässt ein LLM Verbesserungsvorschläge generieren.

### 3.6 Didaktische Prompts
- explain_like_10.md  
- explain_like_junior.md  
- explain_like_senior.md  

### 3.7 Background-Story-Prompt (background_story.md)
- Erzeugt eine narrative Erklärung der Technik.

---

## 4. Evaluationsmodule

### loader.py
Lädt die Prompts.

### evaluator.py
Vergleicht LLM-Antworten mit erwarteten Strukturen.

### metrics.py
Erzeugt Scores:
- clarity
- drift risk
- hallucination risk
- didactic quality

### drift_detector.py
Vergleicht zwei Projekte.

### hallucination_detector.py
Vergleicht LLM-Antworten mit echter Repo-Struktur.

### agent.py
Orchestriert den Evaluationsprozess.

---

## 5. Tests

Alle Tests prüfen:
- ob Prompts geladen werden können
- ob Evaluationsmodule korrekt reagieren
- ob Drift- und Halluzinationsmodule baseline-fähig sind

---

## 6. Aufgaben an das LLM

Das LLM soll:

1. die Prompts korrekt interpretieren  
2. die Evaluationsmodule implementieren  
3. die Tests verstehen  
4. die Architektur nachvollziehen  

---

## 7. How-To-Use (für Code-Assistenten)

1. Öffne das Repository.  
2. Öffne einen Prompt aus `/prompts`.  
3. Sende ihn an ein LLM.  
4. Analysiere die Antwort.  
5. Nutze evaluator.py, um die Antwort zu bewerten.

Damit kann ein LLM die ersten 8 Projekte analysieren, bewerten und verbessern.
