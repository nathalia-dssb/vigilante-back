from google import genai

client = genai.Client(api_key="Ask for the api key")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Write how termodinamics works in 10 words"
)
print(response.text)