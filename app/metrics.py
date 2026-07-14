from threading import Lock
class Metrics:
 def __init__(self): self.lock=Lock(); self.d={"total_questions":0,"rag_requests":0,"appointment_tool_requests":0,"safety_requests":0,"unknown_answers":0,"total_response_time_ms":0.0,"ingestion_runs":0,"errors":0}
 def question(self,r):
  with self.lock:
   self.d["total_questions"]+=1; self.d[r["route"]+"_requests"]+=1; self.d["total_response_time_ms"]+=r["response_time_ms"]
   if r["route"]=="rag" and not r["grounded"]:self.d["unknown_answers"]+=1
 def ingestion(self): self.d["ingestion_runs"]+=1
 def error(self): self.d["errors"]+=1
 def snapshot(self):
  x=dict(self.d); n=x["total_questions"]; x["average_response_time_ms"]=round(x.pop("total_response_time_ms")/n,2) if n else 0.0; return x
metrics=Metrics()
