from extract import load_neos, load_approaches

my_object = load_neos()
print(len(my_object))
contents = load_approaches()
print(type(contents))

for i in my_object:
    if i.designation == "2005 OE3" or i.designation == "170903":
        print(i)

for i in range(10):
    print(my_object[i])

for i in range(2):
    print(contents[i])