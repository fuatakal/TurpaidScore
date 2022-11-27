import time
import streamlit as st
import numpy as np
import pandas as pd
# import SessionState

# session = SessionState.get(run_id=0)

def main():
    st.set_page_config(page_title="Colchicine Resistance Predictor", page_icon=":hospital:")

    st.markdown("<h1 style='text-align: center; color: black;'>Score for Predicting Colchicine Resistant Disease Course in FMF Patients</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>Please fill the form below and click the compute button to see how likely your patient will be resistant to colchicine.</h2>", unsafe_allow_html=True)

    st.markdown("<br/><hr>", unsafe_allow_html=True)

    # Here is the list of features to be sent to the model
    # st.write(model.features)

    ageOnSet = st.checkbox("Age at symptom onset <= 3 years", value=False)
    # comorbidity = st.checkbox("Comorbidity", value=False)
    # duration = st.checkbox("Duration of attack ≥3 days", value=False)
    frequency = st.checkbox("Attack frequency (≥1 attack/month)", value=False)
    arthritis = st.checkbox("Arthritis", value=False)
    chestPain = st.checkbox("Chest pain", value=False)
    mutations = st.checkbox("Homozygosity/compound heterozygosity for exon 10 MEFV mutations", value=False)

    
    st.markdown("<hr>", unsafe_allow_html=True)

    left_button, right_button, _ = st.columns([1,1,6])

    computed = False
    crScore = 0
    with left_button:
        if st.button("Compute"):

            # For debugging purposes
            #st.write(ageOnSet)
            #st.write(comorbidity)
            #st.write(duration)
            #st.write(frequency)
            #st.write(arthritis)
            #st.write(chestPain)
            #st.write(mutations)

            #crScore = ageOnSet*0.5 + comorbidity*1 + duration*0.5 + frequency*1 + arthritis*0.5 + chestPain*0.5 + mutations*2
            crScore = ageOnSet*0.5 + frequency*1.0 + arthritis*1.0 + chestPain*0.5 + mutations*2.0
            computed = True


    with right_button:
        if st.button("Clear"):
            st.session_state["ageOnSet"] = False
            #st.session_state["comorbidity"] = False
            #st.session_state["duration"] = False
            st.session_state["frequency"] = False
            st.session_state["arthritis"] = False
            st.session_state["chestPain"] = False
            st.session_state["mutations"] = False
            ageOnSet = False
            #comorbidity = False
            #duration = False
            frequency = False
            arthritis = False
            chestPain = False
            mutations = False

            #Session.run_id += 1

    if computed:

        st.markdown("<br/>", unsafe_allow_html=True)

        if crScore > 2:
            st.info('It is **likely** that your patient is resistant to colchicine. Because, my calculations show **{}** as the risk score for this patient.'.format(str(crScore)))
        else:
            st.success('It is **unlikely** that your patient is resistant to colchicine. Because, my calculations show **{}** as the risk score for this patient.'.format(str(crScore)))

        st.error('By the way, do not forget that I am just a prototype! Don\'t take my word for it.')

if __name__ == '__main__':
    main()
