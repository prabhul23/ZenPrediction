import sklearn
import streamlit as st
import pandas as pd
import numpy as np
import pickle
# mapped data
mapping_dict = {'Yes': 1, 'No': 0,'No Experience':0,'Less than one':1,'one year':2,'two years':3,'three years':4,'four years':5,'More than 5':6,
                'Not Applicable':0,'Less than 3LPA':1,'3-5LPA':2,'5.1-7LPA':3,'7.1-10 LPA':4,'> 10 LPA':5,
                '12 - 16 Hours (Per week)':2,'8 Hours (Per week)':1,'<8 Hours (Per week)':0,'Engineering':0,'Non-Engineering':1,
                '20-30k':1,'Less than 20k':0,'31-50k':2,'Above 70k':4,'51-70k':3,
                'BE/B.Tech':0,'B.Sc':1,'B.Com':2,'BCA':3,'Diploma':4,'BA':5,'BBA':6,'B.Arch':7,'School':0,'Under Graduate':2,'Post Graduate':3,
                '300-579':0,'580-669':1,'670-739':2,'740-799':3,'800-850':4,
                'Very Basic(Dont Know how to Code, Need to Start from Scratch)':0,'Basic(Know Basics of Coding)':1,'Intermediate(Know Coding but not advance level )':2,'Advanced(Very Good in Coding )':3,
                'Working in Non-IT':2,'Graduate looking for the job':1,'Working in IT':3,'Student':0,
                'No Coding experience':0,'Basic Looping':1,'Basic DS ( Array, LL, Stack, Q)':2,'Nested/2D arrays':3,'File-handling':4,'Dropped':1,'Ongoing':2,"Completed":3,
                'Friend':0,'Google search':1,'Instagram':2,'YouTube':3,'Google Ads':4,'Facebook':5,'Employee referred':6,'LinkedIn':7,
                'Direct - Full Payment':1,'Direct - Partial Payment':2,'Emandate - Propelld':0,'EMI - 3 Month':3,'EMI - 6 Month':4,'EMI - 9 Month':5,'EMI - 12 Month':6,
                'drop':0,'conv':1
                }

user_input = {}


@st.cache_data
def load_model():
    model = pickle.load(open("ZenClass (1).pkl", "rb"))
    return model
feature_names = pickle.load(open("Featurenames (1).pkl", "rb"))

st.title("Zen Class Prediction App")

# 10th marks
marks_10 = st.slider('How much did you score in 10th?(Percentage)', 0, 100, 60)
user_input['10 Marks'] = [marks_10]

# 12th marks
marks_12 = st.slider('How much did you score in 12th?(Percentage)', 0, 100, 60)
user_input['12th Marks (In Percentage)'] = [marks_12]

# Coding experience
coding = st.selectbox('How much coding experience do you have (in years)?', ('No Experience','Less than one','one year','two years','three years','four years','More than 5'))
user_input["Coding experience (In Years)"] = [mapping_dict[coding]]

# Current CTC
ctc = st.selectbox('What is your current CTC (in lakhs)?',('Not Applicable','Less than 3LPA','3-5LPA','5.1-7LPA','7.1-10 LPA','> 10 LPA'))
user_input["Current CTC"] = [mapping_dict[ctc]]

# hours spend
weekly_hours = st.selectbox('How many hours a week you can spend?', ('<8 Hours (Per week)','8 Hours (Per week)','12 - 16 Hours (Per week)'))
user_input["How many hours a week you can spend?"] = [mapping_dict[weekly_hours]]

# about us
about_us = st.selectbox('How you know about us?', ('Friend','Google search','Instagram','YouTube','Google Ads','Facebook','Employee referred','LinkedIn'))
user_input["How you know about us?"] = [mapping_dict[about_us]]

# payment type
payment_type = st.selectbox("Payment Type", ('Direct - Full Payment','Direct - Partial Payment','Emandate - Propelld','EMI - 3 Month','EMI - 6 Month','EMI - 9 Month','EMI - 12 Month'))
user_input["Payment Type"] = [mapping_dict[payment_type]]

# UG Degree
degree_ug = st.selectbox('What is your UG Degree?', ('BE/B.Tech','B.Sc','B.Com','BCA','Diploma','BA','BBA','B.Arch'))
user_input["UG Degree"] = [mapping_dict[degree_ug]]

# UG marks
marks_ug = st.slider('How much did you score in your Undergrad? (percentage)', 0, 100, 60)
user_input["UG Marks (In Percentage)"] = [marks_ug]

# educational background
ed_back = st.selectbox('What is your educational background?', ('Engineering','Non-Engineering'))
user_input["What is your Educational Background ?"] = [mapping_dict[ed_back]]

# highest degree
high_degree = st.selectbox("What is your Highest Qualification?", ('School','Diploma','Under Graduate','Post Graduate'))
user_input["What is your Highest Qualification?"] = [mapping_dict[high_degree]]


# coding background
code_ex = st.selectbox('What Stage you are in when it comes to coding skills?', ('Very Basic(Dont Know how to Code, Need to Start from Scratch)','Basic(Know Basics of Coding)','Intermediate(Know Coding but not advance level )','Advanced(Very Good in Coding )'))
user_input["What Stage you are in when it comes to coding skills?"] = [mapping_dict[code_ex]]

# CIBIL score
cibil = st.selectbox("What's your Current CIBIL Score?", ('300-579','580-669','670-739','740-799','800-850'))
user_input["What's your Current CIBIL Score?"] = [mapping_dict[cibil]]

# current profile
curr_profile = st.selectbox("What's your current profile?", ('Working in Non-IT','Graduate looking for the job','Working in IT','Student'))
user_input["What's your current profile?"] = [mapping_dict[curr_profile]]

# Family Monthly Income
family_ctc = st.selectbox("What's your Family Monthly Income(If you are working, what's your Monthly Income)?",('Less than 20k','20-30k','31-50k','51-70k','Above 70k'))
user_input["What's your Family Monthly Income(If you are working, what's your Monthly Income)?"] = [mapping_dict[family_ctc]]

# Expected CTC
expected_ctc = st.selectbox('Whats your expected salary (CTC/Annum) after completing this program with GUVI?', ('Less than 3LPA','3-5LPA','5.1-7LPA','7.1-10 LPA','> 10 LPA'))
user_input["Whats your expected salary (CTC/Annum) after completing this program with GUVI?"] = [mapping_dict[expected_ctc]]

# work experience
work_exp = st.selectbox('Work experience (In Years)', ('No Experience','Less than one','one year','two years','three years','four years','More than 5'))
user_input["Work experience (In Years)"] = [mapping_dict[work_exp]]

# coding exposure
coding_exp = st.selectbox("How much coding exposure do you have?", ('No Coding experience','Basic Looping','Basic DS ( Array, LL, Stack, Q)','Nested/2D arrays','File-handling'))
user_input["Your Coding exposure"] = [mapping_dict[coding_exp]]

#print(len(user_input.keys()))
user_input = pd.DataFrame(user_input)
user_input.replace(mapping_dict)

model = load_model()
input_array = np.array([user_input[feature] for feature in feature_names]).reshape(1, -1)

if st.button("Predict"):
    proba = model.predict_proba(input_array)
    df = pd.DataFrame({'Converted': [proba[0][1]*100], 'Dropped': proba[0][0]*100})
    st.table(df)

