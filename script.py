'''
Dataset source: https://nlds.soe.ucsc.edu/sarcasm2

By Shereen Oraby, Vrindavan Harrison, Lena Reed, Ernesto Hernandez, Ellen Riloff and Marilyn Walker. "Creating and Characterizing a Diverse Corpus of Sarcasm in Dialogue." In The 17th Annual SIGdial Meeting on Discourse and Dialogue (SIGDIAL), Los Angeles, California, USA, 2016.
'''
import numpy as np
import pandas
import re

def main():
	data = clean_data()

def clean_data():
	'''
	Steps:
	1. Load data from csv file
	2. Remove unnecessary quotes
	3. Remove emoticons
	3. Fix all typos using Microsoft's Bing Spell Check API: https://www.microsoft.com/cognitive-services/en-us/bing-spell-check-api
	'''
	# step 1
	data = pandas.read_csv('sarcasm_v2.csv').as_matrix()
	# print(data.shape)
	data[:, 0] = np.array([find_category(x) for x in data[:, 0]])
	data[:, 1] = np.array([sarcasm(x) for x in data[:, 1]])
	# print(data[0,1]) # should be 1 for sarcasm

	# step 2
	data[:, 3] = np.array([clean_quotes(x) for x in data[:, 3]])
	data[:, 4] = np.array([clean_quotes(x) for x in data[:, 4]])

	# step 3
	data[:, 3] = np.array([remove_emoticons(x) for x in data[:, 3]])
	data[:, 4] = np.array([remove_emoticons(x) for x in data[:, 4]])

	return data

def find_category(category):
	return {
        'GEN': 0, # general
        'HYP': 1, # hyperbole
		'RQ': 2 # rhetorical question
    }[category]

def sarcasm(sarcasm_value):
	return {
		'sarc': 1, # true for sarcasm
		'notsarc': 0 # false for sarcasm
	}[sarcasm_value]

def get_data_index(ID):
	'''find the index of the data point. Corresponds to 1234 in GEN_sarc_1234 under ID in data.
	'''
	# TODO: given a string as shown in the comment, extract the number in it, possibly with regex.
        # Test

def clean_quotes(string):
	'''
	clean_quotes a string and removes beginning and closing quotation marks. Also replaces all duplicated double quotation marks with just one set of double quotation marks, e.g. ""hello"" with "hello"
	'''
	if string[0] == '"':
		string = string[1:] # first character
	if string[-1] == '"':
		string = string[:-1] # last character
	string = re.sub('\"\"', "\"", string)
	# triple quotes should not exist after removing first and last quotes from beginning and end, respectively, of the original string.
	# quadruple quotes will also be removed by replacing all duplicated double quotes "" with a single double quote ". This way, back-to-back duplicated double quotes (e.g. ""hello""""world"" will become "hello""world") will be taken care of as well.
	return string

def remove_emoticons(string):
	''' removes emoticons from the strings.'''
	

if __name__ == '__main__':
	main()
