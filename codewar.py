
def to_camel_case(text):
    #your code here
    if text == "":
        return ""
    else:
        if "-" in text:
            text_sub = text.replace("_", "-")
            new_text = text_sub.split("-")
            word = [new_text[0]] + [ n.title() for n in new_text if new_text.index(n) != 0  ]
            return "".join(word)
            
      

print(to_camel_case("The-cat_Is_evil"))

def count_bits(n):
    return bin(n)

        
print(type(count_bits(3)), count_bits(3))

class PersonType:

    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    def printName(self):
        print(PersonType.firstName,' ',PersonType.lastName)
    def setName(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    def getFirstName(self):
        return self.firstName
    def getLastName(self):
        return self.lastName

class DoctorType(PersonType):
    def __init__(self, fn, ln):
        super().__init__(fn, ln)
        self.speciality = None

    def setSpeciality(self, speciality):
        self.speciality = speciality

class BillType:
    def __init__(self, id, charge):
        self.id = id
        self.charge = charge

def valid_parentheses(string):
    #your code here
    return string.count("(") == string.count(")") and string[::-1].find("(") > string[::-1].find(")")

print(valid_parentheses('yl)(g(ty)(ewc(()isbq)ca)x()gbc'))

# def sort_array(source_array):
#     # Return a sorted array.
#     if not source_array : 
#         return []
#     else:
#         for num in source_array:
#             for n in range(0, max(source_array)):
#                 if n % 2 == 1 :
#                     print(source_array.index(num))
#                     print(n)
#                     source_array[source_array.index(num)] = n
#             print(source_array)
#         return source_array

# sort_array([5, 3, 2, 8, 1, 4])



import math

def make_readable(seconds):
     # Do something
    a=str(seconds//3600)
    b=str((seconds%3600)//60)
    c=str((seconds%3600)%60)
    list = [a, b, c]
    new_t = [n if len(n) > 1 else "0" + n for n in list]

    return ":".join(new_t)
    
#     if seconds >= 60:
#         if seconds % 3600 == 0 :
#             hrs = math.floor(seconds / 3600)
#             mins = 0
#         else :
#             hrs = math.floor(seconds / 3600)
#         if seconds % 60 == 0:
#             mins = math.floor(seconds / 60)
#             secs = 0
#         else:
#             mins = seconds % 60
#             secs = mins % 60
#         time = [str(hrs) , str(mins) , str(secs)]
#         new_t = [n if len(n) > 1 else "0" + n for n in time ]
#         return  ":".join(new_t)
#     else:
#         secs = seconds
#         time = [str(0), str(0), str(secs)]
#         new_t = [n if len(n) > 1 else "0" + n for n in time ]
#         return ":".join(new_t)
    

make_readable(60)
    