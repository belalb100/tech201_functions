def cm_to_m(cm):
    return cm / 100

def m_to_ft(m):
    return m * 3.28084


cm = int(input("Enter the value in centimeters: "))


m = cm_to_m(cm)


ft = m_to_ft(m)

print(f"{cm} cm is equal to {m} meters or {ft} feet.")
