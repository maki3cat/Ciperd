import time
from google import genai
from prompt import generate_prompt

api_key = ""
client = genai.Client(api_key=api_key)
# model = "gemini-2.0-flash-live-001"
model = "gemini-2.0-flash-001"
config = {"response_modalities": ["TEXT"]}

if __name__ == "__main__":
    with open("data2_gemini_api_9.txt", "a") as f:
        for id in range(1000):
            print(f"Generating {id}...")
            prompt, label = generate_prompt()
            prompt_line = f"\n{label} # {prompt}\n"
            f.write(prompt_line)
            response = client.models.generate_content(
                model=model, config=config, contents=prompt)
            response_line = f"{response.text}\n"
            f.write(response_line)
            time.sleep(4)
# 15 RPM
