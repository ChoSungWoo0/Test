subject_score = {'국어' : 0, '영어' : 0, '수학' : 0, '사회' : 0, '과학' : 0}

print('성적을 입력하세요')

for subject in subject_score:
    score = input(f'{subject} 점수 : ')
    subject_score[subject] = int(score)

worst_subject = [key for key, value in subject_score.items() if min(subject_score.values()) == value]
best_subject = [key for key, value in subject_score.items() if max(subject_score.values()) == value]
avg_score = sum(subject_score.values()) / len(subject_score)

print('---------------------------------------')

print('최저 점수: ', end='')

if len(worst_subject) > 1:
    for index in range(len(worst_subject)) :
        if index+1 == len(worst_subject):
            print(f'{worst_subject[index]}', end='\n')
        else :
            print(f'{worst_subject[index]}, ', end='')

else :
    print(worst_subject[0])

print('최고 점수: ', end='')

if len(best_subject) > 1:
    for index in range(len(best_subject)) :
        if index+1 == len(best_subject):
            print(f'{best_subject[index]}', end='\n')
        else:
            print(f'{best_subject[index]}, ', end='')

else :
    print(best_subject[0])

print(f'평균 점수 : {avg_score}')




