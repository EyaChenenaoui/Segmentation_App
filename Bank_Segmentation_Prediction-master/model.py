# Importing necessary libraries
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

# Importing the dataset
data = pd.read_excel('output.xls',index_col=0)
logreg = pickle.load(open('model.pkl','rb'))


# Dictionary containing the mapping
variety_mappings = {0: 'NS', 1: 'SALARIE HAUT CADRE', 2: 'RETRAITE',3:'RENTIER'
,4:'JEUNE',5:'TRE SALARIE',6:'PERSONNEL',7:'INACTIF',8:'PERSONNEL ATTIJARI INACTIF',21:'PROFESSIONNEL LIBERALE',22: 'ARTISAN',23: 'COMMERCANT', 24: 'AGRICULTEUR',25:'AUTRE'
,41:'ASSOCIATION ET AMBASSADES',42:'COOPERATIVE',43:'ENTREPRISE NON RESIDENTE',44:'MICRO-ENTREPRISE  ',
51:'TRE PROFESSIONNEL',52:'TRE RETRAITE',53: 'TRE INACTIF',61: 'PME', 62: 'GEI',63:'PROFESSIONNEL BE'
,101:'SALARIE CADRE MOYEN',102:'SALARIE AGENT D EXECUTION',106:'PERSONNEL DU COMEX',211:'PROFESSIONNEL SANTE'
}

# Function for classification based on inputs
def classify(a,b,c,d,e,f,g,h,i):
   
    # StandardScaler featurs
    Stand_features =np.array([a, b, c, d, e,f]).reshape(1, -1)
    my_patient_data_X = StandardScaler().fit_transform(Stand_features) 

    # Dummies features
    model_columns = data.iloc[:,7:].columns
    rr = np.array([g, h, i]).reshape(1,-1)
    Stand_features =pd.DataFrame(rr,columns=['CLT_SECTEUR_ACTIVITE','CLT_VILLE_NAISSANCE','CLT_TYPE_P_IDENT'])
    query  = pd.get_dummies(Stand_features)
    query = query.reindex(columns=model_columns, fill_value=0)

    # Conbine all array Convert to numpy array
    out_arr = np.append(my_patient_data_X, query) 

    # Change the data type to float
    out_arr = out_arr.astype(np.float64) 

    print(out_arr)

    prediction = variety_mappings [logreg.predict(out_arr.reshape(1, -1))[0]]
    print(prediction)

    return prediction # Return the prediction


# Function for classification based on inputs
def classifyNum(a,b,c,d,e,f,g,h,i):
   
    # StandardScaler featurs
    Stand_features =np.array([a, b, c, d, e,f]).reshape(1, -1)
    my_patient_data_X = StandardScaler().fit_transform(Stand_features) 

    # Dummies features
    model_columns = data.iloc[:,7:].columns
    rr = np.array([g, h, i]).reshape(1,-1)
    Stand_features =pd.DataFrame(rr,columns=['CLT_SECTEUR_ACTIVITE','CLT_VILLE_NAISSANCE','CLT_TYPE_P_IDENT'])
    query  = pd.get_dummies(Stand_features)
    query = query.reindex(columns=model_columns, fill_value=0)

    # Conbine all array Convert to numpy array
    out_arr = np.append(my_patient_data_X, query) 

    # Change the data type to float
    out_arr = out_arr.astype(np.float64) 

    print(out_arr)

    prediction = logreg.predict(out_arr.reshape(1, -1))[0]
    print(prediction)

    return prediction # Return the prediction

