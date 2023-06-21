""" 
One Hot encoder fucntion
"""
import pandas as pd

features_categorical = ['checkin_acc', 'credit_history',
       'savings_acc', 'present_emp_since', 'inst_rate', 'personal_status',
       'residing_since', 'inst_plans', 'num_credits', 'job',]

features_numerical = ['duration', 'amount', 'age',]

def encode(payload, encoder, X_cat=features_categorical, X_num=features_numerical ):
    data = pd.DataFrame([payload])
    X_num = data[X_num]
    X_cat = data[X_cat]

    X_cat_en = pd.DataFrame(data = encoder.transform(X_cat).toarray(), 
                            columns= encoder.get_feature_names_out())
    
    X_en = pd.concat([X_num, X_cat_en], axis=1)

    
    return X_en
    