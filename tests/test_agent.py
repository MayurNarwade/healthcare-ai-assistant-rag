from app.agent import route_intent,appointment_response
def test_routes():
 assert route_intent("Diagnose my headache")=="safety"
 assert route_intent("Book a cardiology appointment Monday")=="appointment_tool"
 assert route_intent("What is the refill policy?")=="rag"
def test_mock_tool():
 r=appointment_response("Book cardiology Monday")
 assert r["tool"]["simulated"] is True and "not real bookings" in r["answer"]
