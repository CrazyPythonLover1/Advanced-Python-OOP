# Advanced-Python-OOP
Complete python Developer 2020 Zero to Mastery

## 4 PILLARS OF OOP

1. ENCAPSULATION
> We can protect unexpected access from outside. 
> Inner variable of a class can be accessed in a inner function(method).
> Inner variable and function can not be accessed outer function. 

2. ABSTRACTION
> Handle complexity by hiding unnecessary details from the users.
> User don't worry about it's codding. 
> User just use it. 

3. INHERITANCE 
> We can inherit the class in any child class.

```python
class User:
  def sign_in(self):
    print("Logged in")
    return

class Wizard(User): # pass the parrent class
  pass

wizard2 = Wizard()
wizard2.sign_in()

# Here, we can use method of User class in Wizard class.
# That's call Inheritance in programming. 
```


4. POLYMORPHISM
> Poly means many and Morphisom means forms...many forms.
> Polymorphism allows us to have many forms.
> It has ability to redifine methods for the derived classes.

