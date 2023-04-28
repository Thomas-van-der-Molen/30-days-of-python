import json
import re
import csv
#file handling


with open("afile.txt", "r") as speech:
    line_count = speech.readlines()
    print(len(line_count))

with open("afile.txt", "r") as speech:
    word_count = speech.read().split(" ")
    print(len(word_count))#split the contents at each space to count the words

def findMostSpokenLanguages(file, num_languages):
    languages = {}
    sorted_langs = []
    with open(file, "r") as my_file:
        a_dict = json.loads(my_file.read())
        #nested for loop counts the occurrence of each language
        for country in a_dict:
            for language in country["languages"]:
                if language not in languages:
                    languages[language] = 0
                else:
                    languages[language] += 1
        sorted_langs = list(languages)#convert dict to list
        #bubble sort the languages
        for x in range(len(sorted_langs) - 1):
            for y in range(len(sorted_langs) - 1):
                if languages[sorted_langs[y]] < languages[sorted_langs[y+1]]:
                    temp = sorted_langs[y+1]
                    sorted_langs[y+1] = sorted_langs[y]
                    sorted_langs[y] = temp
    return sorted_langs[:num_languages]
        

print(findMostSpokenLanguages("countriesdata.json",3))
print(findMostSpokenLanguages("countriesdata.json",10))

def mostPopulatedCountries(file, num_countries):
    populations = {}
    sorted_pops = []
    with open(file, "r") as my_file:
        a_dict = json.loads(my_file.read())
        #nested for loop counts the occurrence of each language
        for country in a_dict:
            populations[country["name"]] = country["population"]
        sorted_pops = list(populations)#convert dict to list
        #bubble sort the languages
        for x in range(len(sorted_pops) - 1):
            for y in range(len(sorted_pops) - 1):
                if populations[sorted_pops[y]] < populations[sorted_pops[y+1]]:
                    temp = sorted_pops[y+1]
                    sorted_pops[y+1] = sorted_pops[y]
                    sorted_pops[y] = temp
    return sorted_pops[:num_countries]

print(mostPopulatedCountries("countriesdata.json",3))
print(mostPopulatedCountries("countriesdata.json", 10))    


def count_words(file, num_words):
    #the time complexity is way too high
    ret = []
    read_words = []
    with open(file,"r") as input_file:
        contents = input_file.read()
        contents = contents.split(" ")
        #get unique words
        for word in contents:
            if word not in read_words and word != '':
                read_words.append(word)
        #count unique words
        for word in read_words:
            ret.append((word, contents.count(word)))

        #bubble sort words
        for i in range(len(ret)-1):
            for j in range(len(ret)-1):
                if ret[j][1] < ret[j+1][1]:
                    temp = ret[j+1]
                    ret[j+1] = ret[j]
                    ret[j] = temp

    return ret[:num_words]

#print(count_words("sample.txt", 10))

def csv_exercise():
    with open("hacker_news.csv") as my_csv:
        csv_reader = csv.reader(my_csv, delimiter = ',')
        line_count = 0
        python = 0
        javascript = 0
        java = 0
        for row in csv_reader:
            title = row[1]
            if "Python" in title or "python" in title:
                python +=1
            if "Javascript" in title or "javascript" in title or "JavaScript" in title:
                javascript+=1
            if "Java" in title and "JavaScript" not in title:
                java +=1
        print(python)
        print(javascript)
        print(java)

csv_exercise()


