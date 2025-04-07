num = input('정수를 입력하시오 : ')

if num == num[::-1]: #num[::-1]은 문자열을 뒤집는 파이썬 문법법
    print(f'{num}은(는) 거꾸로 정수입니다.')
else:
    print(f'{num}은(는) 거꾸로 정수가 아닙니다.')