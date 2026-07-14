import re
SLOTS={"Cardiology":["10:00 AM","1:30 PM","4:00 PM"],"Dermatology":["9:00 AM","11:00 AM"],
"General Medicine":["8:30 AM","2:00 PM","3:30 PM"],"Pediatrics":["10:30 AM","1:00 PM"],"Orthopedics":["11:30 AM"]}
def check_available_slots(department,requested_date=None):
    return {"department":department,"requested_date":requested_date or "requested day",
      "slots":SLOTS.get(department,SLOTS["General Medicine"]),"simulated":True}
def parse_appointment(question):
    dept=next((d for d in SLOTS if d.lower() in question.lower()),"General Medicine")
    day=next((d.title() for d in ["monday","tuesday","wednesday","thursday","friday"] if d in question.lower()),None)
    return dept,day
