import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="Review Nominations", page_icon="📋", layout="wide")

# Get units from secrets
UNITS = st.secrets.units.cansofcom

# Header
st.title("📋 Review Nominations")

# Sidebar filters
with st.sidebar:
    st.title("Filters")

    # Status filter
    status_filter = st.multiselect(
        "Filter by Status",
        ["Pending Review", "Approved", "Rejected"],
        default=["Pending Review"],
    )

    # Unit filter
    unit_filter = st.multiselect("Filter by Unit", UNITS)

    # Award type filter
    award_filter = st.multiselect(
        "Filter by Award Type",
        ["Chief of Defence Staff Commendation", "Command Commendation", "Unit Award"],
    )

    # Date range filter
    st.subheader("Date Range")
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("From")
    with col2:
        end_date = st.date_input("To")

# Main content
if "submissions" not in st.session_state:
    st.session_state.submissions = []

if not st.session_state.submissions:
    st.info("No submissions to review yet.")
else:
    # Convert submissions to DataFrame
    df = pd.DataFrame(st.session_state.submissions)

    # Apply filters
    if status_filter:
        df = df[df["status"].isin(status_filter)]
    if unit_filter:
        df = df[df["unit"].isin(unit_filter)]
    if award_filter:
        df = df[df["award"].isin(award_filter)]

    # Display statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Submissions", len(df))
    with col2:
        st.metric("Pending Review", len(df[df["status"] == "Pending Review"]))
    with col3:
        st.metric("Approved", len(df[df["status"] == "Approved"]))

    # Display data table
    st.subheader("Submissions")

    # Add action buttons to each row
    def add_actions(row):
        return f"""
        <div style="display: flex; gap: 5px;">
            <button onclick="approveSubmission('{row["timestamp"]}')">✅</button>
            <button onclick="rejectSubmission('{row["timestamp"]}')">❌</button>
            <button onclick="viewDetails('{row["timestamp"]}')">👁️</button>
        </div>
        """

    # Display the table
    st.dataframe(
        df,
        column_config={
            "timestamp": "Submission Date",
            "rank": "Rank",
            "name": "Name",
            "unit": "Unit",
            "award": "Award",
            "status": st.column_config.SelectboxColumn(
                "Status",
                options=["Pending Review", "Approved", "Rejected"],
                required=True,
            ),
            "letter_filename": "Letter",
            "citation_filename": "Citation",
        },
        hide_index=True,
        use_container_width=True,
    )

    # Add JavaScript for button actions
    st.markdown(
        """
    <script>
    function approveSubmission(timestamp) {
        // Handle approval
        console.log('Approving submission:', timestamp);
    }
    
    function rejectSubmission(timestamp) {
        // Handle rejection
        console.log('Rejecting submission:', timestamp);
    }
    
    function viewDetails(timestamp) {
        // Handle view details
        console.log('Viewing details for:', timestamp);
    }
    </script>
    """,
        unsafe_allow_html=True,
    )
