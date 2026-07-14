from app.confidence import confidence
def test_confidence_levels():
 assert confidence([])[0]=="low"
 assert confidence([{"relevance_score":.8},{"relevance_score":.7}])[0]=="high"
 assert confidence([{"relevance_score":.6}])[0]=="medium"
