import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize session state for submissions if it doesn't exist
if "submissions" not in st.session_state:
    st.session_state.submissions = []

# Set page config for a better look
st.set_page_config(
    page_title="Honours and Awards Nomination", page_icon="🏅", layout="wide"
)

# Get ranks and units from secrets
RANKS = st.secrets.ranks.enlisted + st.secrets.ranks.officers
UNITS = st.secrets.units.cansofcom

# Sidebar
with st.sidebar:
    st.title("🏅 Resources")

    st.subheader("Quick Links")
    st.markdown("""
    - [Awards Policy](https://example.com/policy)
    - [Citation Guidelines](https://example.com/citations)
    - [FAQs](https://example.com/faq)
    """)

    st.subheader("Contact Support")
    st.write("Need help? Contact the awards team:")
    st.write("📧 awards@example.com")
    st.write("📞 (555) 123-4567")

    st.divider()

    st.subheader("Form Progress")
    st.progress(0)  # This will be updated based on form completion

    st.divider()

    st.caption("Last updated: March 2024")
    st.caption("Version 1.0.0")

# Header
st.title("🏅 Honours and Awards Nomination Form")

# Information callout at the top
st.info("""
This form is for submitting nominations for honours and awards. Please ensure all required documents are prepared before starting.
The nomination process typically takes 2-3 weeks for review.
""")

# Main form container with border
with st.container(border=True):
    # Award Selection Section
    st.subheader("Award Selection")
    st.write("Please select the award being nominated for:")

    # Create three columns for award options
    award_col1, award_col2, award_col3 = st.columns(3)

    with award_col1:
        with st.container(height=300, border=True):
            st.write("#### 🏅 Chief of Defence Staff Commendation")
            st.info(
                "**Purpose:** Outstanding service or achievement of a particularly demanding nature"
            )
            st.write(
                "**Focus:** Exceptional leadership, significant impact, outstanding contribution"
            )

    with award_col2:
        with st.container(height=300, border=True):
            st.write("#### 🎖️ Command Commendation")
            st.info(
                "**Purpose:** Meritorious service or achievement that brings credit to the command"
            )
            st.write(
                "**Focus:** Command objectives, excellence in duties, unit effectiveness"
            )

    with award_col3:
        with st.container(height=300, border=True):
            st.write("#### 🏆 Unit Award")
            st.info(
                "**Purpose:** Collective achievement or outstanding service by a unit"
            )
            st.write(
                "**Focus:** Team accomplishments, unit operations, collective excellence"
            )

    # Radio button selection
    award = st.radio(
        "Select Award:",
        [
            "Chief of Defence Staff Commendation",
            "Command Commendation",
            "Unit Award",
            "Other",
        ],
        horizontal=True,
    )

    if award == "Other":
        award = st.text_input("Please specify the award")

    # Nominee Information Section
    st.subheader("Nominee Information")
    st.write("Please provide the details of the person you wish to nominate:")

    # Create three columns for nominee info
    col1, col2, col3 = st.columns(3)

    with col1:
        rank: str = st.selectbox("Rank", RANKS)

    with col2:
        name: str = st.text_input("Full Name")

    with col3:
        unit: str = st.selectbox("Unit", UNITS)

    # File upload section
    st.subheader("Required Documentation")
    st.write("Please upload the following documents:")

    # Create two columns for document uploads
    doc_col1, doc_col2 = st.columns(2)

    # Letter of Recommendation upload
    with doc_col1:
        st.write("#### Letter of Recommendation")
        with st.expander("📋 Letter Requirements"):
            st.write("The letter of recommendation should include:")
            st.write("- Clear justification for the nomination")
            st.write("- Specific examples of achievements or actions")
            st.write("- Impact of the nominee's contributions")
            st.write("- Must be signed by the unit commanding officer")
            st.write("- Should be on official letterhead")

        letter_of_recommendation = st.file_uploader(
            "Upload Letter of Recommendation (PDF)",
            type=["pdf"],
            help="Maximum file size: 10MB",
        )

    # Citation upload
    with doc_col2:
        st.write("#### Proposed Citation")
        with st.expander("📋 Citation Guidelines"):
            st.write("The citation should:")
            st.write("- Be concise and impactful")
            st.write("- Highlight key achievements")
            st.write("- Follow the standard citation format")
            st.write("- Be no longer than 100 words")

        citation = st.file_uploader(
            "Upload Proposed Citation (PDF)",
            type=["pdf"],
            help="Maximum file size: 10MB",
        )

    # Submit button
    if st.button("Submit Nomination", type="primary"):
        if not all([rank, name, unit, award, letter_of_recommendation, citation]):
            st.error(
                "❌ Please fill in all required fields and upload all necessary documents."
            )
            st.warning(
                "Missing required information. Please check the form and try again."
            )
        else:
            # Create submission record
            submission = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "rank": rank,
                "name": name,
                "unit": unit,
                "award": award,
                "letter_filename": letter_of_recommendation.name,
                "citation_filename": citation.name,
                "status": "Pending Review",
            }

            # Add to session state
            st.session_state.submissions.append(submission)

            st.success("✅ Nomination submitted successfully!")
            st.info("""
            Next steps:
            1. You will receive a confirmation email within 24 hours
            2. The nomination will be reviewed by the awards committee
            3. You will be notified of the decision within 2-3 weeks
            """)

            # Show a summary of the submission
            st.subheader("Submission Summary")
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Nominee Details:**")
                st.write(f"Rank: {rank}")
                st.write(f"Name: {name}")
                st.write(f"Unit: {unit}")
            with col2:
                st.write("**Award Information:**")
                st.write(f"Award: {award}")
                st.write("Documents: ✅ Uploaded")
