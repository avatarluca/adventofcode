def load_input():
    with open("c:/Users/lucam/OneDrive/Desktop/advent_of_code/tor_3/input.txt", "r") as f:
        return f.read().strip()

def part1(input):
    import re
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input)
    sum = 0
    for match in matches:
        sum += int(match[0]) * int(match[1])

    return sum


def part2(input):
    import re
    
    mul_pattern = r"mul\((\d+),(\d+)\)"
    total_sum = 0

    enabled = True

    for i in range(len(input)): # linear durch input weil wenn dont dann alle nachfolgenden mul ignoriert werden
        # chamer no besser mache idem i nöd nur immer +1 macht sondern halt denn i je nachdem wie lang das wort isch verschiebt
        if input[i:].startswith("don't()"):
            enabled = False
        elif input[i:].startswith("do()"):
            enabled = True
        
        if enabled:
            mul_match = re.match(mul_pattern, input[i:])
            if mul_match: # nur wenn mul am anfang vo dem substring ist (sonst könnt dont()do()dont()mul() nicht funktionieren)
                total_sum += int(mul_match.group(1)) * int(mul_match.group(2))
    
    return total_sum


def main():
    input = load_input()

    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()