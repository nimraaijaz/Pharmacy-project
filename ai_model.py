import google.generativeai as genai
prompt = input("Enter your prompt: ")
genai.configure(api_key="AIzaSyCZsPpcwGXJohwFG70QlmPXALnqSgcoeJQ")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(prompt)
print(response.text)