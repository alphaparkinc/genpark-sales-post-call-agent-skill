# sales-post-call-agent-skill

> **GenPark AI Agent Skill** -- Auto-transcribe analysis, CRM field mapper, and email draft writer.

## Quick Start

```python
from client import SalesPostCallClient
client = SalesPostCallClient()
res = client.analyze_transcript("Budget is an issue", "Sarah")
print(res["crm_updates"])
```
