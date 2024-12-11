def load_input():
    with open("c:/Users/lucam/OneDrive/Desktop/advent_of_code/adventofcode/2024/tor_11/input.txt", "r") as f:
        return f.read().strip()
    

# Han bereits bi part1 part2 lösig gha (will ich denkt han dass es i part1 sust viel länger gah würdi).
# Han aber drum no nachträglich für part1 e unoptimierti lösig gmacht.


def part1(input):
    stones = input.split(" ")
    blinks = 25

    for blink in range(blinks):
        new_stones = []
        for i, stone in enumerate(stones):
            stone_int = int(stone)

            if stone_int == 0:
                new_stones.append("1")
            elif len(str(stone)) % 2 == 0:
                left = stone[:len(str(stone)) // 2]
                right = stone[len(str(stone)) // 2:]

                new_stones.append(str(left))
                new_stones.append(str(int(right)))
            else:
                new_stones.append(str(stone_int * 2024))


        stones = new_stones
    return len(stones)


def part2(input):
    stones = input.split(" ")
    blinks = 75

    stone_counts = {} # es chunt nöd uf dposition druf a (so werded doppelti stei igspart) => Es git viel glichi stei wege begrenzti regle und art
    for stone in stones:
        if stone in stone_counts:
            stone_counts[stone] += 1
        else:
            stone_counts[stone] = 1

    for _ in range(blinks):
        new_stones = {}
        for stone, count in stone_counts.items():
            stone_int = int(stone)

            if stone_int == 0:
                if "1" in new_stones:
                    new_stones["1"] += count
                else:
                    new_stones["1"] = count
            elif len(str(stone)) % 2 == 0:
                left = stone[:len(str(stone)) // 2]
                right = stone[len(str(stone)) // 2:]

                if left in new_stones:
                    new_stones[left] += count
                else:
                    new_stones[left] = count
                if str(int(right)) in new_stones:
                    new_stones[str(int(right))] += count
                else:
                    new_stones[str(int(right))] = count
            else:
                new_stone = str(stone_int * 2024)
                if new_stone in new_stones:
                    new_stones[new_stone] += count
                else:
                    new_stones[new_stone] = count

        stone_counts = new_stones

    total_stones = 0
    for count in stone_counts.values():
        total_stones += count

    return total_stones


def main():
    input = load_input()

    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()