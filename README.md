# tech201_functions

## Functions



### Why we use functions

- To be more effecient in our code rather than enter lines and lines of print code.
- D R Y
- Don't repeat yourself: Keep it as simple as possible.

- Functions: allows us to call our code.
- Embed particular actions so we can re- use our code.

`def print_something():`  it stands for define. empty prenthesis are required. The colon tells python what is indented is linked to the above function.
     `print("Something has been printed")` # Nothing happens because we haven't put anything to be called.
- the power comes with the argument in functions
`print_something()` # more effecient no need to say print we just call the function right away.


```def print_something(print_string):`
     `print(print_string)```

`print_something("this is my variable")`

`print_something("This is the second time I called this function")`
- Clear printing of your argument is really important as you can get confused if you haven't done so.


`def greeting(name):`
     `print("Hello my name is " + name)`

`greeting("Belal")`
`greeting("Mo")`
- Very useful instead of doing print comma again and again.

### The return statement

`def addition(int1, int2): 
- inside brackets are variables.`

     `return int1 + int2 # You must enter return so Python knows what to do with what we have given it.`

`print(addition(2, 2))`

###Default Arguments


`def addition(int1=2, int2=2):` We set the default argument in between brackets, we are saying int1 and
  `int2 = value assigned`
     `return int1 + int2`

 `print(addition())
 print(addition(10, 10))`  
 - we can change argument
 `print(addition())`

### Multiple Arguments

 `def multi_args(*multiargs):` #star passes the argument to tuple
    `print(type(multiargs))`

     `for arg in multiargs:`
         `p`rint(arg)`

 `multi_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)`

 `print(multi_args(1, 2, 3, 4, 5)) # problem because it is trying to print out function as functions aren't to be printed rather the argument.`


### Type Hints

`def greeting(name: str):` # Good habit if you want certain type of data you input it in your argument.
      `print("Hello my name is " + name)`

`greeting("Belal")`

`def division(num1: int = 5, num2: int = 2) -> float:`
     `return num1 / num2`

`print(division())`


## Function best practises

1. Name your functions clearly lower case and underscores
2. All arguments should be clear in their need and where possible include their expected type.
3. Remember the return statement or your function will return None.
4. Keep functions small where possible, to preserve readibility and simplicity.
5. Use comments in your functions/methods to give instructions on how to use them
6. Consider using type ints to avoid errors when you run your code.

