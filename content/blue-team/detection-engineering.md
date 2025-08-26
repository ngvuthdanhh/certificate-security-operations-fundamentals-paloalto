# Detection Engineering Notes

## Pipeline
Collect → Normalize → Enrich → Correlate → Alert → Triage → Case

## Rule design
- Hypothesis-driven; map to ATT&CK
- Detection logic + FP scenarios + suppression strategy
- Test data; QA checklist; version control

## Examples (pseudo)
- "Multiple failed logins followed by success from new ASN within 10m"
- "Sensitive process spawning script interpreter + network to rare domain"
