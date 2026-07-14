import json,requests,time,os
API=os.getenv("API_BASE_URL","http://localhost:8000")
data=json.load(open("evaluation/evaluation_dataset.json",encoding="utf-8")); rows=[]
for x in data:
 t=time.perf_counter()
 try:
  d=requests.post(API+"/ask",json={"question":x["question"]},timeout=130).json()
  rows.append({"id":x["id"],"route_ok":d.get("route")==x["expected_route"],"citation_ok":all(s in [z["document"] for z in d.get("sources",[])] for s in x["expected_sources"]),"unknown_ok":x["expected_answerable"] or not d.get("grounded",True),"latency_ms":round((time.perf_counter()-t)*1000,2),"error":False})
 except Exception as e:rows.append({"id":x["id"],"error":True,"message":str(e)})
n=len(rows);print("Route accuracy:",sum(r.get("route_ok",0) for r in rows)/n);print("Citation match:",sum(r.get("citation_ok",0) for r in rows)/n);print("Errors:",sum(r["error"] for r in rows))
json.dump(rows,open("evaluation/evaluation_results.json","w"),indent=2)
