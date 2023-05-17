 #!/usr/bin/python3
 def multiply_by_2(a_dictionary):
     new = a_dictionary.copy()
     list_keys = list(new.keys())

    for key in list_keys:
        new[key] *= 2
    return new
