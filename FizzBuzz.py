

def fizzBuzz():
    arr = []
    for i in range(1, 101):
        item = ""
        if i % 3 == 0:
            item += "Fizz"
        if i % 5 == 0:
            item += "Buzz"
        
        if item == "":
            arr.append(i)
        else:
            arr.append(item)
    return arr