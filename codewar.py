import builtins
import string
from sys import builtin_module_names
print(dir(builtins))
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

