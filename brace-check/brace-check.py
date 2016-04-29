
def groupers_are_valid(s):

    openers = ['{', '[', '(']
    closers = ['}', ']', ')']

    double_agents = ['|', '?']

    grouper_stack = []
    for character in list(s):
        if character in double_agents:
            last_grouper = None
            grouper_stack_length = len(grouper_stack)
            if grouper_stack_length > 0:
                last_grouper = grouper_stack[-1]

            if last_grouper == character:
                grouper_stack.pop()
            else:
                grouper_stack.append(character)

        if character in openers:
            index_of_opener = openers.index(character)
            grouper_stack.append(index_of_opener)

        if character in closers:
            index_of_closer = closers.index(character)
            index_of_matching_opener = grouper_stack.pop()
            if index_of_closer != index_of_matching_opener:
                return False

    return len(grouper_stack) == 0

print groupers_are_valid("{|[]()|}")
print groupers_are_valid("{[|]|}")
print groupers_are_valid("{[(])}")
print groupers_are_valid("{[}")
print groupers_are_valid("|{?||?}|")
print groupers_are_valid("|{?|?|}|")
