def main():
    with open('assets/type_1_original.txt', 'r') as file_object:
        content = file_object.readlines()
    with open('assets/type_1_output.txt', 'w') as file_object_output:
        for element in content:
            file_object_output.write(element)

if __name__ == "__main__":
    main()
