# 표준체중(kg) = (현재신장cm - 100) X 0.9
# 비만도(%) = (현재체중 ÷ 표준체중) X 100
def calc_bmi(height, weight):
    standard = (height - 100) * 0.9
    bmi = (weight / standard) * 100
    return int(bmi)

print(calc_bmi(177, 70))
print(calc_bmi(180, 62))
print(calc_bmi(190, 101))
print(calc_bmi(150, 45))
print(calc_bmi(160, 55))
print(calc_bmi(165, 75))