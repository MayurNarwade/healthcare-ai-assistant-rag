def confidence(results):
    if not results:return "low","No relevant evidence was retrieved."
    scores=[x["relevance_score"] for x in results]
    if max(scores)>=.78 and len([x for x in scores if x>=.65])>=2:return "high","Multiple strong supporting passages were retrieved."
    if max(scores)>=.58:return "medium","Relevant supporting evidence was retrieved."
    return "low","Retrieved evidence was weak."
