import pandas
import requests
import lxml.html 

url = "https://www.eurogamer.net/articles/2018-12-21-pokemon-go-type-chart-effectiveness-weaknesses"
page = requests.get(url)
contents = lxml.html.fromstring(page.content)
table_elements = contents.xpath('//tr')

t = [[T.text_content() for T in table_elements[i]] for i in range(len(table_elements))]
Titles = contents.xpath('//th')
Titles = [Title.text_content() for Title in Titles]
df = pandas.DataFrame(t,columns=Titles)
print(df)