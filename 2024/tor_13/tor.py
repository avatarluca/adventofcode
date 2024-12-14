def load_input():
    with open("c:/Users/lucam/OneDrive/Desktop/advent_of_code/adventofcode/2024/tor_13/input.txt", "r") as f:
        return f.read().strip()

def part1(input):
    machines = input.split("\n\n")
    
    configurations = [] # liste vo dicts mit {A, B, P}. Jewils zweier Tupel (x,y)
    for machine in machines:
        lines = machine.split("\n")
        A = tuple(map(int, lines[0].split("X+")[1].split(", Y+")))
        B = tuple(map(int, lines[1].split("X+")[1].split(", Y+")))
        P = tuple(map(int, lines[2].split("X=")[1].split(", Y=")))
        configurations.append({"A": A, "B": B, "P": P})

    total_cost = 0

    for config in configurations:
        ax, ay = config["A"]
        bx, by = config["B"]
        px, py = config["P"]

        sol = []

        # alli mögliche kombis und denn nachher eif min choste sueche
        for a in range(101): # nöd me als 100 button presses für a (gemäss estimate)
            for b in range(101): # nöd me als 100 button presses für b (gemäss estimate)
                if a * ax + b * bx == px and a * ay + b * by == py:
                    cost = 3 * a + b # Tokens = 3 a , 1 b
                    sol.append((cost, a, b))

        res = None
        if sol: 
            res = min(sol)
        
        if res:
            c, a, b = res
            total_cost += c

    return total_cost


def part2(input):
    machines = input.split("\n\n")
    
    configurations = [] # liste vo dicts mit {A, B, P}. Jewils zweier Tupel (x,y)
    for machine in machines:
        lines = machine.split("\n")
        A = tuple(map(int, lines[0].split("X+")[1].split(", Y+")))
        B = tuple(map(int, lines[1].split("X+")[1].split(", Y+")))
        P = tuple(map(int, lines[2].split("X=")[1].split(", Y=")))
        Overflow_P = (P[0] + 10000000000000, P[1] + 10000000000000)
        configurations.append({"A": A, "B": B, "P": Overflow_P})

    """
    Problem: Bruteforce würdi wieder mal vielzlang bruche
    Es brucht entweder e mathematischi direkti oder e dp lösig (oder irgendöppis bessers ka)
    Mathematisch:
    ax * a + bx * b = px
    ay * a + by * b = py

    a = (px * by - py * bx) / (ax * by - ay * bx)
    b = (px - ax * a) / bx
    """

    """
    No usführlich lut notize:
    ax * a + bx * b = px
    bx * b = px - ax * a
    b = (px - ax * a) / bx

    ay * a + by * ((px - ax * a) / bx) = py
    ay * a + (by * px - by * ax * a) / bx = py
    bx * ay * a + by * px - by * ax * a = py * bx
    bx * ay * a - by * ax * a = py * bx - by * px
    a * (bx * ay - by * ax) = py * bx - by * px
    a = (py * bx - by * px) / (bx * ay - by * ax)
    """

    total_cost = 0  
    for i, config in enumerate(configurations):
        ax, ay = config["A"]
        bx, by = config["B"]
        px, py = config["P"]

        a = (px * by - py * bx) / (ax * by - ay * bx)
        b = (px - ax * a) / bx

        cost = 3 * a + b

        if a.is_integer() and b.is_integer(): # nur wennd pushingazahl ganzzahlig sind sust kei lösig
            total_cost += int(cost)

        # print(f'Maschine {i+1} het min cost {cost}')

    return total_cost

def main():
    input = load_input()

    print(part1(input))
    print(part2(input))

if __name__ == "__main__":
    main()