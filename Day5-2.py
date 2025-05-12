from collections import defaultdict, deque

data=""" 
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
# Split the whole thing into lines
lines = data.strip().split("\n")
# Find the empty line that separates the rules and updates
split_index = lines.index("")
# Get rules (before the empty line)
rule_lines = lines[:split_index]
# Get updates (after the empty line)
update_lines = lines[split_index + 1:]

rules = []
for line in rule_lines:
    parts = line.strip().split()
    for part in parts:
        if "|" in part:
            a, b = map(int, part.split("|"))
            rules.append((a, b))

updates = []
for line in update_lines:
    update = list(map(int, line.split(",")))
    updates.append(update)

comeBefore={}
# create a dictionary that store sets to record for each number, what has to come before it.
for a,b in rules:
    if b not in comeBefore:
        comeBefore[b]=set()
    comeBefore[b].add(a)
print(comeBefore)
print(updates)

def fix_update(update,comeBefore):
    changed=True
    while changed:
        changed=False
        for i in range(len(update)):
            curr = update[i]
            if curr in comeBefore:
                for must_come_before in update[i+1:]:
                    if must_come_before in comeBefore[curr]:
                        j=update.index(must_come_before)
                        update[i],update[j]=update[j],update[i]
                        changed=True
                        break
                if changed:
                    break
    return update


# def is_valid(update,comeBefore):
#     seen=[]
#     for index,ls in enumerate(update):
#         print("ls",ls)
#         if ls in comeBefore:
#             remaining=update[index+1:]
#             for i in comeBefore[ls]:
#                 print("CB",comeBefore[ls])
#                 print(i,"seen1",remaining)
#                 if i in remaining:
#                     return False
#         seen.append(ls)
#         print("seen2",seen)
#     return True

answer=0
for update in updates:
    print("u",update)
    fixed=fix_update(update[:], comeBefore)
    print("fixed update",fixed)
    middle_index=len(fixed)//2
    answer+=fixed[middle_index]

print(answer)



