from config import supabase_key, supabase_url
from supabase import create_client, Client

supabase: Client = create_client(supabase_url, supabase_key)


async def get_recommendations():
    response = supabase.table('recommendations').select("body").execute()
    return response.data
