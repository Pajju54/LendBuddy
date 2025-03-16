# import streamlit as st
# import os
# from langchain_groq import ChatGroq
#
# # Set the Groq API key from environment variables
# os.environ["GROQ_API_KEY"] = "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"
#
# # Initialize ChatGroq with provided model and parameters
# llm = ChatGroq(
#     model="mixtral-8x7b-32768",
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2,
# )
#
# # Page config
# st.set_page_config(layout="wide")
#
# # State to track current page
# if "page" not in st.session_state:
#     st.session_state.page = 0
#
# # Define all the questions
# questions = [
#     # Personal Details
#     {"title": "Title", "type": "selectbox", "options": ["Mr.", "Ms.", "M/s", "Others"]},
#     {"title": "Applicant Name", "type": "text"},
#     {"title": "Marital Status", "type": "selectbox", "options": ["Single", "Married"]},
#     {"title": "Religion", "type": "text"},
#     {"title": "Gender", "type": "selectbox", "options": ["Male", "Female"]},
#     {"title": "Date of Birth", "type": "date"},
#     {"title": "Number of Dependents", "type": "number"},
#     {"title": "Current City Duration (Years/Months)", "type": "text"},
#     {"title": "Current Residence Duration (Years/Months)", "type": "text"},
#
#     # Present Address
#     {"title": "Present Address", "type": "text"},
#     {"title": "Landmark", "type": "text"},
#     {"title": "City", "type": "text"},
#     {"title": "State", "type": "text"},
#     {"title": "Country", "type": "text"},
#     {"title": "Pin Code", "type": "text"},
#     {"title": "Landline Number", "type": "text"},
#     {"title": "Mobile Number", "type": "text"},
#     {"title": "Email ID", "type": "text"},
#
#     # Occupational Details
#     {"title": "Occupation", "type": "selectbox", "options": ["Salaried", "Self-employed", "Professional", "Other"]},
#     {"title": "Type of Company", "type": "selectbox",
#      "options": ["Pvt. Ltd.", "Public Ltd.", "Proprietor", "Partnership", "Trader", "Retailer"]},
#     {"title": "Nature of Business", "type": "text"},
#     {"title": "Employer/Business Name", "type": "text"},
#     {"title": "Employer/Business Address", "type": "text"},
#     {"title": "Designation", "type": "text"},
#     {"title": "Experience in Current Job/Business (Years/Months)", "type": "text"},
#     {"title": "Total Experience in Job/Business (Years/Months)", "type": "text"},
#     {"title": "Office Landline Number", "type": "text"},
#     {"title": "Official Email ID", "type": "text"},
#
#     # Financial Details
#     {"title": "PAN Number", "type": "text"},
#     {"title": "Aadhar Card Number", "type": "text"},
#     {"title": "Voter ID Number", "type": "text"},
#     {"title": "Existing Bank Account Number (if applicable)", "type": "text"},
#     {"title": "Existing Loan Number (if applicable)", "type": "text"},
#
#     # Personal References
#     {"title": "Reference 1: Name", "type": "text"},
#     {"title": "Reference 1: Relationship with Applicant", "type": "text"},
#     {"title": "Reference 1: Residential Address", "type": "text"},
#     {"title": "Reference 1: Mobile Number", "type": "text"},
#     {"title": "Reference 2: Name", "type": "text"},
#     {"title": "Reference 2: Relationship with Applicant", "type": "text"},
#     {"title": "Reference 2: Residential Address", "type": "text"},
#     {"title": "Reference 2: Mobile Number", "type": "text"},
#
#     # Vehicle Ownership
#     {"title": "Vehicle Manufacturer", "type": "text"},
#     {"title": "Vehicle Model", "type": "text"},
#     {"title": "Purchase Year", "type": "text"},
#     {"title": "Financed", "type": "selectbox", "options": ["Yes", "No"]},
#
#     # Other Assets
#     {"title": "Assets Owned", "type": "multiselect",
#      "options": ["LCD/LED", "Microwave", "Home Theatre", "Modular Kitchen", "Smartphone", "AC", "Laptop/Tablet",
#                  "Washing Machine"]},
#
#     # Interest in Additional Services
#     {"title": "Interested Services", "type": "multiselect",
#      "options": ["Insurance", "Mutual Fund", "Credit Card", "Fixed Deposit", "Recurring Deposit"]},
# ]
#
# # Track form responses in session state
# if "responses" not in st.session_state:
#     st.session_state.responses = [None] * len(questions)
#
# # Display current question
# current_question = questions[st.session_state.page]
#
# with st.container():
#     st.title("Loan Application Form")
#
#     # Display question based on type
#     if current_question["type"] == "text":
#         st.session_state.responses[st.session_state.page] = st.text_input(current_question["title"],
#                                                                           value=st.session_state.responses[
#                                                                                     st.session_state.page] or "")
#     elif current_question["type"] == "selectbox":
#         st.session_state.responses[st.session_state.page] = st.selectbox(current_question["title"],
#                                                                          current_question["options"],
#                                                                          index=current_question["options"].index(
#                                                                              st.session_state.responses[
#                                                                                  st.session_state.page]) if
#                                                                          st.session_state.responses[
#                                                                              st.session_state.page] in current_question[
#                                                                              "options"] else 0)
#     elif current_question["type"] == "date":
#         st.session_state.responses[st.session_state.page] = st.date_input(current_question["title"],
#                                                                           value=st.session_state.responses[
#                                                                               st.session_state.page])
#     elif current_question["type"] == "number":
#         st.session_state.responses[st.session_state.page] = st.number_input(current_question["title"],
#                                                                             value=st.session_state.responses[
#                                                                                       st.session_state.page] or 0)
#     elif current_question["type"] == "multiselect":
#         st.session_state.responses[st.session_state.page] = st.multiselect(current_question["title"],
#                                                                            current_question["options"],
#                                                                            default=st.session_state.responses[
#                                                                                        st.session_state.page] or [])
#
# # Navigation buttons
# col1, col2, col3 = st.columns([1, 3, 1])
#
# with col1:
#     if st.session_state.page > 0:
#         if st.button("⬅ Back"):
#             st.session_state.page -= 1
#
# with col3:
#     if st.session_state.page < len(questions) - 1:
#         if st.button("Next ➡"):
#             st.session_state.page += 1
#     else:
#         if st.button("Submit"):
#             st.success("Form submitted successfully!")
#             st.write("*Responses:*")
#             for i, q in enumerate(questions):
#                 st.write(f"{q['title']}: {st.session_state.responses[i]}")
#
# # Chatbot Section
# with st.sidebar:
#     st.title("Chat with LLM")
#     chatbot_input = st.text_area("Type your Question here...", height=150)
#
#     if st.button("Send"):
#         if chatbot_input:
#             st.write(f"*You:* {chatbot_input}")
#
#             # Use the Groq model to generate a response
#             response = llm.predict(chatbot_input)
#             st.write(f"*Bot:* {response}")



