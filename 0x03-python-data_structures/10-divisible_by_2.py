def divisible_by_2(my_list=[]):
    output = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            output.append(True)
        else:
            output.append(False)

    return (output)
