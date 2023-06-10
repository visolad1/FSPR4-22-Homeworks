def upper_letter(s): 
    try: 
        return s.upper()
    except AttributeError as err: 
        return err

s = "mama"
isinstance (s, str ) 


if __name__ == "__main__":
    print(upper_letter(5))
    print(upper_letter('adgfhgj'))

# =============================================================

def num_division(num): 
    try: 
        return num/2
    except TypeError as err: 
        return err

if __name__ == "__main__":
    print(num_division(10))
    print(num_division('dfh'))
    
# ========================================================
def num_division(num):  # ?
    try: 
        return num/2
    except TypeError as err: 
        return err

if __name__ == "__main__":
    print(num_division(10))
    print(num_division('dfh'))

