import pandas as pd
import plotly.express as px
df = pd.read_csv("pokemon.csv")

fig = px.scatter(df, x="Type 1", y="Type 2", color="Type 1", hover_name="Name", title="Pokémon Type 1 vs. Type 2")
fig.show()