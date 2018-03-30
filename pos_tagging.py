from pythainlp.tag import pos_tag
from pythainlp.tokenize import word_tokenize

def main():

    with open('assets/type_1/naming_list.txt', 'r', encoding='utf8') as source:
        contents = (source.readlines())
        contents = [content.strip() for content in contents]

    tokenized_contents = [list(word_tokenize(content)) for content in contents]
    tagged_pos = [(pos_tag(tokenized_content, engine='artagger')) for tokenized_content in tokenized_contents]
    print(tagged_pos)

    # with open('assets/type_1/cosine_values.txt', 'w', encoding='utf8') as result:
    #     for sentence in (tokenized_contents):
    #         for original_sentence in (original_tokenized_contents):
    #             vector1 = (count(sentence))
    #             vector2 = (count(original_sentence))
    #             cosine = get_cosine(vector1, vector2)
    #             if cosine >= 0.3:
    #                 result.write('"' + (''.join(sentence)) + '"' + ' COMPARED TO ' + '"' + (''.join(original_sentence)) + '"' + ' = ' + str(cosine))
    #                 result.write('\n')

if __name__ == '__main__':
    main()
