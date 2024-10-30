# diffence between arrays and list 
# arrays stores  data of same type
# list stores diffrent data of diffrent type

# example
courses =["MIT","Cybersecurity","Datascience"]
print(courses[1])

# looping through an element 
for Y in courses:
  print("Course is",Y)

# Adding an elemnt into an array
courses.append("Web Development")
print(courses)

# deletion of  elemnts in an array
courses.remove("MIT")
print(courses)
