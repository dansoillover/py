def inner_function():
	print("inner_function is called")
    
def outer_function(func):
	print("outer_function is called")
 	func()
   
outer_function(inner_function)
# outer_function is called
# inner_function is called
