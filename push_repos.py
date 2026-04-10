import os
import subprocess

TARGET_DIR = "/home/freecode/antigrav"

def main():
    if not os.path.isdir(TARGET_DIR):
        print(f"Error: Target directory {TARGET_DIR} does not exist.")
        return

    print("Pushing local changes across all repositories...\n" + "-"*30)

    for item in sorted(os.listdir(TARGET_DIR)):
        repo_path = os.path.join(TARGET_DIR, item)
        if os.path.isdir(repo_path) and os.path.isdir(os.path.join(repo_path, ".git")):
            try:
                # We can just attempt push if tracked or just check ahead. Let's just do a simple push.
                print(f"[{item}] Pushing...")
                subprocess.run(["git", "push"], cwd=repo_path, check=True, capture_output=True, text=True) # or without capture_output
                print(f"[{item}] Successfully pushed.")
            except subprocess.CalledProcessError as e:
                # It might say everything up to date, which is ok, but a failure usually means rejected.
                # Actually, git push might return 0 even if "Everything up-to-date", and might write to stderr.
                if "Everything up-to-date" in e.stderr if hasattr(e, 'stderr') and e.stderr else "":
                     print(f"[{item}] Already up to date.")
                else:
                     print(f"[{item}] Error during git push / or already up to date: {e}")

    print("-" * 30)
    print("All repositories processed.")

if __name__ == "__main__":
    main()
