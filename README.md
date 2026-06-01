# AgentForge Local AI Software Factory

AgentForge is a local-first AI worker framework for planning, coding, testing, reviewing, documenting, and preparing publishable projects while staying controlled by objective files, approval gates, and Git checkpoints.

## Current Status

Phase 0 foundation is active.

Built so far:
- Objective file
- Rules file
- Roadmap file
- Agent roles file
- Approval gates file
- Project registry
- Task intake format
- Task safety checker
- Status checker
- Pre-run checker
- Task creator

## Core Commands

Show current mission:
python scripts/show_mission.py

Show system status:
python scripts/status.py

Run full pre-check:
python scripts/run_check.py

Create a new task:
python scripts/create_task.py "AgentForge" "Task title" "Task objective"

Check a task:
python scripts/check_task.py tasks/example_task.json

## Safety Model

AgentForge starts with protected boundaries:
- AgentForge can edit itself during foundation building.
- Trading AI Terminal is registered but protected.
- High-risk actions require approval.
- Git checkpoints are required before major work.
- No live trading automation is allowed.
