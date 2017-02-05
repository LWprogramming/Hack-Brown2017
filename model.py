import ipdb
import data_clean
import request
import re
import numpy as np

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
	save_training_data(reduced_data[:, 1], reduced_quotes, reduced_response)

def save_training_data(labels, quotes_vector, response_vector):
	'''creates a csv with some number of rows with 3 columns--the first being the label for the training example, the second as the sentiment value for the quote, and the third being the sentiment value for the response. Saves the csv file.
	'''
	num_examples = labels.size # should be same as quotes or response vector length
	quote_sentiment_vector = request.make_request(quotes_vector).decode('utf-8')
	response_sentiment_vector = request.make_request(response_vector).decode('utf-8')
	quote_sentiment_vector = np.array(re.findall('0\.[0-9]+', quote_sentiment_vector))
	response_sentiment_vector = np.array(re.findall('0\.[0-9]+', response_sentiment_vector))
	quote_sentiment_vector = np.array([float(x) for x in quote_sentiment_vector])
	response_sentiment_vector = np.array([float(x) for x in response_sentiment_vector]) # change strings to numbers
	data = np.concatenate((labels.reshape(num_examples, 1), quote_sentiment_vector.reshape(num_examples, 1), response_sentiment_vector.reshape(num_examples, 1)), axis=1)
	data = data.reshape(data.size / 3, 3)
	np.savetxt('training_data.csv', data, delimiter=',')
	return data

if __name__ == "__main__":
	main()
