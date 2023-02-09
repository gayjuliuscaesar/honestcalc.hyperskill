msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


def calc(a, operation, b):
    if operation == '+':
        res = a + b
        return res
    elif operation == '-':
        res = a - b
        return res
    elif operation == '*':
        res = a * b
        return res
    elif operation == '/' and b != 0:
        res = a / b
        return res
    else:
        print(msg_3)


def do_int(v):
    if v.is_integer():
        v = int(v)
        return v
    else:
        return v


def is_one_digit(v):
    try:
        if v == int(v):
            return -10 < v < 10
    except ValueError:
        return False


def check(a, operation, b):
    msg = ''
    if is_one_digit(a) and is_one_digit(b):
        msg = msg + msg_6
    if (a == 1 or b == 1) and operation == '*':
        msg = msg + msg_7
    if (a == 0 or b == 0) and (operation == '*' or operation == '-' or operation == '+'):
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


def check_calc(v1, move, v2):
    operations = '+-*/'
    if move not in operations:
        print(msg_2)
    else:
        check(v1, move, v2)
        res = calc(v1, move, v2)
        return res


def ending(res, mem):
    answer = ''
    memo = mem
    runner = bool
    while answer != 'y' and answer != 'n':
        answer = input(msg_4)
        if answer == 'y':
            if is_one_digit(res):
                msg_index = 10
                while msg_index < 13:
                    if msg_index == 10:
                        answer = input(msg_10)
                    elif msg_index == 11:
                        answer = input(msg_11)
                    else:
                        answer = input(msg_12)
                    if answer == 'y':
                        msg_index += 1
                    else:
                        break
                else:
                    memo = res
            else:
                memo = res

    answer = ''
    while answer != 'y' and answer != 'n':
        answer = input(msg_5)
        if answer == 'n':
            runner = False
        else:
            runner = True
    return memo, runner


def main():
    memory = 0
    run = True
    while run:
        equation = input(msg_0)
        x, operation, y = equation.split()

        try:
            if x == 'M':
                x = memory
            if y == 'M':
                y = memory
            x = float(x)
            y = float(y)

        except ValueError:
            print(msg_1)
            pass

        result = check_calc(x, operation, y)
        print(result)

        memory, run = ending(result, memory)


if __name__ == '__main__':
    main()
