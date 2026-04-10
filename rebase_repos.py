import os
import subprocess
import sys

TARGET_DIR = "/home/freecode/antigrav"

def main():
    if not os.path.isdir(TARGET_DIR):
        print(f"Error: Target directory {TARGET_DIR} does not exist.")
        return

    branch = sys.argv[1] if len(sys.argv) > 1 else "main"

    print(f"Rebasing all repositories onto origin/{branch}...\n" + "-"*30)

    for item in sorted(os.listdir(TARGET_DIR)):
        repo_path = os.path.join(TARGET_DIR, item)
        if os.path.isdir(repo_path) and os.path.isdir(os.path.join(repo_path, ".git")):
            try:
                print(f"[{item}] Fetching and rebasing...")
                subprocess.run(["git", "fetch"], cwd=repo_path, check=True)
                subprocess.run(["git", "rebase", f"origin/{branch}"], cwd=repo_path, check=True)
                print(f"[{item}] Successfully rebased.")
            except subprocess.CalledProcessError as e:
                print(f"[{item}] Error during git rebase: {e}")
                print(f"[{item}] Aborting rebase...")
                subprocess.run(["git", "rebase", "--abort"], cwd=repo_path)

    print("-" * 30)
    print("All repositories processed.")

if __name__ == "__main__":
    main()
