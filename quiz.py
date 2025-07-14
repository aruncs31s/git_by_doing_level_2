#!/usr/bin/env python3

"""
If you found self here , this a just a python script using only the print and input functions.
"""
score = 0
count = 0


def main():

    global score
    global count
    print("Level 2".center(50, "="))
    print()

    should_continue = input("Did you finish reading README (y/N): ").lower().strip()

    if should_continue not in ["y", "yes"]:
        print("Please read the README".center(50))
        return
    score += 1
    count += 1
    print(f"\nScore {score} / {count}")

    print("Question 1:")
    print("Imaigine you created a new file called update.sh .")
    print("Which command would you use to add that to staging area? ")
    print()

    ans_1 = input("Please enter the command: ").lower().strip()

    if ans_1 not in ["git add", "add"]:
        print("Incorrect! Please read level_0 again.")
        return

    print("Correct!")
    score += 1
    count += 1
    print(f"Score {score} / {count}")
    print()

    print("Question 2:")
    print("Imagine you've created multiple files in you git directory:")
    ans_2 = input("Which option is used to add multiple files? ").strip()

    if ans_2 not in ["-A", "A", "git add -A"]:
        print("Incorrect! Please READ the README.")
        return

    print("Correct!")
    score += 1
    count += 1
    print(f"\nScore {score} / {count}")
    print()

    print("Question 3:")
    print("Imagine you added a file text.txt")
    print("But you accidently deleted that some point ")

    ans_3 = input("Which command can be used to recover that file? ").lower().strip()

    if ans_3 not in ["git restore" , "restore"]:
        print("Incorrect! Read the README again.")
        return

    print("Correct!")
    score += 1
    count += 1
    print(f"\nScore {score} / {count}")
    print()
    print(" Level 2 Completed ".center(50 , "="))

if __name__ == "__main__":
    main()