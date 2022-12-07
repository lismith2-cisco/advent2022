with open("2022_6_signal_input.txt") as f:
    buffer = f.read()

position = 0
while (True):
    for first_add in range(13, -1, -1):
        for second_add in range(1, 14-first_add):
            # print(
            #     f"comparing {buffer[position + first_add]} and {buffer[position + first_add + second_add]}")
            if buffer[position + first_add] == buffer[position + first_add + second_add]:
                # print("same!")
                break
        else:
            # print(f"no dupicate for first_add {first_add}")
            continue
        # print(f"duplicate found for first_add {first_add}")
        break
    else:
        # print(f"no duplicates found at position {position}")
        break
    # print(
    #     f"duplicate found at position {position}, jumping by {first_add + 1}")
    position += first_add + 1

print(position + 14)
