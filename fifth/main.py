
# if __name__ == __main__
# It means the script can be imported or run standalone
# (functions and classes in this module can be reused without the main block of code executing.
# It helps readability, leaves no global variables and avoids unintended execution)

# module is a single file and the libraries are a collection of modules, packages

# importing a library, when you run the library directly, it displays something ,but you want a particular thing without the others showing
# when you run the library directly, it displays a help page, so you use this to run without displaying help page, i guess
# you want to import and use some of the variables and functions without running it directly


def main():
    print(" Hi ")
    # Your program goes here


if __name__ =='__main__':
    main()