from litellm import completion
import os

os.environ["GEMINI_API_KEY"] = "AIzaSyDlG8CHj5ht782edcYg5MfeTVsrMc05tUo"

def gemini():
    response = completion(
        model = "gemini/gemini-1.5-flash",
        messages = [
            {"role": "user", "content": "Hello, how are you?"}
        ]
    )
    
    print(response["choices"][0]["message"]["content"])

gemini()