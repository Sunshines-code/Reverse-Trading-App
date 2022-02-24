import pandas as pd 
df = pd.read_csv('./assets/Resources/data/cities.csv')
html = df.to_html()
  
# write html to file
text_file = open("data.html", "w")
text_file.write(html)
text_file.close()