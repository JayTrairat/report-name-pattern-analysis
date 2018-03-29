def main():
    for index in range(0, 8):
        type = dict(type=index+1)
        with open('assets/type_{type}/removal_output.txt'.format(**type), 'r', encoding='utf8') as resource:
            contents = (resource.readlines())

        PRE = []
        MIDPRE = []
        MIDPOST = []
        POST = []
        for content in contents:
            content = content.strip()
            elm = content.split('|')
            # test only 1 - 100 important words
            if len(elm)-2 >= 1 and len(elm)-2 <= 100:
                PRE.append(elm[0])
                for index in range(1, len(elm)-2):
                    MIDPRE.append(elm[index])
                POST.append(elm[len(elm)-2])



        with open('assets/type_{type}/naming_element_in_pre.txt'.format(**type), 'w', encoding='utf8') as result:
            result.write('\n'.join(set(PRE)))
        with open('assets/type_{type}/naming_element_in_midpre.txt'.format(**type), 'w', encoding='utf8') as result:
            result.write('\n'.join(set(MIDPRE)))
        with open('assets/type_{type}/naming_element_in_midpost.txt'.format(**type), 'w', encoding='utf8') as result:
            result.write('\n'.join(set(MIDPOST)))
        with open('assets/type_{type}/naming_element_in_post.txt'.format(**type), 'w', encoding='utf8') as result:
            result.write('\n'.join(set(POST)))


if __name__ == "__main__":
    # print('NOT IN USED')
    main()
