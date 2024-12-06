'''program that reverse text inputed by user'''
def str_reverse(s):
    """Function that reverse string"""
    return s[::-1]

def main():
    """Main function of our program
    """
    l = input("Your string: ")
    print("reversed string: ", end = "")
    print(str_reverse(l))
    input()

if __name__ == "__main__":
    main()
