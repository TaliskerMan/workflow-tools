import os
import subprocess

TARGET_DIR = "/home/freecode/antigrav"

def main():
    if not os.path.isdir(TARGET_DIR):
        print(f"Error: Target directory {TARGET_DIR} does not exist.")
        return

    print("Pulling latest changes across all repositories...\n" + "-"*30)

    for item in sorted(os.listdir(TARGET_DIR)):
        repo_path = os.path.join(TARGET_DIR, item)
        if os.path.isdir(repo_path) and os.path.isdir(os.path.join(repo_path, ".git")):
            try:
                print(f"[{item}] Pulling...")
                subprocess.run(["git", "pull"], cwd=repo_path, check=True)
                print(f"[{item}] Successfully pulled.")
            except subprocess.CalledProcessError as e:
                print(f"[{item}] Error during git pull: {e}")

    print("-" * 30)
    print("All repositories processed.")

if __name__ == "__main__":
    main()
