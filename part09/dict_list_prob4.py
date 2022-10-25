response = {
    "result": {
        "label_kr": ["새", "벌새", "꽃", "벌레", "자연", "파이썬"],
        "label_en": ["Bird", "Hummingbird", "Flower", "Bug", "Nature", "Python"]
    }
}

find_tag = input("검사할 태그 이미지를 입력하세요 : ")

# 이미지 태그 결과에 find_tag가 있는지 확인하는 if문을 아래 작성해봅시다.
if find_tag in response['result']['label_kr'] + response['result']['label_en']:
    print(f"해당 이미지 태그에 {find_tag} 감지")
else:
    print(f"해당 이미지 태그에 {find_tag} 미감지")
