import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("Status code: ",r.status_code)

response_dict=r.json()

print(response_dict.keys())
print("total_count: ",response_dict['total_count'])

repo_dicts=response_dict['items']
print(len(repo_dicts))

print("\nSelected information about each repository:")
repo_dict=repo_dicts[0]
print("keys:",len(repo_dict))
for key in sorted(repo_dict.keys()):
	print(key)