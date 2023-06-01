import streamlit as st

# Define a list of companies and their contact information
companies = [
    {"name": "Company A", "contact_name": "Contact A", "position": "Position A", "linkedin": "https://linkedin.com/companya"},
    {"name": "Company B", "contact_name": "Contact B", "position": "Position B", "linkedin": "https://linkedin.com/companyb"},
    {"name": "Company C", "contact_name": "Contact C", "position": "Position C", "linkedin": "https://linkedin.com/companyc"},
]

# Define a dictionary to hold bookmarked companies
bookmarked_companies = {}

# Define a dictionary to store the state of each company
company_state = {company["name"]: {"status": "", "contract_amount": ""} for company in companies}

def clear_text():
    st.session_state["Search by company name"] = ""

def main():
    # Custom CSS
    st.markdown("""
    <style>
    .reportview-container {
        padding: 30px 30px 30px 20px;
        background: #D0E8F2;  /* Light blue background color */
    }
    .sidebar .sidebar-content {
        background: #1e6f5c;
    }
    /* Button hover style */
    .stButton>button:hover {
        color: black;
        font-weight: bold;
    }
    /* Background color for expander - Assuming '.st-expander' is the correct class for the expanders */
    .st-expander {
        background: #f0f0f0; /* Very light gray */
    }
    </style>
    """, unsafe_allow_html=True)

    st.sidebar.image("download.png", width=100)  # Add your logo here, adjust the size as needed
    if st.sidebar.button(" <- Go Back "):  # Large "Go Back" button at the top of the sidebar
        clear_text()
        st.experimental_rerun()

    

    search_query = st.sidebar.text_input("Search by company name", "")

    matching_companies = [company for company in companies if search_query.lower() in company["name"].lower()]

   
    for company in matching_companies:
        with st.expander(company['name'], expanded=True):
             # Bookmarking feature: replaced by the bookmark image (a placeholder button here)
            if st.button("🔖", key=f"Bookmark_{company['name']}"):
                bookmarked_companies[company['name']] = company
                st.success(f"{company['name']} has been bookmarked!")

            show_company_info(company, company['name'])



def show_bookmarked_companies():
    st.subheader("Bookmarked Companies")
    if len(bookmarked_companies)> 0:
        for company in bookmarked_companies.values():
            st.write(company["name"])
            st.write(f"Contact Name: {company['contact_name']}")
            st.write(f"Position: {company['position']}")
            st.write(f"LinkedIn: {company['linkedin']}")
            st.write("---")
    else:
        st.sidebar.image("download.png", width=100)  # Add your logo here, adjust the size as needed
        st.sidebar.button(" <- Go Back ")
        #display company 1 info:
        st.subheader("Company A")
        st.write("Contact Name: Contact A")
        st.write("Position: Position A")
        st.write("LinkedIn: https://linkedin.com/companya")

        #tell streamlit to not show anything else:
        st.stop()

if st.sidebar.button("Bookmarked"):
    show_bookmarked_companies()


def show_company_info(company, key):
    st.header(f"Information for {company['name']}")
    st.write(f"Contact Name: {company['contact_name']}")
    st.write(f"Position: {company['position']}")
    st.write(f"LinkedIn: {company['linkedin']}")
    
    status = st.radio("Status", ['About to Contact', 'Already Contacted'], key=f"Status_{key}")
    
    # If the company is not in company_state, add it
    if company["name"] not in company_state:
        company_state[company["name"]] = {"status": "", "contract_amount": ""}
    
    company_state[company["name"]]["status"] = status

    contract_amount = st.text_input('Contract Amount', key=f"Contract_{key}")
    company_state[company["name"]]["contract_amount"] = contract_amount

    if st.button('More information', key=f"MoreInfo_{key}"):
        st.write("Additional company information goes here...")

# The "Go Back" button has been removed from each company's details


    

if __name__ == "__main__":
    main()
