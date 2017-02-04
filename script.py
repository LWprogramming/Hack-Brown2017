import numpy as np
import pandas

def main():
	data = pandas.read_csv('sarcasm_v2.csv').as_matrix()
	# print(data.shape)
	data[:, 0] = np.array([find_category(x) for x in data[:, 0]])
	data[:, 1] = np.array([sarcasm(x) for x in data[:, 1]])
	# print(data[0,1]) # should be 1 for sarcasm

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
if __name__ == '__main__':
	main()
