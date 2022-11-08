testStr1 = '(abc(123(!"£)))'
testStr2 = '(abc123(!"£)))'
testStr3 = '(abc(123(!"£))'

def testBracets(str):
    amtOfBracets = 0
    stack = [] 
    for i in range(len(str)):
        if str[i] == '(':
            amtOfBracets += 1
            stack.append(str[i])

        elif str[i] == ')':
            closed = False

            for y in range(len(stack)):
                x = stack.pop()
                if x == '(':
                    closed = True
                    amtOfBracets -= 1
                    break

            if not closed:
                return('incomplete')
                break

        else:
            stack.append(str[i])

    if amtOfBracets:
        return('incomplete')

    return('complete')

print(f'{testStr1}:{testBracets(testStr1)}')
print(f'{testStr2}:{testBracets(testStr2)}')
print(f'{testStr3}:{testBracets(testStr3)}')
