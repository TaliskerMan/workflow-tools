import os
import subprocess
import sys

TARGET_DIR = "/Users/charlestalk/AntiGravity"

def main():
    if not os.path.isdir(TARGET_DIR):
        print(f"Error: Target directory {TARGET_DIR} does not exist.")
        return

    commit_msg = sys.argv[1] if len(sys.argv) > 1 else "Local commit for updates"

    print(f"Committing local changes across all repositories in {TARGET_DIR}...\n" + "-"*30)

    for item in sorted(os.listdir(TARGET_DIR)):
        repo_path = os.path.join(TARGET_DIR, item)
        if os.path.isdir(repo_path) and os.path.isdir(os.path.join(repo_path, ".git")):
            try:
                # Check for changes (both tracked AND untracked)
                status = subprocess.run(
                    ["git", "status", "--porcelain"],
                    cwd=repo_path,
                    capture_output=True,
                    text=True,
                    check=True
                )

                if status.stdout.strip():
                    print(f"[{item}] Changes detected. Committing...")
                    # Add all files
                    subprocess.run(["git", "add", "."], cwd=repo_path, check=True)
                    # Commit changes
                    subprocess.run(["git", "commit", "-m", commit_msg], cwd=repo_path, check=True, stdout=subprocess.DEVNULL)
                    print(f"[{item}] Successfully committed.")
                else:
                    print(f"[{item}] Clean. No changes to commit.")
                    
            except subprocess.CalledProcessError as e:
                print(f"[{item}] Error during git operations: {e}")

    print("-" * 30)
    print("All repositories processed.")

if __name__ == "__main__":
    main()
