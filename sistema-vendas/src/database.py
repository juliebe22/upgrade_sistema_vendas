import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

url = os.getenv("SUPABASE_URL")
chave = os.getenv("SUPABASE_KEY")

if not url or not chave:
    raise ValueError(
        "Configure SUPABASE_URL e SUPABASE_KEY no arquivo .env"
    )

supabase = create_client(url, chave)
