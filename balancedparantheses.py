def parentheses(str):
    stack = []
    dict = {"]":"[", "}":"{", ")":"("}
    for char in str:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                print False
        else:
            print False
    print stack == []

parentheses("{{}}")