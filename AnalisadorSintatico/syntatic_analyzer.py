
def clr_1(grammar, sentence):

    table = grammar.get_LR_canonic_data()
    action_table = table[0]
    goto_table = table[1]
    stack = []

    stack.append("$")
    stack.append(0)
    lookahead = sentence[0]
    index = 0

    while True:
        last = stack[-1]

        print(stack)
        if (last, lookahead) in action_table:
            action = action_table[(last, lookahead)]

            if ('accept' in action):
                print("Accept")
                return True

            elif ('shift' in action):

                stack.append(lookahead)
                index += 1
                lookahead = sentence[index]
                stack.append(action[1])

            elif ('reduce' in action):
                if (action[2] == ['&']):
                    stack.pop()
                    old_last = stack[-1]
                    stack.append(action[1])
                    last = stack[-1]
                    goto = goto_table[(old_last, last)]
                    stack.append(goto)
                else:
                    for x in range(len(action[2]) * 2):
                        stack.pop()
                    old_last = stack[-1]
                    stack.append(action[1])
                    last = stack[-1]
                    goto = goto_table[(old_last, last)]
                    stack.append(goto)

        else:
            break

    return False
