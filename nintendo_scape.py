import requests
import bs4

response = requests.get("https://www.yachtclubgames.com/blog/shovel-knight-live-steel-thy-shovel-concert/")
# print(response.text)

soup = bs4.BeautifulSoup(response.text, "html.parser")
# print(soup)
# print(soup.select(".title"))

n_headings = []

for item in soup.select(".title"):
    n_headings.append(item.text)

# print(headings)

import pandas as pd
heading_df = pd.DataFrame()
heading_df['n_headings'] = pd.Series(n_headings).values
# print(heading_df)
# print(heading_df["n_headings"].values)

heading_df.to_csv('n_headings.csv')