num_vars = int(input("Enter the number of variables"))
vars= input("Enter the variable for comparison")
rules=[]
for i in range(3):
    rule= input(f"Enter the rules {i+1}")
    rules.append(rule)


goal_var= input("Enter the goal variable ")

#facts for checking
fact1 = input("Enter fact 1 (in the format '<variable> = T/F'): ")
fact2 = input("Enter fact 2 (in the format '<variable> = T/F'): ")

def check_goals(rules, goal_var, facts, satisfied_goals=[]):
    for rule in rules:
        antecedent, consequent = rule.split('IF ')[1].split(' THEN ')
        if consequent.split()[0] == goal_var:
            additional_goals = antecedent.split(' AND ')
            for goal in additional_goals:
                if goal not in satisfied_goals:
                    for fact in facts:
                        if goal == fact.split()[0] and fact.split()[2] == 'T':
                            satisfied_goals.append(goal)
                            break
            # Step 8: Recursive call to check for new unsatisfied goals
            for goal in additional_goals:
                if goal not in satisfied_goals:
                    check_goals(rules, goal.split()[0], facts, satisfied_goals)
    return satisfied_goals

def unsatisfied_goals(rules,goal_var, facts):
    for rule in rules:
        antecedent, consequent = rule.split('IF ')[1].split(' THEN ')
        if consequent.split()[0] == goal_var:
            additional_goals = antecedent.split(' AND ')
            for goal in additional_goals:
                if goal not in facts:
                    facts.append(goal)
 

    return unsatisfied_goals

# Call the function with the given inputs and print the result
facts = [fact1, fact2]
print(unsatisfied_goals)
