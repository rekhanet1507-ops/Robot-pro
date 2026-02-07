import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyBcE_Y325qlBW34YOeKLRvaQ9_y-xdFIdk")

# Use most compatible model
model = genai.GenerativeModel("models/gemini-2.5-flash")

print("🤖 Human-like AI Robot Started")
print("Ask me anything (type 'exit' to stop)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("🤖 Robot: Goodbye! Have a nice day 😊")
        break

    prompt = f"""
    You are a friendly robot assistant.
    Respond like a human in simple and clear language.
    Keep answers short and polite.

    User question: {user_input}
    """

    try:
        response = model.generate_content(prompt)

        if response.text:
            print("🤖 Robot:", response.text.strip())
        else:
            print("🤖 Robot: Sorry, I didn’t understand that.")

    except Exception as e:
        print("⚠️ Error:", e)
