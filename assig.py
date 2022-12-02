# importing requests package
import requests	

def StoryTimes():
	
	# Times.com api
	# following query parameters are used
	# source, sortBy and apiKey
	query_params = {
	"source": "times-story",
	"sortBy": "top",
	"apiKey": "4dbc17e007ab436fb66416009dfb59a8"
	}
	main_url = " https://time.com/"

	# fetching data in json format
	res = requests.get(main_url, params=query_params)
	open_times_page = res.json()

	# getting all story in a string story
	article = open_bbc_page["story"]

	# empty list which will
	# contain all trending story
	results = []
	
	for ar in story:
		results.append(ar["title"])
		
	for i in range(len(results)):
		
		# printing all trending story
		print(i + 1, results[i])

	#to read the news out loud for us
	from win32com.client import Dispatch
	speak = Dispatch("SAPI.Spvoice")
	speak.Speak(results)				

# Driver Code
if __name__ == '__main__':
	
	# function call
	StoryTimes()
