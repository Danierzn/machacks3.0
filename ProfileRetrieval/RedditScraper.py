import requests
import time
import json

CLIENTID = 'xxx'
CLIENTSECRET = 'xxx'
def get_headers():
	
	#opens token file and finds the token and time of retrieval
	f = open('redditbearertoken','r')
	s = f.read()
	f.close()
	T = '' 	#token to read
	t = 0	#time to read
	
	if len(s) > 45:
		#token is from 0 to 44, 44 to l-1 is the time of retrieval
		T = s[0:44]
		t = float(s[45:(len(s)-1)]) 
		
	else:
		print('Token file empty, must be generated')
		
	
	
	# CLIENT_ID, SECRET_TOKEN
	auth = requests.auth.HTTPBasicAuth(CLIENTID, CLIENTSECRET)

	# here we pass our login method (password), username, and password
	data = {'grant_type': 'password', #remove once done
        	'username'	: 'xxx',
        	'password'	: 'xxx'}

	# setup our header info, which gives reddit a brief description of our app
	headers = {'saf': 'saf type 0.1'}

	# send our request for an OAuth token

	if (time.time() - t > 43200):
		TOKEN = T
		print('Token retrieved from file') #debug
		
	else:
		res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
		# convert response to JSON and pull access_token value
		TOKEN = res.json()['access_token']
		print('Bearer token generated')
		
		f = open('redditbearertoken','w') #debug
		f.write(TOKEN+str(time.time()))
		f.close()
		
	# add authorization to our headers dictionary
	headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
	return headers
	
def try_request(link, h, timeout):
	t = time.time()
	
	while (time.time() - t < timeout):
	
		try:
			res = requests.get(link, headers = h)
			
			if str(res) == '<Response [429]>':
				continue
				
		except:
			continue
			
		break
	
	return res

def format_selftext(txt):
	allow_chr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '
	s = ''
	for c in txt:
		if c in allow_chr:
			s = s + c
			
	return s
	
def user_posts_csv(username, filename): #retrieves and writes user posts as csv
	
	headers = get_headers()

	res = try_request('https://oauth.reddit.com/user/%s/submitted/' % username, headers,30) #attempts requests for 30s

	resjson = res.json()
	
	f = open(filename,'a')
	for post in resjson['data']['children']:

		s = post['data']['selftext']
		t = post['data']['created_utc']
		s = format_selftext(s)
		
		if len(s) > 0:
			f.write(s + ',' + str(t) + '\n')
	
	f.close()

# test: for dumping requests to file instead of repeatedly requesting
''' 
s = json.dumps(resjson, indent = 4)
print(resjson)
f = open('res.json','w')
f.write(s)
f.close()
'''
'''
f = open('res.json','r')
resjson = json.loads(f.read())
f.close()
'''

### Example Usage:
username = 'MNGrrl'
filename = 'posts.csv'
user_posts_csv(username,filename);
