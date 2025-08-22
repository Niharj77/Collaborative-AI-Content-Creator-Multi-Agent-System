# In a real project, you would use environment variables instead of hardcoding API keys.
# Example: os.environ.get("OPENAI_API_KEY")

class Config:
    """Configuration class for API keys and settings."""
    OPENAI_API_KEY = "your_openai_api_key_here"
    SERPAPI_API_KEY = "your_serpapi_api_key_here"
