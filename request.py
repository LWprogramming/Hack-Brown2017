########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64
import script

api_key = script.get_api_key()
# print(type(api_key))

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

# print('reached point 0')
# print(type(body))
# print(str(body))
try:
	conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
	# print('reached point 1')
	conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, str(body), headers)
	# print('reached point 2')
	response = conn.getresponse()
	data = response.read()
	# print('reached point 3')
	print(data)
	# print('reached point 4')
	conn.close()
except Exception as e:
	print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
