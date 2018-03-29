# -*- coding: utf-8 -*-

from pythainlp.tokenize import word_tokenize
from collections import Counter as count
import math

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def main():
    try:

        with open('assets/type_1/original.txt', 'r', encoding='utf8') as original:
            original_contents = original.readlines()
            original_contents = [''.join(content.strip().split('|')) for content in original_contents]

        with open('assets/type_1/naming_list.txt', 'r', encoding='utf8') as source:
            contents = source.readlines()
            contents = [content.strip() for content in contents]

        tokenized_contents = [list(word_tokenize(content)) for content in contents]
        original_tokenized_contents = [list(word_tokenize(content)) for content in original_contents]

        with open('assets/type_1/cosine_values.txt', 'w', encoding='utf8') as result:
            for sentence in (tokenized_contents):
                for original_sentence in (original_tokenized_contents):
                    vector1 = (count(sentence))
                    vector2 = (count(original_sentence))
                    cosine = get_cosine(vector1, vector2)
                    if cosine >= 0.3:
                        result.write('"' + (''.join(sentence)) + '"' + ' COMPARED TO ' + '"' + (''.join(original_sentence)) + '"' + ' = ' + str(cosine))
                        result.write('\n')

        with open('assets/type_1/cosine_values_only_value.txt', 'w', encoding='utf8') as result:
            for sentence in (tokenized_contents):
                for original_sentence in (original_tokenized_contents):
                    vector1 = (count(sentence))
                    vector2 = (count(original_sentence))
                    cosine = get_cosine(vector1, vector2)
                    if cosine >= 0.3:
                        result.write(str(cosine))
                        result.write('\n')

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
