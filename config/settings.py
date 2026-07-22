from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

CHROMA_DB_PATH = "chroma_db"

DATA_FOLDER = "data"