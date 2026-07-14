.PHONY: install run ingest ui test evaluate
install:
	pip install -r requirements.txt
run:
	uvicorn app.main:app --reload
ingest:
	python scripts/ingest_documents.py
ui:
	streamlit run frontend/streamlit_app.py
test:
	pytest -q
evaluate:
	python evaluation/evaluate.py
