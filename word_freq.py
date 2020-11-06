"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""
import os
import gensim
from gensim.parsing.preprocessing import remove_stopwords
import argparse
import collections

COUNT_WORDS = 100
def count_top_words(file_name, limit):
    with open(file_name, "r", encoding="UTF-8") as file:
        words = []
        for line in file:
            line = remove_stopwords(line.strip().lower())
            words += line.split()

    top_list = collections.Counter(words).most_common(limit)
    print(top_list)

if __name__ == '__main__':
    stop_words = stopwords.words('english') + stopwords.words('russian')
    parser = argparse.ArgumentParser(description='Напишите имя файла, который хотите проверить')
    parser.add_argument('file_path', nargs='?', default='my_file.txt')
    file_path = parser.parse_args().file_path
    if os.path.isfile(file_path) and os.path.getsize != 0: 
            count_top_words(file_path, COUNT_WORDS)
    else:
            print("Файл отсутствует")
    