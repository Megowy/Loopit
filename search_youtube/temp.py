from apiclient import discovery

api_key = 'AIzaSyByG2wn7WwPrea9_RMYeRejfVKi8yBf5xs'

youtube = discovery.build('youtube','v3',developerKey = api_key)

search ='andy timmons'
number_of_results = 10
request = youtube.search().list(q = search, part='snippet',type='video', maxResults=10)


result = request.execute()
print(type(result))

result_item = result['items']
print(type(result_item))


from pprint import PrettyPrinter
pp = PrettyPrinter()

pp.pprint(result)

result_item = result['items']
result_list = []
# for nr in range(0, number_of_results):
#
#     result_list.append( {"video_id": result_item[nr]['id']['videoId'],
#                        "video_thumbnail": result_item[nr]['snippet']['thumbnails']['medium']['url'],
#                        "title": result_item[nr]['snippet']['title'],
#                        "desription": result_item[nr]['snippet']['description']})
#
# print(result_list)