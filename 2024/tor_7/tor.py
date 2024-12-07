def load_input():
    with open("c:/Users/lucam/OneDrive/Desktop/advent_of_code/adventofcode/2024/tor_7/input.txt", "r") as f:
        return f.read().strip()

def part1(input): 
    lines = input.split("\n")
    dict = {}
    for line in lines:
        key, values = line.split(": ")

        value = values.split(" ")

        dict[key] = value

    count = 0
    for key in dict:
        values = dict[key]
        for i in range(2 ** (len(values) - 1)):
            binary = bin(i)[2:] # binär vo i ohni 0b
            binary = "0" * (len(values) - 1 - len(binary)) + binary # so dass jedi zahl glich lang isch (value length - 1)
            
            sol = int(values[0])
            for j in range(len(binary)):
                if binary[j] == "0":
                    sol += int(values[j + 1])
                else:
                    sol *= int(values[j + 1])
            if sol == int(key):
                count += int(key)
                break

    return count
    

def part2(input):
    lines = input.split("\n")
    dict = {}
    for line in lines:
        key, values = line.split(": ")

        value = values.split(" ")

        dict[key] = value

    count = 0
    for i, key in enumerate(dict):
        values = dict[key]

        for i in range(3 ** (len(values) - 1)):
            ternary = ""
            for j in range(len(values) - 1):
                ternary += str(i // (3 ** (len(values) - 2 - j)) % 3) # -2 will j vo 0 startet

            sol = int(values[0])
            for j in range(len(ternary)):
                if ternary[j] == "0":
                    sol += int(values[j + 1])
                elif ternary[j] == "1":
                    sol *= int(values[j + 1])
                else:
                    sol = int(str(sol) + values[j + 1])

            if sol == int(key):
                count += int(key)
                break

    return count

def main():
    input = load_input()

    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()