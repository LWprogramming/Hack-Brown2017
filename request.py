'''
Code adapted from https://westus.dev.cognitive.microsoft.com/docs/services/TextAnalytics.V2.0/operations/56f30ceeeda5650db055a3c9
'''
import http.client, urllib.request, urllib.parse, urllib.error
import script
import numpy as np

def main():
    '''
    Sends a single POST request with a test bit of text.
    '''
    sample_text = 'I had a wonderful experience! The rooms were wonderful and the staff were helpful.' # from default given at https://www.microsoft.com/cognitive-services/en-us/text-analytics-api
    make_request(np.array([sample_text]))

def make_request(text_vector):
    '''
    Sends one request for each item in text_vector, which is a numpy vector. Careful not to exceed the API limit!
    '''
    headers = headers()
    params = urllib.parse.urlencode({})
    body = body_from_string_vectors(text_vector)
    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, str(body), headers)
        response = conn.getresponse()
        data = response.read()
        print(data) # score is on a scale from 0 to 1, with 0 being the most negative sentiment and 1 being the most positive sentiment. Includes some metadata.
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def body_from_string_vectors(vector):
    '''
    Takes in a numpy vector of strings, each string representing a separate quote from someone.
    '''
    body_documents_list = []
    for string in vector:
        body_documents_list += {
        'language': 'en',
        'id': '1',
        'text': string
        }
    body = {
        'documents': {
            body_documents_list
        }
    }

def generate_headers():
    api_key = script.get_api_key()
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': api_key
    }
    return headers

if __name__ == '__main__':
    main()
