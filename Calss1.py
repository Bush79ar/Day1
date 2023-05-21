class Employee:
    def __init__ (self, empid,empname,empslary,empdepartment):
        self.empid = empid
        self.empname = empname
        self.empslary = empslary
        self.__empdepartment = empdepartment
  
       
       
        
    def assgin_department(self , new_empdepartment):
        self.__empdepartment= new_empdepartment
        
    def  calculate_empslary(self,hounr ):
        if hounr >  50:
            overtime = hounr -50
            overtime_amount =(overtime*(self.empslary/50))
            #print(f"({self.empname} worked overtime")
            return  overtime_amount
        else:
            return self.empslary
            
        
        
    def print_Employee_details(self):
        return f"this person name is {self.empid} and {self.empname} and {self.empslary} and {self.__empdepartment}"
        
        
p1 = Employee("E79867", "AAA", 50000, "Acount")
p2 = Employee("E79867", "BBB", 400, "Acount")
p3 = Employee("E79867", "ccc", 60000, "Acount")
p4 = Employee("E79867", "ddd", 70000, "Acount")
p2.assgin_department("HR")
print(p2.calculate_empslary(10))







        
    