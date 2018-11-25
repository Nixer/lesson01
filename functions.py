def get_summ(one, two, delimiter='&'):
    return (str(one) + str(delimiter) + str(two)).upper()


sum_string = get_summ("Learn", "Python")
print(sum_string)
