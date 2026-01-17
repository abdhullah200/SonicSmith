import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# List of model names to try
model_names = [
    "gemini-pro",
    "models/gemini-pro",
    "gemini-1.5-pro",
    "models/gemini-1.5-pro",
    "gemini-1.5-flash",
    "models/gemini-1.5-flash",
    "gemini-1.5-pro-latest",
    "models/gemini-1.5-pro-latest",
    "gemini-1.5-flash-latest",
    "models/gemini-1.5-flash-latest",
]

print("Testing Gemini models...\n")

for model_name in model_names:
    try:
        from agno.models.google import Gemini
        model = Gemini(id=model_name, api_key=GOOGLE_API_KEY)
        
        # Try a simple test
        response = model.invoke("Say 'test successful'")
        print(f"✅ WORKS: {model_name}")
        print(f"   Response: {response}\n")
        break  # Stop at first working model
        
    except Exception as e:
        error_msg = str(e)[:100]  # First 100 chars of error
        print(f"❌ FAILED: {model_name}")
        print(f"   Error: {error_msg}...\n")

print("\n" + "="*50)
print("Test complete! Use the model that worked above.")