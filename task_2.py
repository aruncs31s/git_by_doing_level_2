import json
import os

data = {"task_1": "done", "task_2": "undone"}


def check_task_1():
    try:
        with open("data.json", "r") as f:
            contents = json.load(f)
    except Exception as e:
        print(f"Error {e}")
    return contents


contents = check_task_1()
run_count = contents.get("task_2_run_count", 0)

if contents.get("task_2" , "undone")  == "done":
    print("This can only Run Once")
    exit(0)

print("Level 2".center(50, "="))
print()
print()
if run_count == 0:
    print("You will learn about the status command here")
    print("A new file is created find its name ")
    os.system("touch .gcek")
    print("The program will now exit find the file name and come back")
    contents["task_2_run_count"] = 1
    with open("data.json", "w") as f:
        json.dump(contents, f)
    exit(0)

print("Question 1:")
ans_1 = str(input("What is the name of the new file? ")).lower().strip()
if ans_1 not in ["gcek" , ".gcek"]:
    print("Wrong answer")
    print("Please read the README and try again")
    print("You need to check the for the unstaged files")
    exit(0)

print("Task 2 Completed ".center(50, "="))
print("Now run Task 3")
contents["task_2"] = "done"
contents["task_2_run_count"] = run_count + 1
with open("data.json", "w") as f:
        json.dump(contents, f)
exit(0)