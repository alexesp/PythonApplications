from token import OP


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


print("#########################################################")

class Student:
    def __init__(self, new_name, new_grade):
        self.name = new_name
        self.grades = new_grade

    def average(self):
        return sum(self.grades) / len(self.grades)


student_one = Student('Rolf Smith', [70,80,90,99])
student_two = Student('Jose', [70,80,90,100])
print(student_one.name)
print(student_two.name)
print(student_one.__class__)


print(student_one.average())
print(Student.average(student_one))
print(student_two.average())
print(Student.average(student_two))


print("#########################################################")

class WorkingStudent(Student):
    def __init__(self, new_name, new_grade, salary):
        super().__init__(new_name, new_grade)
        self.salary = salary
    @property
    def weekly_salary(self):
        return self.salary * 15

rolf = WorkingStudent('Rolf',[70,80,90,99], 1500)
print(rolf.salary)
print(rolf.weekly_salary)


print("#########################################################")

my_file = open('data.txt', 'r')
file_content = my_file.read()

my_file.close()
print(file_content)

user_name = input('Enter your name: ')
my_file = open('write.txt', 'w')
my_file.write(user_name)
my_file.close()
