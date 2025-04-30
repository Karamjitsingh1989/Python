class Employee:
    
    employee_count = 100
    list = []

    def __init__(self, name, salary, designation):
         Employee.employee_count += 1
         self.__name = name
         self.__salary = salary
         self.__designation = designation
         self.__employeeCode = Employee.employee_count
         employee = {"Employee ID":self.__employeeCode,"Name":self.__name, "Salary":self.__salary,"Designation":self.__designation}
         Employee.list.append(employee)
         
    def getEmployeeDetail(self):
         return Employee.list

employee1 = Employee("Karam",200000,"Software Engineer")  
employee2 = Employee("Agaazbir",200000,"Software Engineer")  
employee3 = Employee("Harsimrat",200000,"Software Engineer")  
employee4 = Employee("Amit",200000,"Software Engineer")  
employee5 = Employee("Mitesh",200000,"Software Engineer")         
employee6 = Employee("Harry",200000,"Software Engineer")  

#print(employee1.getEmployeeDetail())


class Customer:
     def __init__(self, name, phoneNo):
          self.__name = name
          self.__phoneNo = phoneNo

     def get_name(self):
          return self.__name
     
     def get_phone(self):
          return self.__phoneNo
     def set_phoneNo(self, phone):
          self.__phoneNo = phone
          
          
customer = Customer("Karamjit",8427883915)

print(customer.get_name())
customer.set_phoneNo(9878423232)
print(customer.get_phone())        

  
       
       
       