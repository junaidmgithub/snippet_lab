from rest_framework.utils.urls import remove_query_param, replace_query_param


url = 'http://www.google.com/abcd/?name=junaid&location=palakkal'

new_url = replace_query_param(url, 'name', 'javas')
print(new_url)

new_url = replace_query_param(new_url, 'location', 'thalappara')
print(new_url)

new_url = remove_query_param(new_url, 'location')
print(new_url)
