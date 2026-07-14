import requests,os
url=os.getenv("API_BASE_URL","http://localhost:8000")
r=requests.post(f"{url}/ingest",json={"reset":False},timeout=300);r.raise_for_status();print(r.json())
