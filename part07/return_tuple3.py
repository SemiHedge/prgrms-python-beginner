"""온도 표기법
섭씨(Celsius) °C = (°F - 32) / 1.8 , = K - 273.15
화씨(Fahrenheit) °F = (°C * 1.8) + 32, = (K - 273.15) * 1.8 + 32
절대온도(Kelvin) K = °C + 273.15, = (°F - 32) / 1.8 + 273.15
"""

def convert_temperature(t, unit):
    if unit == 'C':
        c = t
        f = c * 1.8 + 32
        k = c + 273.15
        return c, f, k
    if unit == 'F':
        f = t
        c = (f - 32) / 1.8
        k = f + 273.15
        return c, f, k
    if unit == 'K':
        k = t
        c = k - 273.15
        f = (k - 273.15) * 1.8 + 32
        return c, f, k
    
    return 0, 0, 0


t = 30.1
u = 'C'
t_expr = convert_temperature(t, u)
print(t_expr)

