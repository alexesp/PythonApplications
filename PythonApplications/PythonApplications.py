print("Repaso de sintaxis en Python")

def greet():
        print("Hello finction")
greet()

############# C#
# public void greet()
# {
#     Console.PrintLine("Hello function.");
# } 
# greet();

############# Golang

# func greet(){
#     fmt.Println("Hello function")
# }

# greet()

#List
blockchain = [1]

def add_value():
    #blockchain.append(5.2)
    blockchain.append([blockchain[0],5.2])
    print(blockchain)

add_value()
add_value()
add_value()

friends = ["Rolf", "John", "Anna"]
counter = 0
print("#########################################################")
for friend in friends:
  print(counter)
  print(friend)
  counter = counter + 1
print("#########################################################")
for counter, friend in enumerate(friends):
    print(counter)
    print(friend)
print("#########################################################")
print(list(enumerate(friends)))
print("#########################################################")
print(list(zip([0,1,2],friends)))

print("#########################################################")
print(dict(enumerate(friends)))



print("#########################################################")

divide = lambda x, y: x / y
print((lambda x, y: x / y)(15,3))

def divide1(x, y):
    return x / y


#########    C#
# public int divide(int x, int y)
# {
#     return x / y;
# }

##########   Golang
# func divide(x int, y int) int {
#     return x / y
#     }



