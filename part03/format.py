# string format
text1 = "{}대학 {}학번 {}입니다."
text2 = "{0}대학 {1}학번 {2}입니다. {2}은/는 {1}학번입니다."

# format
new_text1 = text1.format('머쓱', 20, '스펜서')
print(new_text1)

new_text2 = text2.format('머쓱', 20, '스펜서')
print(new_text2)

print(text2.format('머쓱', 20, '스펜서'))