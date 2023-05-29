#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

        """Prints x elememt.
        Args:
            my_list(list): The list to print element.
            x(int): The number of elements.
        Returns:
            Number of elememts printed.
        """

        r = 0

        for n in range(0, x):
            try:
                print("{:d}".format(my_list[n], end="")
                r += 1
            except (ValueError, TypeError):
                continue
        print("")
        return (r)
