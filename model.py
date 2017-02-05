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
	reduced_data = data[0:20, :] # take the first 20 examples
	response = request.make_request()

if __name__ == "__main__":
	main()
