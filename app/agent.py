import re,time
from app.tools import check_available_slots,parse_appointment
SAFETY=["diagnose","diagnosis","what disease","what should i take","change my dose","stop my medication","chest pain","overdose","suicidal"]
APPT=["book","appointment","available slot","availability","schedule a"]
def route_intent(q):
    x=q.lower()
    if any(k in x for k in SAFETY):return "safety"
    if any(k in x for k in APPT):return "appointment_tool"
    return "rag"
def safety_response():
    return {"answer":"This assistant provides document-based policy information only and cannot diagnose conditions or provide individualized treatment. Please contact a qualified healthcare professional. If symptoms may be urgent or life-threatening, contact local emergency services immediately.","sources":[],"confidence":"high","confidence_reason":"Healthcare safety routing was activated.","route":"safety","grounded":False,"response_time_ms":0.0,"tool":None}
def appointment_response(q):
    start=time.perf_counter(); dept,day=parse_appointment(q); result=check_available_slots(dept,day)
    slots=", ".join(result["slots"])
    return {"answer":f"I checked the simulated appointment schedule. {dept} has mock availability for {day or 'the requested day'} at {slots}. These are demonstration slots only and are not real bookings.","sources":[],"confidence":"high","confidence_reason":"The deterministic mock scheduling tool returned availability.","route":"appointment_tool","grounded":True,"response_time_ms":round((time.perf_counter()-start)*1000,2),"tool":{"name":"check_available_slots","simulated":True}}
