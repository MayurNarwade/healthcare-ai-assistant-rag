import re
def normalize_text(text:str)->str: return re.sub(r"\s+"," ",text).strip()
def excerpt(text:str,n=320)->str: return text if len(text)<=n else text[:n].rsplit(" ",1)[0]+"..."
