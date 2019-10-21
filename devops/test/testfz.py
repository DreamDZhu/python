object1 = ["Will",28,["python","c#","javascript"]]
object2 = object1


print(f"id of object 1 {id(object1)}")
print(object1)
print([id(ele) for ele in object1])


print(f"id of object 2 {id(object2)}")
print(object2)
print([id(ele) for ele in object2])

object1[0] = "aaa"
object1[2].append("CSS")

print("更改object1 之后")
print(f"id of object 1 {id(object1)}")
print(object1)
print([id(ele) for ele in object1])


print(f"id of object 2 {id(object2)}")
print(object2)
print([id(ele) for ele in object2])