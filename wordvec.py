# -*- coding: utf-8 -*-

from gensim.models import Word2Vec
from pythainlp.tokenize import word_tokenize

def main():
    try:
        with open('assets/type_1/removal_output.txt', 'r', encoding='utf8') as source:
            contents = source.readlines()
            contents = [''.join(content.strip().split('|')) for content in contents]

        tokenized_contents = [list(word_tokenize(content)) for content in contents]
        model = Word2Vec(tokenized_contents, min_count=1)
        result = model.similar_by_word('รายจ่าย')
        print(result)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
