# LM Studio Connection Plan

Goal:
Use LM Studio as the first local model backend for UltraWorkers.

Reason:
- Easier GUI than Ollama.
- Easier model management.
- Safer first step after Ollama disk-fill problems.
- OpenAI-compatible local server can be used by future UltraWorkers scripts.

Rules:
- Do not download models until disk space is checked.
- Keep C: above 100 GB free if possible.
- Absolute danger zone: below 50 GB free.
- Prefer storing models outside C: if LM Studio allows it.
- Start with one coding model only.

Future flow:
UltraWorkers script -> LM Studio local server -> local model response -> report saved to reports/

Planned first test:
Ask local model to summarize ULTRAWORKERS_OBJECTIVE.md without editing files.

Not enabled yet:
- Discord bot
- Telegram alerts
- Autonomous execution
- Trading automation
