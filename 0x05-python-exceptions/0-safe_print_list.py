!#/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    
    count = 0;

    try:
        for n in range(0, x):
            print(f"{my_list[n]}", end="")
            count += 1
    except Exemption:
        print()
        return count
    print()
    return count
