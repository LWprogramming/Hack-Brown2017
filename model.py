import ipdb
import data_clean
import request

'''
Model for determining whether a given piece of input text is sarcastic or not.
'''

def main():
	data = data_clean.clean_data()
	# print(data.shape) # should be (4692, 5)
	# ipdb.set_trace()  ######### Break Point ###########
	reduced_data = data[0:2, :] # take the first 20 examples
	reduced_quotes = reduced_data[:, 3]
	reduced_response = reduced_data[:, 4]
	# quotes_value = request.make_request(reduced_quotes)
	# response_value = request.make_request(reduced_response)
	quotes_value = b'{"documents":[{"score":0.8677991,"id":"0"},{"score":0.9363753,"id":"1"}],"errors":[]}'
	response_value = b'{"documents":[{"score":0.9520152,"id":"0"},{"score":0.4560984,"id":"1"}],"errors":[]}'
	print(quotes_value)
	print(response_value)

if __name__ == "__main__":
	main()
