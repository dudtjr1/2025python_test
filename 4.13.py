print('세 자리의 암스트롱 수 :', end = ' ')

for num in range(100, 1000):
    hundreds = num // 100 
    tens = (num // 10) % 10 
    ones = num % 10  

    if (hundreds**3 + tens**3 + ones**3) == num:
        print(num, end = ' ')
        
