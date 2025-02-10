def clarification():
    clarify = input(f"are you sure you want to delete {names[-1]} (yes or no)")
    if clarify == "yes":
        print(f"{names[-1]} has been deleted")
    else:
        print("okay, you may continue"
def get_names2():
    names=[]
    while True:
        name=input(
            "Enter a name, type 'done' to finish or 'remove' to delete the last name from the list: ")
        if name.lower() == 'remove':
            if names:
                clarification()
            else:
                print("No names to delete")
        elif name.lower() == "done":
            for name in names:
                print(name)
            break
        else:
            names.append(name)
get_names2()
