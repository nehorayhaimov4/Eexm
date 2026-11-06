# START

reverse_string_detector = []

while True:
    user_input = input("Enter string: ")
    if user_input.lower() == "quit":
        break
    reverse_string_detector.append(user_input)

reversed_match_found = False

for string in reverse_string_detector:
    reversed_string = string[::-1]
    if reversed_string in reverse_string_detector:
        reversed_match_found = True
        break

print()
print("Output:")
if reversed_match_found:
    print("Reversed match found")
else:
    print("No reversed match found")

# STOP