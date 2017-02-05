import ipdb
import data_clean
import request
import re
import numpy as np
from sklearn import SGDClassifier

'''
Model for determining whether a given piece of input text is sarcastic or not.
'''

def main():
	'''
		# for just the first two examples, this applies
		# # quotes_value = request.make_request(reduced_quotes)
		# # response_value = request.make_request(reduced_response)
		# quotes_value = b'{"documents":[{"score":0.8677991,"id":"0"},{"score":0.9363753,"id":"1"}],"errors":[]}'
		# response_value = b'{"documents":[{"score":0.9520152,"id":"0"},{"score":0.4560984,"id":"1"}],"errors":[]}'
		# print(quotes_value)
		# print(response_value)
	'''
	data = data_clean.clean_data()
	# print(data.shape) # should be (4692, 5)
	# ipdb.set_trace()  ######### Break Point ###########
	reduced_data = data[0:2, :] # take the first 20 examples
	reduced_quotes = reduced_data[:, 3]
	reduced_response = reduced_data[:, 4]
	save_data(reduced_data[:, 1], reduced_quotes, reduced_response, 'training_data')
	classifier = train()

	clf = SGDClassifier(loss="hinge", penalty="l2")
	

def train():
	file_name = 'training_data.csv'
	data = pandas.read_csv('sarcasm_v2.csv').as_matrix()
	labels = data[:, 0]
	features = data[:, 1:]
	clf = SGDClassifier(loss="hinge", penalty="l2")
	clf.fit(features, labels)
	return clf

def save_data(labels, quotes_vector, response_vector, file_name):
	'''creates a csv with some number of rows with 3 columns--the first being the label for the training example, the second as the sentiment value for the quote, and the third being the sentiment value for the response. Saves the csv file.
	'''
	num_examples = labels.size # should be same as quotes or response vector length
	quote_sentiment_vector = request.make_request(quotes_vector).decode('utf-8')
	response_sentiment_vector = request.make_request(response_vector).decode('utf-8')
	quote_sentiment_vector = np.array(re.findall('0\.[0-9]+', quote_sentiment_vector))
	response_sentiment_vector = np.array(re.findall('0\.[0-9]+', response_sentiment_vector))
	quote_sentiment_vector = np.array([float(x) for x in quote_sentiment_vector])
	response_sentiment_vector = np.array([float(x) for x in response_sentiment_vector]) # change strings to numbers
	labels = labels.reshape(num_examples, 1)
	quote_sentiment_vector = quote_sentiment_vector.reshape(num_examples, 1)
	response_sentiment_vector = response_sentiment_vector.reshape(num_examples, 1)

	# TODO: fix this
	# # now adding polynomial features of up to degree 5.
	# features = np.zeros((num_examples, 10))
	# for i in range(5):
	# 	features[i] = quote_sentiment_vector ** i
	# 	features[10 - i - 1] = response_sentiment_vector ** i
	# data = np.concatenate((labels, quote_sentiment_vector, response_sentiment_vector, features), axis=1)

	data = np.concatenate((labels, quote_sentiment_vector, response_sentiment_vector), axis=1)
	data = data.reshape(data.size / 3, 3)
	print(data)
	np.savetxt(file_name + '.csv', data, delimiter=',')


if __name__ == "__main__":
	main()
