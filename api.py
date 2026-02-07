import google.generativeai as genai

genai.configure(api_key="AIzaSyBcE_Y325qlBW34YOeKLRvaQ9_y-xdFIdk")

models = genai.list_models(models/gemini-2.5-flash)

print("Available Gemini Models:\n")
for model in models:
    print(model.name)
