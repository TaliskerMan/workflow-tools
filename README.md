# Workflow Tools

A collection of helper scripts to manage development workflows across machines.

## Scripts

| Script | Description |
|---|---|
| `save_work.py` | Log your session progress and push updates to your plan file |
| `init_plans.py` | Initialize `plan/AppNamePlan.md` in all repositories |
| `sync_repos.py` | Clone or pull all GitHub repositories to your local machine |

## Setup

Clone this repository and run the setup script:

```bash
cd /home/freecode/antigrav
git clone https://github.com/TaliskerMan/workflow-tools.git
cd workflow-tools
chmod +x setup_env.sh
./setup_env.sh
source ~/.bashrc
```

## Usage

- **`save_work`** — Run from inside any repository to log what you accomplished and what's next. Commits and pushes the plan file.
- **`init_plans`** — Run once to create `plan/AppNamePlan.md` in all repositories under `/home/freecode/antigrav`.
- **`sync_repos`** — Clone missing repositories and pull updates for existing ones.

## License

GNU GPL v3 — Chuck Talk
