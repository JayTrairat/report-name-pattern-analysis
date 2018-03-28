def main():
    PRE = []
    MIDPRE = []
    MIDPOST = []
    POST = []
    with open('assets/type_1/naming_element_in_pre.txt', 'r', encoding='utf8') as pre:
        contents = pre.readlines()
        contents = [content.strip() for content in contents]
        PRE = contents

    with open('assets/type_1/naming_element_in_midpre.txt', 'r', encoding='utf8') as midpre:
        contents = midpre.readlines()
        contents = [content.strip() for content in contents]
        MIDPRE = contents

    with open('assets/type_1/naming_element_in_pre.txt', 'r', encoding='utf8') as midpost:
        contents = midpost.readlines()
        contents = [content.strip() for content in contents]
        MIDPOST = contents

    with open('assets/type_1/naming_element_in_pre.txt', 'r', encoding='utf8') as post:
        contents = post.readlines()
        contents = [content.strip() for content in contents]
        POST = contents

    naming_list = ['รายงาน' + pre + midpre + midpost + post for pre in PRE for midpre in MIDPRE for midpost in MIDPOST for post in POST]

    with open('assets/type_1/naming_list.txt', 'w', encoding='utf8') as output:
        output.write('\n'.join(naming_list))

if __name__ == "__main__":
    main()
