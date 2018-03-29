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
        with open('assets/type_1/removal_output.txt', 'r', encoding='utf8') as source:
            contents = source.readlines()
            contents = [content.strip().split('|') for content in contents]
            contents = [content for content in contents if len(content)-2 > 0 and len(content)-2 <= 4]
            print(contents)

        # tokenized_contents = [list(word_tokenize(content)) for content in contents]
        #
        # for sentence in (tokenized_contents):
        #     print(sentence)
        #     print('\r\n')
        # vector1 = (count(['hello', 'world']))
        # vector2 = (count(['hello', 'there']))
        #
        # cosine = get_cosine(vector1, vector2)
        # print ('Cosine:' + str(cosine))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
