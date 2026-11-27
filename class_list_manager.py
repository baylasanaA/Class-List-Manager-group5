# Class List Manager - Group 5
# MIS 211 Bonus Assignment (GitHub Teamwork)
names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]

# ===== Each student adds her function BELOW this line =====
# Written by: Baylasan (task 1)
def count_names(names):
    return len(names)

# Written by: Jana (task 2)
def search_name(names, name):
    return name in names

# Written by: Kawthar (task 3)
def sort_names(names):
    return sorted(names)

# Written by: Noura (task 4)
def names_starting_with(names, letter):
    return [name for name in names if name.lower().startswith(letter.lower())]

# Written by: Joury (task 6)
def to_upper(names):
    result = []
    for name in names:
        result.append(name.upper())
    return result
    
def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    # Each student calls her function here, for example:
    print("Number of names:", count_names(names))
‏    print("Search Sara:", search_name(names, "Sara"))
    print("Sorted names:", sort_names(names))
    print("Names starting with L:", names_starting_with(names, "L"))
    print("Uppercase names:", to_upper(names))





main()
