def main():
    stop_words = [
        'Hello',
    ]
    with open('assets/type_1_original.txt', 'r') as file_object:
        content = file_object.readlines()

    with open('assets/type_1_output.txt', 'w') as file_object_output:
        content = [element.strip().split('|') for element in content]
        for elements in content:
            filtered_elements = ([element for element in elements if element not in stop_words])
            joined_filtered_elements = '|'.join(filtered_elements)
            file_object_output.write(joined_filtered_elements + '\n')

if __name__ == "__main__":
    main()
