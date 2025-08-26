# Common Playbooks (Templates)

## Suspicious Login
- **Trigger**: Impossible travel / unfamiliar location
- **Enrichment**: Geo, ASN, device, MFA status
- **Decide**: Reset password? MFA challenge? Session revoke
- **Contain**: Disable account (if high risk), notify user
- **Lessons**: Tuning conditions; add device profiling

## Malware on Endpoint
- **Trigger**: EDR quarantine / high-sev alert
- **Enrichment**: Hash VT score, prevalence, process tree
- **Contain**: Network isolate, kill proc, block hash/domain
- **Collect**: Triage package; volatile data
