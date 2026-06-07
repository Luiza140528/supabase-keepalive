import os
import time
import requests
from datetime import datetime

SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://risjmvmbppjbsmnsubwa.supabase.co")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

def ping_supabase():
    try:
        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}"
        }
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/municipios?limit=1",
            headers=headers,
            timeout=10
        )
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if response.status_code in [200, 206]:
            print(f"[{now}] ✅ Supabase OK - Status: {response.status_code}")
        else:
            print(f"[{now}] ⚠️ Supabase respondeu com status: {response.status_code}")
    except Exception as e:
        print(f"[{datetime.now()}] ❌ Erro ao pingar Supabase: {e}")

if __name__ == "__main__":
    print("🚀 Supabase Keepalive iniciado")
    print(f"📡 Projeto: {SUPABASE_URL}")
    print(f"⏰ Ping a cada 4 dias")

    while True:
        ping_supabase()
        time.sleep(4 * 24 * 60 * 60)
