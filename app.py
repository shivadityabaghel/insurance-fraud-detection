import streamlit as st
import json

import subprocess
import os



def execute_contract():

    os.chdir("smartcontract")
    command = "brownie run scripts\deploy.py"  

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    output, error = process.communicate()
    info = output.decode("utf-8")
    os.chdir("..")

    print("Bloack details:")
    print(info)

def main():
    st.title("Choose from the available policy options")

    col1, col2, col3 = st.columns(3)

    with col1:
        dict1 = {
            "Id": '101',
            'Company Name': "HDFC pvt. lmt",
            'Start_date': '01-04-2024',
            'end_date': '01-04-2025',
            'Amount': '300000',
        }
        st.write(dict1)
    with col2:
        dict1 = {
            "Id": '201',
            'Company Name': "KK pvt. lmt",
            'Start_date': '01-04-2024',
            'end_date': '01-04-2026',
            'Amount': '500000',
        }
        st.write(dict1)
    with col3:
        dict1 = {
            "Id": '301',
            'Company Name': "PK pvt. lmt",
            'Start_date': '01-04-2024',
            'end_date': '01-10-2024',
            'Amount': '200000',
        }
        st.write(dict1)


    with open('accounts.json', 'r') as json_file:
        accounts = json.load(json_file)

    #print(accounts)
    current_acc = st.selectbox(
        'Choose an account to log in ',
        accounts
    )

    accounts.remove(current_acc)

    st.write(f"current log in account is {current_acc}")

    # Initialize session state
    if 'form_data' not in st.session_state:
        st.session_state.form_data = {}
    if 'claimed_policy' not in st.session_state:
        st.session_state.claimed_policy = []

    # Form inputs
    with st.form("My Form"):
        st.header("Enter the details of Policy plan:")
        pol_id = st.text_input("Enter the id")
        if pol_id not in ['101', '201', '301']:
            st.warning("Choose correct id")
        byer_add = st.text_input("Your Address")
        other = st.multiselect('Other allowed accounts', accounts)

        submitted = st.form_submit_button("Submit")

        if submitted:
            execute_contract()
            st.session_state.form_data['pol_id'] = pol_id
            st.session_state.form_data['byer_add'] = byer_add
            st.session_state.form_data['other'] = other
            st.success("Policy Created successfully!")


    st.write("Stored Form Data:")

    st.title("Make claim of insurance")

    with st.form("Claim form"):
        st.write("Enter your details:")
        pol_id = st.text_input("Enter the id of policy")
        claim_add = st.text_input("Enter Your address")
        other_allowed = st.session_state.form_data.get('other')


        if pol_id == st.session_state.form_data.get('pol_id'):
            if claim_add in other_allowed or claim_add == st.session_state.form_data.get(
                    'byer_add'):
                if pol_id in st.session_state.claimed_policy:
                    st.warning("Policy already claimed")
                else:
                    st.session_state.claimed_policy.append(pol_id)
                    st.success("Policy claimed")
            else:
                st.warning("Policy ID matched but not address")
        else:
            st.warning("False claim - Fraud detected")

        submitted = st.form_submit_button("Submit")

if __name__ == "__main__":
    main()
