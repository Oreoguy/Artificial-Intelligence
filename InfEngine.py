# function to parse the boolean expression in the rule
def parse_expression(expression, values):
    # tokenize the expression based on spaces
    tokens = expression.split()
    result = True
    operator = "AND"
    for token in tokens:
        if token == "AND":
            operator = "AND"
        elif token == "OR":
            operator = "OR"
        elif token == "NOT":
            result = not values.get(tokens[tokens.index(token) + 1])
        else:
            if operator == "AND":
                result = result and values.get(token)
            else:
                result = result or values.get(token)
    return result

# function to check which rules fire based on the given facts
def check_rules(fact1, fact2, rules):
    values = {
        rule[0]: False for rule in rules
    }
    values[fact1[0]] = fact1[1]
    values[fact2[0]] = fact2[1]
    fired_rules = []
    for rule in rules:
        if parse_expression(rule[1], values):
            fired_rules.append(rule[0])
            values[rule[0]] = True
    return fired_rules


# main program
num_vars = int(input("Enter the number of variables: "))
variables = input("Enter the variable names: ").split()[:num_vars]
rules = []
for i in range(3):
    rule = input(f"Enter rule {i+1}: ")
    var = rule.split()[-1]
    while var not in variables:
        print(f"Error: variable {var}")
        rule = input(f"Enter rule {i+1}: ")
        var = rule.split()[-1]
    rules.append((var, rule[3:-len(var)-1]))
fact1 = (input("Enter fact 1: "), input("Enter value of fact 1 (T/F): ").upper() == "T")
fact2 = (input("Enter fact 2: "), input("Enter value of fact 2 (T/F): ").upper() == "T")
fired_rules = check_rules(fact1, fact2, rules)
print ("Rules_fired :",rules)