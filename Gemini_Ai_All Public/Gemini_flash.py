import google.generativeai as genai

genai.configure(api_key="u r api key here")
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 8192,
    # "response_mime_type": "text/plain",

}
# history = []
model = genai.GenerativeModel("gemini-1.5-flash", generation_config=generation_config)
inp  = input("enter")
res = model.generate_content(inp)
# print(res.text)
for chunk in res:
    print(chunk.text, end="", flush=True)
# chat = model.start_chat(history=history)