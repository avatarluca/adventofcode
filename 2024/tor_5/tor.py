def load_input():
    with open("c:/Users/lucam/OneDrive/Desktop/advent_of_code/adventofcode/2024/tor_5/input.txt", "r") as f:
        return f.read().strip()
    

# OK, part1 het viel länger brucht als gedacht lol
# Part2 isch denn en chline cleanup


def part1(input):
    count = 0

    material = input.split("\n\n")
    rules = material[0].split("\n")
    updates = material[1].split("\n")

    for i in range(len(updates)):
        update_nums = updates[i].split(",")
        valid = True
       
        for k, update_num in enumerate(update_nums): # nimmt e update nums und luegt ob sie mal vorchunt
            update_num = int(update_num)
            for rule in rules:
                rule_nums = rule.split("\n")
                
                for rule_num in rule_nums:
                    rule_num = rule_num.split("|")
                    
                    left = int(rule_num[0])
                    right = int(rule_num[1]) 

                    # chamer optimiere idem mer eifach nur regle gaht go luege wo left und right sicher i de liste vorchömed (denn evtl for loop merge)
                    if update_num == left:
                        for j in range(len(update_nums)):
                            if k > j and int(update_nums[j]) == right:
                                valid = False
                                break
                    elif update_num == right: 
                        for j in range(len(update_nums)):
                            if k < j and int(update_nums[j]) == left:
                                valid = False
                                break
                                
        if valid:
            count += int(update_nums[len(update_nums) // 2])
    return count 


def part2(input):
    count = 0

    material = input.split("\n\n")
    rules = material[0].split("\n")
    updates = material[1].split("\n")

    splitted_rules = []
    for rule in rules:
        left, right = rule.split("|")
        splitted_rules.append((int(left), int(right)))

    for i in range(len(updates)):
        update_nums = updates[i].split(",")
        valid = True
        
        # dasmal direkt ints
        update_nums = [int(num) for num in update_nums]

        for left, right in splitted_rules:
            if left in update_nums and right in update_nums:
                if update_nums.index(left) > update_nums.index(right): # me mues eig nur luege ob left vor right chunt
                    valid = False
                    break
        if not valid:
            """
            for k in range(len(update_nums)):
                for left, right in splitted_rules:
                    if left in update_nums and right in update_nums:
                        left_i = update_nums.index(left)
                        right_i = update_nums.index(right)

                        if left_i > right_i:
                            update_nums[left_i], update_nums[right_i] = update_nums[right_i], update_nums[left_i]
            """
            # REVISIT
            # Chline denkfehler gha (het aber lustigerwis trotzdem funktioniert)
            # Idee: Es git kei garantie wenn me swapped das denn die bereits verwendete regle no stimmet
            # Drum hani eifach welle durch updatenums dureloope bis es halt nümme swapped (aber das han ich irgendwie komisch gmacht)
            # Für das brüchtemer en while und höret denn erst uf wenn kei swaps meh gmacht wird (also en art bruteforce)
            # Funktioniert nur wenns kei zyklischi A | B und B | A rules git (bzw. au indirekt mit A | B, B | C und C | A) sondern DAG.
            # Denn wers unenscheidbar. 
            fertig = False
            while not fertig:
                fertig = True

                for left, right in splitted_rules:
                    if left in update_nums and right in update_nums:
                        left_i = update_nums.index(left)
                        right_i = update_nums.index(right)

                        if left_i > right_i:
                            update_nums[left_i], update_nums[right_i] = update_nums[right_i], update_nums[left_i]
                            fertig = False
    
            count += int(update_nums[len(update_nums) // 2])

            # Alternativ chamer en graph us de regle mache und denn topologisch sortiere (um e fixi reihefolg zbecho)
    return count 


def main():
    input = load_input()

    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()