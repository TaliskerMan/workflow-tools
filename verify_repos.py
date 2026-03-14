import json
import os
import subprocess

with open("/tmp/gh_repos.json", "r") as f:
    repos = json.load(f)

base_dir = "/home/freecode/antigrav"
all_clean = True

print("Verifying repositories:\\n" + "-"*30)
for repo in repos:
    name = repo["name"]
    target_dir = os.path.join(base_dir, name)
    
    if os.path.isdir(target_dir):
        # ensure no local modifications and up to date with branch
        res = subprocess.run(["git", "status"], cwd=target_dir, capture_output=True, text=True)
        if "Your branch is up to date" in res.stdout and "nothing to commit, working tree clean" in res.stdout:
            print(f"[OK] {name} is up-to-date and clean.")
        elif "nothing to commit, working tree clean" in res.stdout and ("Your branch is behind" not in res.stdout and "have diverged" not in res.stdout):
            # sometimes the exact wording varies (like newly cloned repos might not have upstream set just right, though git clone sets it). Let's use `git status -s` and `git branch -vv`
            status_s = subprocess.run(["git", "status", "-s"], cwd=target_dir, capture_output=True, text=True).stdout
            if not status_s.strip():
                print(f"[OK] {name} is clean.")
            else:
                print(f"[WARN] {name} is not clean:\\n{status_s}")
                all_clean = False
        else:
            print(f"[WARN] {name} status issue:\\n{res.stdout}")
            all_clean = False
    else:
        print(f"[ERROR] {name} directory missing.")
        all_clean = False

print("-" * 30)
if all_clean:
    print("All repositories are confirmed up to date and clean.")
else:
    print("Some repositories have issues.")
