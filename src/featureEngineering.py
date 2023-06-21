""" 
One Hot encoder fucntion
"""
import pandas as pd

def encode(data, X_cat, X_num, encoder):
    X_num = data[X_num]
    X_cat = data[X_cat]

    X_cat_en = pd.DataFrame(data = encoder.transform(X_cat).toarray(), 
                            columns= encoder.get_feature_names_out())
    
    X_en = pd.concat([X_num, X_cat_en], axis=1)

    
    return X_en
    