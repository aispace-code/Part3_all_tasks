num = input('Enter numbers: ')
step = int(input('Enter steps: '))
num1 = num.split()
def f(step, num1):
    return num1[-step:] + num1[:-step]
print(f(step, num1))