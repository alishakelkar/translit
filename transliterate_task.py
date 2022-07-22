import numpy
import pandas as pd
import csv
import os
import sys
import argparse

parser=argparse.ArgumentParser(description='Transliterates words from English-Hindi. Example command: python3 transliterate_task.py /Path/to/input.csv /path/to/output.csv lang_code')
parser.add_argument("input path", help= "input csv path")
parser.add_argument("output path", help="path for output csv")
parser.add_argument("language code", help="translit lang code")

args = parser.parse_args()


def file_exists_exception():
    if not os.path.isfile(sys.argv[1]):
        print("Invalid input path")
    # if not os.path.exists(sys.argv[2])
    

def main():
    file_exists_exception()
    # input_csv_exception()
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    lang_code = sys.argv[3]

    df = pd.read_csv(input_path, names = ['English text'])
    words = set()
    df['English text'].str.lower().str.split().apply(words.update)
    words = [word.strip('0123456789') for word in words]

    #finding unique
    unique = []
    for word in words:
        if word not in unique:
            unique.append(word)

    #sort
    unique.sort()

    unique_with_space = []
    for i in unique:
        my_str = i
        result = ' '.join(my_str)
        unique_with_space.append(result)
    
    df = pd.DataFrame(unique_with_space, columns=['Text'])
    # df.to_csv('/datadrive/translit/IndicXlit/IndicXlit/inference/cli/source/source.txt',index=False)
    df.to_csv('source/source.txt',index=False)
    cmd = "bash transliterate_word.sh "
    returned_value = os.system(cmd + "'"+lang_code+"'") 

    eng_dictionary = {}
    with open("output/final_transliteration.txt") as file:
        for line in file:
            (key, value) = line.split()
            eng_dictionary[str(key).replace(':', '')] = value
    
    filename = sys.argv[1]
    input_list = []
    output_list = []


    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            input_list.append(row[0])
            input = row[0].split()

            # print(input)

            combine = []
            for i in input:
                lower_input = i.lower()
                # print(lower_input)
                if lower_input in eng_dictionary:
                    combine.append(eng_dictionary[lower_input])
                    # print(i, ':', eng_dictionary[lower_input])      
            output_list.append(' '.join(combine))

    with open(output_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(zip(input_list, output_list))


if __name__ == "__main__":
    file_exists_exception()
    main()

