def load_input():
    with open("c:/Users/lucam/OneDrive/Desktop/advent_of_code/tor_1/input.txt", "r") as f:
        return f.read().strip()

def part1(input):
    left_list = []
    right_list = []

    lines = input.split("\n")

    for line in lines:
        left_right = line.split("   ")

        left = int(left_right[0])
        right = int(left_right[1])
        left_list.append(left)
        right_list.append(right)

    left_list.sort()
    right_list.sort()

    count = 0
    for i in range(len(left_list)):
        count += abs(left_list[i] - right_list[i])


    return count
def part2(input):
    similarity_score = 0

    left_list = []
    right_list = []

    lines = input.split("\n")

    for line in lines:
        left_right = line.split("   ")

        left = int(left_right[0])
        right = int(left_right[1])
        left_list.append(left)
        right_list.append(right)

    for i in range(len(left_list)):
        count = 0
        for j in range(len(right_list)):
            if left_list[i] == right_list[j]:
                count += 1

        similarity_score += count * left_list[i]


    return similarity_score


def main():
    input = load_input()

    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()