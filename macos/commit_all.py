import os
import subprocess

TARGET_DIR = "/Users/charlestalk/AntiGravity"
COMMIT_MSG = "Save artifacts and plans"

def main():
    if not os.path.isdir(TARGET_DIR):
        print(f"Error: Target directory {TARGET_DIR} does not exist.")
        return

    print("Committing and pushing across all repositories...\n" + "-"*30)

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
                    print(f"[{item}] Changes detected. Committing and pushing...")
                    # Add all files
                    subprocess.run(["git", "add", "."], cwd=repo_path, check=True)
                    # Commit changes
                    subprocess.run(["git", "commit", "-m", COMMIT_MSG], cwd=repo_path, check=True, stdout=subprocess.DEVNULL)
                    # Push changes
                    subprocess.run(["git", "push"], cwd=repo_path, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    print(f"[{item}] Successfully committed and pushed.")
                else:
                    print(f"[{item}] Clean. No changes to commit.")
                    
            except subprocess.CalledProcessError as e:
                print(f"[{item}] Error during git operations: {e}")

    print("-" * 30)
    print("All repositories processed.")

if __name__ == "__main__":
    main()