import streamlit as st
import os
from langchain_groq import ChatGroq

# Set the Groq API key from environment variables
os.environ["GROQ_API_KEY"] = "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"

# Initialize ChatGroq with provided model and parameters
llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Page config
st.set_page_config(layout="wide")

# State to track current page
if "page" not in st.session_state:
    st.session_state.page = 0

# Define all the questions
questions = [
    # Personal Details
    {"title": "Title", "type": "selectbox", "options": ["Mr.", "Ms.", "M/s", "Others"]},
    {"title": "Applicant Name", "type": "text"},
    {"title": "Marital Status", "type": "selectbox", "options": ["Single", "Married"]},
    {"title": "Religion", "type": "text"},
    {"title": "Gender", "type": "selectbox", "options": ["Male", "Female"]},
    {"title": "Date of Birth", "type": "date"},
    {"title": "Number of Dependents", "type": "number"},
    {"title": "Current City Duration (Years/Months)", "type": "text"},
    {"title": "Current Residence Duration (Years/Months)", "type": "text"},

    # Present Address
    {"title": "Present Address", "type": "text"},
    {"title": "Landmark", "type": "text"},
    {"title": "City", "type": "text"},
    {"title": "State", "type": "text"},
    {"title": "Country", "type": "text"},
    {"title": "Pin Code", "type": "text"},
    {"title": "Landline Number", "type": "text"},
    {"title": "Mobile Number", "type": "text"},
    {"title": "Email ID", "type": "text"},

    # Occupational Details
    {"title": "Occupation", "type": "selectbox", "options": ["Salaried", "Self-employed", "Professional", "Other"]},
    {"title": "Type of Company", "type": "selectbox",
     "options": ["Pvt. Ltd.", "Public Ltd.", "Proprietor", "Partnership", "Trader", "Retailer"]},
    {"title": "Nature of Business", "type": "text"},
    {"title": "Employer/Business Name", "type": "text"},
    {"title": "Employer/Business Address", "type": "text"},
    {"title": "Designation", "type": "text"},
    {"title": "Experience in Current Job/Business (Years/Months)", "type": "text"},
    {"title": "Total Experience in Job/Business (Years/Months)", "type": "text"},
    {"title": "Office Landline Number", "type": "text"},
    {"title": "Official Email ID", "type": "text"},

    # Financial Details
    {"title": "PAN Number", "type": "text"},
    {"title": "Aadhar Card Number", "type": "text"},
    {"title": "Voter ID Number", "type": "text"},
    {"title": "Existing Bank Account Number (if applicable)", "type": "text"},
    {"title": "Existing Loan Number (if applicable)", "type": "text"},

    # Personal References
    {"title": "Reference 1: Name", "type": "text"},
    {"title": "Reference 1: Relationship with Applicant", "type": "text"},
    {"title": "Reference 1: Residential Address", "type": "text"},
    {"title": "Reference 1: Mobile Number", "type": "text"},
    {"title": "Reference 2: Name", "type": "text"},
    {"title": "Reference 2: Relationship with Applicant", "type": "text"},
    {"title": "Reference 2: Residential Address", "type": "text"},
    {"title": "Reference 2: Mobile Number", "type": "text"},

    # Vehicle Ownership
    {"title": "Vehicle Manufacturer", "type": "text"},
    {"title": "Vehicle Model", "type": "text"},
    {"title": "Purchase Year", "type": "text"},
    {"title": "Financed", "type": "selectbox", "options": ["Yes", "No"]},

    # Other Assets
    {"title": "Assets Owned", "type": "multiselect",
     "options": ["LCD/LED", "Microwave", "Home Theatre", "Modular Kitchen", "Smartphone", "AC", "Laptop/Tablet",
                 "Washing Machine"]},

    # Interest in Additional Services
    {"title": "Interested Services", "type": "multiselect",
     "options": ["Insurance", "Mutual Fund", "Credit Card", "Fixed Deposit", "Recurring Deposit"]},
]

