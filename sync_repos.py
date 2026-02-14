import subprocess
import os
import json

TARGET_DIR = "/home/freecode/antigrav"

def get_repos():
    print("Fetching repository list...")
    try:
        result = subprocess.run(
            ["gh", "repo", "list", "--limit", "1000", "--json", "name,url"],
            capture_output=True,
            text=True,
            check=True
        )
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error fetching repositories: {e}")
        print(e.stderr)
        return []

def sync_repo(repo):
    name = repo['name']
    url = repo['url']
    repo_path = os.path.join(TARGET_DIR, name)

    if os.path.isdir(repo_path):
        print(f"Updating {name}...")
        try:
            # Check if it's actually a git repo before pulling
            if os.path.isdir(os.path.join(repo_path, ".git")):
                subprocess.run(["git", "-C", repo_path, "pull"], check=True)
            else:
                print(f"Skipping {name}: Directory exists but is not a git repository.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to pull {name}: {e}")
    else:
        print(f"Cloning {name}...")
        try:
            subprocess.run(["git", "clone", url, repo_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to clone {name}: {e}")

def main():
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
    
    print(f"Syncing repositories to {TARGET_DIR}")
    repos = get_repos()
    print(f"Found {len(repos)} repositories.")
    
    for repo in repos:
        sync_repo(repo)

if __name__ == "__main__":
    main()
