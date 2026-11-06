# START

valid_ranks = []

while True:
    user_input = input("Enter rank: ")

    try:
        rank = int(user_input)
    except ValueError:
        print("Invalid input, skip")
        continue

    if rank == -999:
        if len(valid_ranks) >= 10:
            break
        else:
            print("Need at least 10 valid ranks. Keep entering.")
            continue

    if rank < 1 or rank > 5:
        print("Not in range, skip")
        continue

    valid_ranks.append(rank)

total_valid = len(valid_ranks)
average_rank = sum(valid_ranks) / total_valid
highest_rank = max(valid_ranks)

print()
print(f"Number of valid ranks: {total_valid}")
print(f"Average rank: {average_rank:.2f}")
print(f"Highest rank: {highest_rank}")

# STOP