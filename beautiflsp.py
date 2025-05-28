import re
from urllib.request import urlopen

url = "https://es.wikipedia.org/wiki/Historia_de_M%C3%A9xico"
page = urlopen(url)
page
html_bytes = page.read()
html = html_bytes.decode("utf-8")
pattern = "<html.*?>.*?</html.*?>"
match_results = re.search(pattern,html, re.IGNORECASE)

str(all)
all = re.sub("<.*?>","",all)

print(all)

#title_index = html.find ("<title>")
#title_index

#start_index = title_index + len("<title>")
#start_index

#end_index = html.find("</title>")
#end_index

#title = html[start_index:end_index]
#title
#print(title)
