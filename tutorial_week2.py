input_num = input('다섯자리 숫자를 입력해주세요 : ')


answer_num = '12345'

if len(input_num) > 5 or len(input_num) < 5:
    print(len(input_num))
    exit('다섯자리 숫자가 아닙니다')

strike = 0
ball = 0

for index, answer in enumerate(answer_num):
    if input_num[index] == answer:
        strike += 1
    elif answer in input_num:
        ball += 1

print(f'{strike} strike  {ball} ball')

