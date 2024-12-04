def load_input():
    with open("input.txt", "r") as f:
        return f.read().strip()

def main():
    input = load_input()
    algorithm(input)

if __name__ == "__main__":
    main()

def algorithm(input):
    pass
