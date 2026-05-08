def main() -> None:

    #just reading file in read-only mode
    my_file = open("data.txt", "r")
    print(my_file.read())

    # close the open file after operations:
    my_file.close()

    # now write into file with 'w'. this mode will erase the file content and write new data in it.
    user_input: str = input("Please enter your name: ")
    write_in_file = open("data.txt", "w")
    write_in_file.write(user_input)

    # close the open file after operations:
    write_in_file.close()

    # just reading file in read-only mode
    my_file = open("data.txt", "r")
    print(my_file.read())

    # close the open file after operations:
    my_file.close()



if __name__ == '__main__':
    main()
