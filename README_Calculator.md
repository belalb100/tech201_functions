`def cm_to_m(cm):
    return cm / 100` - in the first line the argument is cm and we will return cm into to the equivalent value in metres by dividing it by 100.

`def m_to_ft(m):` - this take the argument 'm' which has the value of metres and then multiplies it by 3.28084 which is the mathmatical equation for converting metres to feet.
    `return m * 3.28084`

- input the value in cm
`cm = int(input("Enter the value in centimeters: "))`
- value entered by the user will be stored in the variable 'cm'

- convert cm to m
`m = cm_to_m(cm)` # It now calls this function and passes 'cm' as an argument and the returned value is stored as the variable 'm'

- convert m to ft
`ft = m_to_ft(m)`
- This calls the function and passes 'm' as an argument, the returned value is stored as the cariable 'ft'

`print(f"{cm} cm is equal to {m} meters or {ft} feet.")`
- Now the code prints the results.
