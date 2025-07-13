import json
import os
import subprocess

os.system("touch add_me")
data = {"task_1": "undone"}
try:
    with open("data.json", "r") as f:
        contents = json.load(f)
except Exception as e:
    # print(f"Error {e}")
    contents = data

if contents["task_1"].strip() == "done":
    print("This can only Run Once")
    exit(0)


print("Level 2".center(50, "="))

print()
print(
    """
You will learn about the add subcommand here 
"""
)

print("Task".center(50, "="))
print(
    """
There is a file named add_me in this folder add that to git using  git add \n
The format is like $ git add file_name 

"""
)
print()


print("Question 1: ")
ans_1 = str(input("Did you add it (y/N) ? ")).lower().strip()

if ans_1 not in ["y", "yes"]:
    print("Please add that file and continue")
    exit(0)


if ans_1 in ["y", "yes"]:

    result = subprocess.run(
        ["git", "ls-files", "--others", "--exclude-standard"],
        stdout=subprocess.PIPE,
        text=True,
    )
    untracked_files = result.stdout.strip().split("\n") if result.stdout else []
    if "add_me" in untracked_files:
        print("Please add that file and continue")
        exit(0)


print("")
print("Task 1 Completed Run Task 2".center(50, "="))

data["task_1"] = "done"

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
