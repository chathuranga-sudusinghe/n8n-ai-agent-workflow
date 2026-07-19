import json
from pathlib import Path


SOURCE_FILE = Path("workflow/n8n-ai-agent-workflow.json")
OUTPUT_FILE = Path("workflow/n8n-ai-agent-workflow-public.json")


with SOURCE_FILE.open("r", encoding="utf-8") as file:
    workflow = json.load(file)


# Remove workflow-specific metadata.
for key in ["id", "versionId", "meta"]:
    workflow.pop(key, None)


# Remove node-specific private metadata and credential references.
for node in workflow.get("nodes", []):
    node.pop("id", None)
    node.pop("webhookId", None)
    node.pop("credentials", None)


with OUTPUT_FILE.open("w", encoding="utf-8") as file:
    json.dump(workflow, file, indent=2)


print(f"Sanitized workflow created: {OUTPUT_FILE}")