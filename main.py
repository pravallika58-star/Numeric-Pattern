
# Case Study 27: Advanced Numeric Pattern Generator

print("====================================")
print("     ADVANCED NUMERIC PATTERN")
print("====================================")

print("1. Hollow Diamond Pattern")
print("2. Symmetric Number Pattern")

choice = input("Enter your choice (1 or 2): ")

if choice == "1" or choice == "2":

    size_text = input("Enter the size of the pattern: ")

    if not size_text.isdigit():
        print("Invalid input! Enter a positive integer.")

    else:
        n = int(size_text)

        if n <= 0:
            print("Size must be greater than zero.")

        elif choice == "1" and n < 2:
            print("Hollow diamond size must be at least 2.")

        else:

            if choice == "1":

                print("\nHOLLOW DIAMOND PATTERN\n")

                # Upper half
                for i in range(1, n + 1):

                    print(" " * (n - i), end="")

                    if i == 1:
                        print("*")
                    else:
                        print("*" + " " * (2 * i - 3) + "*")

                # Lower half
                for i in range(n - 1, 0, -1):

                    print(" " * (n - i), end="")

                    if i == 1:
                        print("*")
                    else:
                        print("*" + " " * (2 * i - 3) + "*")

            elif choice == "2":

                print("\nSYMMETRIC NUMBER PATTERN\n")

                # Upper half
                for i in range(1, n + 1):

                    print(" " * (n - i), end="")

                    for j in range(1, i + 1):
                        print(j, end=" ")

                    for j in range(i - 1, 0, -1):
                        print(j, end=" ")

                    print()

                # Lower half
                for i in range(n - 1, 0, -1):

                    print(" " * (n - i), end="")

                    for j in range(1, i + 1):
                        print(j, end=" ")

                    for j in range(i - 1, 0, -1):
                        print(j, end=" ")

                    print()

else:
    print("Invalid choice! Select 1 or 2.")

print("\n====================================")
print("       PROGRAM COMPLETED")
print("====================================")
