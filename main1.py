import pandas as pd
import plotly.express as px

df = pd.read_csv("pokemon.csv")
top_hp_pokemon = df.nlargest(10, "HP")

fig = px.bar(
    top_hp_pokemon, 
    x="Name", 
    y="HP", 
    color="Type 1",  
    title="Top 10 Pokémon with Highest HP",
    labels={"HP": "HP value", "Name": "Pokemon"},
)

fig.show()