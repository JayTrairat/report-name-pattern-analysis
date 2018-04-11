def main():
    with open('assets/type_1/cosine_values_only_value.txt', 'r', encoding='utf8') as source:
        original_contents = source.readlines()
        original_contents = [content.strip() for content in original_contents]
        original_contents.sort(reverse=True)
        original_contents = original_contents
        with open('assets/type_1/cosine_values_for_ttest.txt', 'w', encoding='utf8') as result:
            result.write('\n'.join(original_contents))

    with open('assets/type_1_refactor_naming_elements/cosine_values_only_value.txt', 'r', encoding='utf8') as source:
        contents = source.readlines()
        contents = [content.strip() for content in contents]
        contents.sort(reverse=True)
        contents = contents
        with open('assets/type_1_refactor_naming_elements/cosine_values_for_ttest.txt', 'w', encoding='utf8') as result:
            result.write('\n'.join(contents))

if __name__ == '__main__':
    main()