# Track form responses in session state
if "responses" not in st.session_state:
    st.session_state.responses = [None] * len(questions)

# Display current question
current_question = questions[st.session_state.page]

with st.container():
    st.title("Loan Application Form")

    # Display question based on type
    if current_question["type"] == "text":
        st.session_state.responses[st.session_state.page] = st.text_input(current_question["title"],
                                                                          value=st.session_state.responses[st.session_state.page] or "")
    elif current_question["type"] == "selectbox":
        st.session_state.responses[st.session_state.page] = st.selectbox(current_question["title"],
                                                                         current_question["options"],
                                                                         index=current_question["options"].index(st.session_state.responses[st.session_state.page]) if st.session_state.responses[st.session_state.page] in current_question["options"] else 0)
    elif current_question["type"] == "date":
        st.session_state.responses[st.session_state.page] = st.date_input(current_question["title"],
                                                                          value=st.session_state.responses[st.session_state.page])
    elif current_question["type"] == "number":
        st.session_state.responses[st.session_state.page] = st.number_input(current_question["title"],
                                                                            value=st.session_state.responses[st.session_state.page] or 0)
    elif current_question["type"] == "multiselect":
        st.session_state.responses[st.session_state.page] = st.multiselect(current_question["title"],
                                                                           current_question["options"],
                                                                           default=st.session_state.responses[st.session_state.page] or [])

# Navigation buttons
col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    if st.session_state.page > 0:
        if st.button("⬅ Back"):
            st.session_state.page -= 1

with col3:
    if st.session_state.page < len(questions) - 1:
        if st.button("Next ➡"):
            st.session_state.page += 1
    else:
        if st.button("Submit"):
            st.success("Form submitted successfully!")
            st.write("*Responses:*")
            for i, q in enumerate(questions):
                st.write(f"{q['title']}: {st.session_state.responses[i]}")

# Chatbot Section
with st.sidebar:
    st.title("Chat with LLM")
    chatbot_input = st.text_area("Type your Question here...", height=150)

    if st.button("Send"):
        if chatbot_input:
            st.write(f"*You:* {chatbot_input}")

            # Prepare the context based on the filled responses
            context = "\n".join([f"{q['title']}: {response}" for q, response in zip(questions, st.session_state.responses)])

            # Add context to the chatbot input to answer questions about the loan application
            context_input = f"Context: {context}\n\nQuestion: {chatbot_input}"

            # Use the Groq model to generate a response based on the context and input
            response = llm.predict(context_input)
            st.write(f"*Bot:* {response}")