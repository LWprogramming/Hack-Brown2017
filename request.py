'''
Code adapted from https://westus.dev.cognitive.microsoft.com/docs/services/TextAnalytics.V2.0/operations/56f30ceeeda5650db055a3c9
'''
import http.client, urllib.request, urllib.parse, urllib.error
import script

def main():
    api_key = script.get_api_key()
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': api_key
    }
    params = urllib.parse.urlencode({})
    body = {
    	"documents": [
    		{
    		"language": "en",
    		"id": "1",
    		"text": "I had a wonderful experience! The rooms were wonderful and the staff were helpful."
    		}
    	]
    }
    try:
    	conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    	conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, str(body), headers)
    	response = conn.getresponse()
    	data = response.read()
    	print(data) # score is on a scale from 0 to 1, with 0 being the most negative sentiment and 1 being the most positive sentiment. Includes some metadata.
    	conn.close()
    except Exception as e:
    	print("[Errno {0}] {1}".format(e.errno, e.strerror))

if __name__ == '__main__':
    main()
