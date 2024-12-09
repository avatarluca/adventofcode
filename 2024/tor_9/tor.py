def load_input():
    with open("c:/Users/lucam/OneDrive/Desktop/advent_of_code/adventofcode/2024/tor_9/input.txt", "r") as f:
        return f.read().strip()

def part1(input):
    blocks = []
    i = 0

    while i < len(input):
        length = int(input[i])
        blocks.append((len(blocks) // 2, length))  
        i += 1
 
    detailed_map = [] # unary 
    for idx, (typ, length) in enumerate(blocks):
        if idx % 2 == 0:  # file
            detailed_map.extend([typ] * length)
        else:  # frei 
            detailed_map.extend(["."] * length)

    n = len(detailed_map)

    for i in range(n-1, 0, -1):
        if detailed_map[i] != ".":
            for j in range(0, i):
                if detailed_map[j] == ".":
                    detailed_map[j] = detailed_map[i]
                    detailed_map[i] = "."
                    break

    checksum = 0
    for pos, block in enumerate(detailed_map):
        if block != ".":
            checksum += pos * block
    
    return checksum

def part2(input):
    blocks = []
    i = 0

    while i < len(input):
        length = int(input[i])
        blocks.append((len(blocks) // 2, length))  
        i += 1

    detailed_map = [] # unary 
    for idx, (typ, length) in enumerate(blocks):
        if idx % 2 == 0:  # file
            detailed_map.extend([typ] * length)
        else:  # frei
            detailed_map.extend(["."] * length)

    n = len(detailed_map)

    current_file_id = 0
    for i in range(n - 1, -1, -1): # numme zum grösst file id finde
        if detailed_map[i] != ".":
            current_file_id = detailed_map[i]
            break

    while current_file_id >= 0:
        # print(current_file_id)
        block_start = 0
        block_length = 0
        for pos, block in enumerate(detailed_map):
            if block == current_file_id:
                if block_length == 0:
                    block_start = pos
                block_length += 1
            elif block_length > 0:
                break

        for target_pos in range(block_start - 1): # wenn freie platz vorem file (left most) als ganzi einheit denn verschieb
            if target_pos + block_length <= n and all(detailed_map[target_pos + i] == "." for i in range(block_length)):             
                for i in range(block_length):
                    detailed_map[target_pos + i] = current_file_id
                    detailed_map[block_start + i] = "."
                break

        current_file_id -= 1

    checksum = 0
    for pos, block in enumerate(detailed_map):
        if block != ".":
            checksum += pos * block

    return checksum


def main():
    input = load_input()

    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()