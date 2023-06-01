import streamlit as st

# Define a list of companies and their contact information
companies = [
    {"name": "Company A", "contact_name": "Contact A", "email": "contact@companya.com", "position": "Position A", "phone": "123-456-7890", "linkedin": "https://linkedin.com/companya"},
    {"name": "Company B", "contact_name": "Contact B", "email": "contact@companyb.com", "position": "Position B", "phone": "098-765-4321", "linkedin": "https://linkedin.com/companyb"},
    {"name": "Company C", "contact_name": "Contact C", "email": "contact@companyc.com", "position": "Position C", "phone": "456-789-0123", "linkedin": "https://linkedin.com/companyc"},
]

# Define a dictionary to hold bookmarked companies
bookmarked_companies = {
    "Example Company": {"name": "Example Company", "contact_name": "Example Contact", "email": "example@example.com", "position": "Example Position", "phone": "000-000-0000", "linkedin": "https://linkedin.com/example"}
}

def main():
    # Custom CSS
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
    </style>
    """, unsafe_allow_html=True)
    st.title("Skyline Design Company Contact Information")
    st.sidebar.markdown("## Search a company")
    search_query = st.sidebar.text_input("Search by company name", "")

    matching_companies = [company for company in companies if search_query.lower() in company["name"].lower()]
    for company in matching_companies:
        with st.beta_expander(company['name'], expanded=True):
            st.header(f"Information for {company['name']}")
            st.write(f"Contact Name: {company['contact_name']}")
            st.write(f"Email: {company['email']}")
            st.write(f"Position: {company['position']}")
            st.write(f"Phone: {company['phone']}")
            st.write(f"LinkedIn: {company['linkedin']}")

            # Similarity feature
            st.subheader("Similar Companies")
            for similar_company in companies:
                if similar_company["name"][0] == company["name"][0]:
                    with st.container():
                        st.markdown(f"**Name**: {similar_company['name']}")
                        st.markdown(f"**Contact Name**: {similar_company['contact_name']}")
                        st.markdown(f"**Email**: {similar_company['email']}")
                        st.markdown(f"**Position**: {similar_company['position']}")
                        st.markdown(f"**Phone**: {similar_company['phone']}")
                        st.markdown(f"**LinkedIn**: [link]({similar_company['linkedin']})")
                        st.markdown("---")  # add a line separator

            # Bookmarking feature
            if st.button(f"Bookmark {company['name']}"):
                bookmarked_companies[company['name']] = company
                st.success(f"{company['name']} has been bookmarked!")

    # Show bookmarked companies
    st.sidebar.markdown("## Bookmarked Companies")
    for name, company in bookmarked_companies.items():
        st.sidebar.markdown(f"**Name**: {company['name']}\n**Contact Name**: {company['contact_name']}\n**Email**: {company['email']}\n**Position**: {company['position']}\n**Phone**: {company['phone']}\n**LinkedIn**: [link]({company['linkedin']})")

if __name__ == "__main__":
    main()

