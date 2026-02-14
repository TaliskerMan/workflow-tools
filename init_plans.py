import os

TARGET_DIR = "/home/freecode/antigrav"

def init_plans():
    print(f"Scanning {TARGET_DIR} for repositories...")
    
    for item in os.listdir(TARGET_DIR):
        item_path = os.path.join(TARGET_DIR, item)
        
        # Only process directories that are git repositories
        if os.path.isdir(item_path) and os.path.exists(os.path.join(item_path, ".git")):
            repo_name = item
            plan_dir = os.path.join(item_path, "plan")
            plan_file = os.path.join(plan_dir, f"{repo_name}Plan.md")
            
            # Create plan directory
            if not os.path.exists(plan_dir):
                print(f"Creating plan directory for {repo_name}...")
                os.makedirs(plan_dir)
            
            # Create plan file if it doesn't exist
            if not os.path.exists(plan_file):
                print(f"Creating plan file: {plan_file}")
                with open(plan_file, "w") as f:
                    f.write(f"# {repo_name} Plan\n\n")
                    f.write("## Work Log\n\n")
                    f.write("- [ ] Initial plan creation.\n")
            else:
                print(f"Plan file already exists for {repo_name}.")

if __name__ == "__main__":
    init_plans()
