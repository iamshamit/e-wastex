import os
from supabase import Client

url = os.environ.get("SUPABASE_URL", "")
key = os.environ.get("SUPABASE_KEY", "")
supabase = Client(url, key)

def fetch_parts():
  parts_data = supabase.from_("parts").select("*").execute().data
  parts_set = []
  for part in parts_data:
      parts_set.append({
          'id': part['id'],
          'name': part['name'],
          'price': "Rs " + str(part['price']),
          'quant': part['quant'],
          'image': part['image']
      })
  return parts_set