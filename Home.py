import streamlit as st

# Set page config
st.set_page_config(page_title="Honours & Awards", page_icon="🏅", layout="wide")

# Header with large title and description
st.title("🏅 Honours & Awards")
st.markdown("""
Welcome to the Honours and Awards portal. This platform facilitates the nomination and review process 
for recognizing exceptional service and achievements.
""")

# Create three columns for main features
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📝 Submit Nomination")
    st.markdown("""
    - Create a new nomination
    - Upload supporting documents
    - Track submission status
    """)
    st.page_link(
        "pages/1_Submit_Nomination.py",
        label="Go to Nomination Form",
        use_container_width=True,
    )

with col2:
    st.markdown("### 📋 Review Submissions")
    st.markdown("""
    - View pending nominations
    - Process submissions
    - Update nomination status
    """)
    st.page_link(
        "pages/2_Review_Submissions.py",
        label="Go to Review Page",
        use_container_width=True,
    )

with col3:
    st.markdown("### 📚 Resources")
    st.markdown("""
    - Awards Policy
    - Citation Guidelines
    - FAQs
    - Contact Support
    """)
    st.page_link(
        "pages/3_Resources.py", label="View Resources", use_container_width=True
    )

# Information section
st.divider()
st.markdown("### ℹ️ About the Process")
st.markdown("""
The honours and awards process is designed to recognize exceptional service and achievements. 
Nominations are carefully reviewed by a committee to ensure they meet the established criteria and standards.

**Key Features:**
- Streamlined nomination process
- Secure document upload
- Real-time status tracking
- Comprehensive review system
""")

# Sidebar
with st.sidebar:
    st.title("🏅 Quick Links")

    st.markdown("### Navigation")
    st.page_link("pages/1_Submit_Nomination.py", label="Submit Nomination")
    st.page_link("pages/2_Review_Submissions.py", label="Review Submissions")
    st.page_link("pages/3_Resources.py", label="Resources")

    st.divider()

    st.markdown("### Contact")
    st.write("Need assistance? Contact the awards team:")
    st.write("📧 awards@example.com")
    st.write("📞 (555) 123-4567")

    st.divider()

    st.caption("Last updated: May 2025")
    st.caption("Version 1.0.0")
