def adder(num_1, num_2):
    num_1 = str(num_1)
    num_2 = str(num_2)
    counter = 0
    answer = ''
    while True:
        if not num_1 or not num_2:
            if not num_1:
                answer = num_2 + answer
            elif not num_2:
                answer = num_1 + answer
            break
        result = int(num_1[-1]) + int(num_2[-1])
        if result < 10:
            answer = str(result) + answer
            num_1, num_2 = num_1[:-1], num_2[:-1]
        else:
            if len(num_1) == 1 and len(num_2) == 1:
                answer = str(result) + answer
                break
            else:
                counter += 1
                answer = str(result)[-1] + answer
                num_1, num_2 = num_1[:-1], num_2[:-1]
                if num_1 and num_2:
                    num_1 = int(num_1) + 1
                    num_1 = str(num_1)
                elif not num_2:
                    num_2 = 1
                    num_2 = str(num_2)
                elif not num_1:
                    num_1 = 1
                    num_1 = str(num_1)
    return counter, answer

res = adder(555, 9)
print(res)