from google import genai

client = genai.Client(api_key="XXXXXXXXX") # HIDDEN RETROACTIVELY

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["Is this system run locally?"]
)
print(response.text)
