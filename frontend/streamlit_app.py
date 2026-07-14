import os,requests,streamlit as st
API=os.getenv("API_BASE_URL","http://localhost:8000")
st.set_page_config(page_title="Healthcare AI Assistant",page_icon="🏥",layout="wide")
st.title("🏥 Healthcare AI Assistant"); st.caption("Grounded answers from approved healthcare documents")
st.warning("Document-based policy information only. This prototype does not provide diagnosis, treatment, or emergency care.")
examples=["Can a patient request a medication refill through telehealth?","How can a patient request a copy of their records?","What identification is required during a telehealth visit?","Can I book a cardiology appointment for Monday?","Does the policy explain dental implant coverage?"]
if "q" not in st.session_state:st.session_state.q=""
choice=st.selectbox("Example questions",[""]+examples)
if choice:st.session_state.q=choice
q=st.text_area("Your question",key="q")
c1,c2=st.columns(2)
ask=c1.button("Ask",type="primary",use_container_width=True)
if c2.button("Clear",use_container_width=True):st.session_state.q="";st.rerun()
if ask:
 if not q.strip():st.error("Enter a question.")
 else:
  try:
   with st.spinner("Searching the knowledge base..."):r=requests.post(f"{API}/ask",json={"question":q},timeout=130)
   if not r.ok:st.error(r.json().get("detail",{}).get("message","Request failed."))
   else:
    d=r.json();st.subheader("Answer");st.write(d["answer"])
    a,b,c=st.columns(3);a.metric("Confidence",d["confidence"].title());b.metric("Route",d["route"]);c.metric("Latency",f'{d["response_time_ms"]:.0f} ms')
    st.caption(d["confidence_reason"])
    if d.get("tool"):st.info("Mock tool used; no real appointment was booked.")
    for src in d["sources"]:
     with st.expander(f'{src["document"]} · relevance {src["relevance_score"]:.2f}'):st.write(src["excerpt"]);st.caption(src["chunk_id"])
  except requests.RequestException:st.error("Cannot connect to the API. Confirm that FastAPI is running.")
