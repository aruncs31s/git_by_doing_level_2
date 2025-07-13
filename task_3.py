import json
import os
import subprocess
import random 



data = {"task_3": { "password": "Null" , "run_count": 0 , "status": "undone" }}

try:
    with open("data.json", "r") as f:
        try:
            contents = json.load(f)
        except Exception as e:
            contents = data
except:
    contents = data
    os.system('touch data.json')

run_count = contents.get("task_3", {}).get("run_count", 0)
password =  contents.get("task_3", {}).get("password", "")
if int(run_count) == 0:
    data["task_3"]["run_count"] += 1
    os.system("touch new-file")
    try:
        with open("new-file", "a") as f:
            password = random.randint(1000, 9999)
            data["task_3"]["password"] = str(password)
            f.write(f"password is {password}\n")

    except Exception as e:
        print(f"Error writing to file: {e}")
    with open("data.json", "w") as f:
        json.dump(data, f)
    os.system("git add new-file")
    os.system("rm new-file")

    print("Level 2".center(50, "="))
    print("Task 3".center(10))
    print("""
        There is a new file i have created  and staged it using git add \n
        There is password in that file find the name of the file and password from the file.
        """)
    exit(0)

print("Question 1")
ans_1 = str(input("what is the name of the file? ")).lower().strip()

if ans_1 not in ["new-file"]:
    print("Please read the README and try again")
    exit(0)

print("Correct\n")
print("Question 2")
ans_2 = str(input("what is the password ")).lower().strip()

if ans_2 != password: 
    print("Please try again")
    exit(0)


print("Correct\n")
print()
print("Task 3 Completed ".center(50, "="))
print("Now run Task 4")

contents["task_3"]["status"]= "done"
with open("data.json", "w") as f:
        json.dump(contents, f)
exit(0)