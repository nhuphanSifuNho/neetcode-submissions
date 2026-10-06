from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    cur_student = scores[0][0]
    cur_max = scores[0][1]
    for student, score in scores:
        if cur_max < score:
            cur_max = score
            cur_student = student
    return cur_student



# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))



# To access a student's score using their name from a list of tuples, you have two primary options: convert it to a dictionary for instant lookups, or loop through the list to find a match.
# ## Method 1: Convert to a Dictionary (Recommended)
# If you need to look up scores multiple times, the most efficient and Pythonic way is to convert the list of tuples into a dict. Python automatically treats the first element of the tuple as the key (name) and the second as the value (score).

# students = [("Alice", 90), ("Bob", 80), ("Charlie", 70)]
# # 1. Convert the list of tuples to a dictionarystudent_dict = dict(students)
# # 2. Access the score directly using the name key
# print(student_dict["Alice"])  # Output: 90
# print(student_dict["Bob"])    # Output: 80

# Safe Lookup Tip: If a name might not exist, use .get() to avoid a crash:

# # Returns None instead of crashing if "David" isn't found
# print(student_dict.get("David")) 

# ------------------------------
# ## Method 2: Loop and Search (Best for One-Time Lookups)
# If you only need to look up a score once and don't want to create a new dictionary, you can use a loop to search for the specific name.

# students = [("Alice", 90), ("Bob", 80), ("Charlie", 70)]target_name = "Bob"
# # Loop through and unpack the name and scorefor name, score in students:
#     if name == target_name:
#         print(f"{target_name}'s score is {score}")
#         break

# Output:

# Bob's score is 80

# ------------------------------
# ## Method 3: One-Liner (List Comprehension)
# If you want a quick one-liner to pull the score out of the list:

# students = [("Alice", 90), ("Bob", 80), ("Charlie", 70)]
# # Extracts the score where the name matchesscore = [score for name, score in students if name == "Charlie"][0]
# print(score)  # Output: 70

# Would you like to see how to handle situations where multiple students have the same name, or do you want to learn how to update a student's score once you find it?

