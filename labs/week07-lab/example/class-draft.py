





# วิธีการแก้ปัญหา
class ClassName:
    """Class docstring"""

    # ข้อมูลที่เราต้องใช้ในการแก้ปัญหา ระบุไว้ใน constructor method
    def __init__(self, parameters):
        # Constructor method
        self.attribute = value


    # การกระทำ ==> method
    def method_name(self):
        # Instance method
        return something

# การสร้างวัสดุจากคลาส ==> เอาคลาสมาใช้
myObj = ClassName(parameters)

# ใช้งานวัสดุจากคลาส
print(myObj.attribute)
resultFromMethod = myObj.method_name()

myObj = ClassName(parameters)
print(myObj.attribute)
print(myObj.method_name())
myObj.method_name2()