def sum_digits(str):
    sum=0
    for c in str:
        if c.isdigit()==True:
            sum+=int(c)
    return sum
string = input()
print(sum_digits(string))