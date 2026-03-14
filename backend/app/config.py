import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DATABASE_URL = os.getenv(
"DATABASE_URL",
"postgresql://admin:admin@localhost:5432/context_ai"
)
