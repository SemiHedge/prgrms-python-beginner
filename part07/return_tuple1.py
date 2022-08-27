"""온도 표기법
섭씨(Celsius) °C = (°F - 32) / 1.8 , = K - 273.15
화씨(Fahrenheit) °F = (°C * 1.8) + 32, = (K - 273.15) * 1.8 + 32
절대온도(Kelvin) K = °C + 273.15, = (°F - 32) / 1.8 + 273.15
"""

def convert_temperature(c):
    c = c
    f = c * 1.8 + 32
    k = c + 273.15
    return c, f, k


# 함수 실행
t = 25.5
t_expr = convert_temperature(t)
print(t_expr)
