from dotenv import load_dotenv
import os

load_dotenv()

bot_token = os.getenv('TOKEN')
supabase_url: str = os.getenv("SUPABASE_URL")
supabase_key: str = os.getenv("SUPABASE_KEY")