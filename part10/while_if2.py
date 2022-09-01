# while_sample2.py True로 바꾸기
import random
learning_score = random.randint(0, 100)

while True:
    if learning_score >= 90:
        break
    else:
        print(f"학습 스코어 미달 : {learning_score}")
        learning_score = random.randint(0, 100)
print(f"최종 학습 스코어 : {learning_score}")


import random
learning_score = random.randint(0, 100)

while True:
    if learning_score >= 90:
        break
    print(f"학습 스코어 미달 : {learning_score}")
    learning_score = random.randint(0, 100)
print(f"최종 학습 스코어 : {learning_score}")
