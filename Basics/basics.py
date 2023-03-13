def main() -> None:
    int_ = 0
    str_ = ""
    list_ = ["", 2] # Mutable (Changeable)
    tuple_ = (3, 2, 5) # Immutable (Un-changeable)
    dict_ = {1: "one"} # dictionary[1] == "one"
    '''
        for x, y in thisdict.items():
        print(x, y)
    '''
    bool_ = True
    set_ = {"a", "b", "c"}

    # List and Dictionary Comprehension
    list2_ = [x**2 for x in range(1, 20) if x % 2 == 0] # List of even numbers squared from 1 to 19
    # One Line if statement: True if condition else False
    list3_ = [x**2 if x % 2 == 0 else x for x in range(1, 20) ] # Only square Even numbers
    dict2_ = {index:str(item) for index, item in enumerate(list2_) if item < 300}
    print(list3_)

def sort_close_to_50(num: int):
    """
    thislist = [100, 50, 65, 82, 23]
    thislist.sort(key = sort_close_to_50)
    """
    return abs(num - 50)

def if_else():
    a = 200
    b = 33

    print("A") if a > b else print("B")

    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
    else:
        print("a is greater than b")

if __name__ == "__main__":
    main()