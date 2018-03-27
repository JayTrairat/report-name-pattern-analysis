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
            PRE.append(elm[0])
            for index in range(1, len(elm)-2):
                MIDPRE.append(elm[index])
            POST.append(elm[len(elm)-2])

        with open('assets/type_{type}/naming_element_in_pre.txt'.format(**type), 'w', encoding='utf8') as result:
            result.write(', '.join(PRE))
        with open('assets/type_{type}/naming_element_in_midpre.txt'.format(**type), 'w', encoding='utf8') as result:
            result.write(', '.join(MIDPRE))
        with open('assets/type_{type}/naming_element_in_midpost.txt'.format(**type), 'w', encoding='utf8') as result:
            result.write(', '.join(MIDPOST))
        with open('assets/type_{type}/naming_element_in_post.txt'.format(**type), 'w', encoding='utf8') as result:
            result.write(', '.join(POST))


if __name__ == "__main__":
    main()
