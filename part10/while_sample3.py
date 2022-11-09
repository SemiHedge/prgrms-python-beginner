# 특정 수치가 나올 때 까지 반복
# 데이터 분석이나 인공지능을 하다보면, 원하는 결과가 나올 때까지 기다려야 할 때가 있다.
import random, time
learning_score = random.randint(1, 100)
# print(learning_score)

while learning_score < 90:
    print(f'학습 스코어 미달 : {learning_score}')
    learning_score = random.randint(1, 100)
    time.sleep(1)
print(f'최종 학습 스코어 : {learning_score}')