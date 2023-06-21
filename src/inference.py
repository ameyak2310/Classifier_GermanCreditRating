""" 
inference
"""

def infer(payload_en, model):
    y_prob = model.predict_proba(payload_en)[:,1]
    return y_prob 