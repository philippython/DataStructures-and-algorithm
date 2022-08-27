
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
    for num in range(2, n):
        if n % num == 1:
            print(num)
        
count_bits(1234)