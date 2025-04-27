hi = "hello" 
print(hi[-4:-0])

lan = "language, hello"
print(lan[0:8])

print(lan.upper())
print(lan.lower())
print(lan.capitalize())
print(lan.casefold())
print(lan.strip())

sentance ="pple, anana, herry"
fruits = sentance.split(", ") 
print(fruits)

fruits = sentance.join("abc")
print(fruits)

sentance = "Hello,world!"
print(sentance.find("world"))
print(sentance.replace("world", "james "))

name = "John"
age = 30
street = "no: 15 moshine  street "

print("my name is {} and I am {} year old, I live at {}".format(name,  age, street  ) )

print(f"my name is {name} and I am {age} year old, I live at {street}" )


seed = ("I am seed from the import ")