""" 
inference
"""

def infer(payload_en, encoder, model):
    y_prob = model.predict_proba(payload_en)[:,1].round(3)
    return y_prob 