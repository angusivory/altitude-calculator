import math

altitudes = [[11000, -0.0065], [20000, 0], [32000, 0.001], [47000, 0.0028], [51000, 0], [71000, -0.0028], [84852, -0.002]]
SEA_TEMP = 288.15
SEA_PRESSURE = 101325
MAX_HEIGHT_THAT_CAN_BE_CALCULATED = altitudes[len(altitudes)-1][0]
g = 9.80665
R = 287.00



def work_magic(height):
    T1 = SEA_TEMP
    P1 = SEA_PRESSURE
    density = 0
    h1 = 0

    for index, level in enumerate(altitudes):
        a = altitudes[index][1]
        h0 = h1
        T0 = T1
        P0 = P1
        if height == 0:
            break
        elif (height - altitudes[index][0]) >= 0:
            h1 = altitudes[index][0]
            T1 = calc_temperature(T0, a, h1, h0)
            P1 = calc_pressure(P0, T1, T0, a, h1, h0)

        else:
            h1 = height
            T1 = calc_temperature(T0, a, h1, h0)
            P1 = calc_pressure(P0, T1, T0, a, h1, h0)
            break

    density = calc_density(P1, T1)
    T_in_C = T1 - 273.15
    print(f"At an altitude of {height}m,\ntemperature: {T1}K or {T_in_C} Celsius\npressure: {P1}Pa\nair density: {density}kg/m^3")        


def calc_temperature(T0, a, h1, h0):
    new_temp = T0 + a*(h1 - h0)
    return new_temp

def calc_pressure(P0, T1, T0, a, h1, h0):
    if a != 0:
        new_pressure = P0 * (T1/T0)**(-g/(a*R))
    else:
        new_pressure = P0 * math.exp((-g/(R*T1))*(h1-h0))
    
    return new_pressure

def calc_density(P, T):
    new_density = P/(R*T)
    return new_density


height = int(input("Enter altitude to calculate for\n"))
while height > MAX_HEIGHT_THAT_CAN_BE_CALCULATED:
    print(f"Currently this program can only accept values up to {MAX_HEIGHT_THAT_CAN_BE_CALCULATED}.")
    height = int(input("Enter altitude to calculate for\n"))

work_magic(height)