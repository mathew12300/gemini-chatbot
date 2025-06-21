import google.generativeai as genai
from google.generativeai.types import GenerationConfig

# ✅ Set up Gemini API key
genai.configure(api_key="AIzaSyD_sxHzRaC9cWZy4-UbDyP-cwcDHMJyPDk")

# ✅ Create the model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# ✅ Generate content
response = model.generate_content(
    contents=[{"role": "user", "parts": ["Explain gravity simply."]}],
    generation_config=GenerationConfig(
        temperature=0.7,
        max_output_tokens=256
    )
)

print(response.text)
