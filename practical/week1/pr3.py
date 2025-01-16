def main():
    while True:
        print("\nMenu:")
        print("1. Look up information about 'input' function")
        print("2. Quit the program")

        choice = input("Enter your choice: ")

        if choice == "1":
            help(input)  
        elif choice == "2":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
