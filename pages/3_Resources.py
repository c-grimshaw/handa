import streamlit as st

# Set page config
st.set_page_config(
    page_title="Resources - Honours & Awards", page_icon="📚", layout="wide"
)

# Header
st.title("📚 Resources")

# Create tabs for different resource categories
tab1, tab2, tab3 = st.tabs(["Policy Documents", "Guidelines", "FAQs"])

with tab1:
    st.markdown("### Awards Policy")
    st.markdown("""
    #### Chief of Defence Staff Commendation
    The CDS Commendation is awarded to recognize deeds or activities beyond the demand of normal duty. 
    It is the highest level of commendation that can be awarded by the Chief of the Defence Staff.
    
    #### Command Commendation
    The Command Commendation recognizes meritorious service or achievement that brings credit to the command.
    It is awarded for outstanding performance of duties or exceptional service.
    
    #### Unit Award
    The Unit Award recognizes collective achievement or outstanding service by a unit. It is awarded to 
    units that have demonstrated exceptional performance in operations or training.
    """)

    st.download_button(
        label="📥 Download Full Policy Document",
        data="Policy document content would go here",
        file_name="Awards_Policy.pdf",
        mime="application/pdf",
    )

with tab2:
    st.markdown("### Citation Guidelines")
    st.markdown("""
    #### General Guidelines
    - Citations should be concise and impactful
    - Focus on specific achievements and their impact
    - Use clear, professional language
    - Maximum length: 100 words
    
    #### Required Elements
    1. Opening statement of achievement
    2. Specific examples of actions
    3. Impact of the actions
    4. Closing statement of recognition
    
    #### Example Citation
    > "For outstanding leadership and dedication in the planning and execution of Operation X. 
    > Captain Smith's innovative approach to mission planning resulted in a 40% increase in operational 
    > effectiveness. His exceptional performance brought great credit to the Canadian Special Operations Forces."
    """)

    st.download_button(
        label="📥 Download Citation Template",
        data="Citation template content would go here",
        file_name="Citation_Template.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )

with tab3:
    st.markdown("### Frequently Asked Questions")

    with st.expander("What is the typical review timeline?"):
        st.write("""
        The review process typically takes 2-3 weeks from submission to final decision. 
        This includes:
        - Initial review by the awards committee
        - Command review and approval
        - Final processing and notification
        """)

    with st.expander("Who can submit a nomination?"):
        st.write("""
        Any member of a unit can submit a nomination. The nominator should:
        - Be familiar with the nominee's achievements
        - Have access to supporting documentation
        - Be able to provide a detailed justification
        """)

    with st.expander("What documents are required?"):
        st.write("""
        Required documents include:
        - Letter of recommendation (signed by unit CO)
        - Proposed citation
        - Any additional supporting documentation
        All documents must be in PDF format.
        """)

    with st.expander("How do I track my nomination?"):
        st.write("""
        You can track your nomination through the Review Submissions page. 
        The status will be updated as the nomination progresses through the review process.
        """)

# Sidebar
with st.sidebar:
    st.title("📚 Quick Links")

    st.markdown("### Navigation")
    st.page_link("Home.py", label="Home")
    st.page_link("pages/1_Submit_Nomination.py", label="Submit Nomination")
    st.page_link("pages/2_Review_Submissions.py", label="Review Submissions")

    st.divider()

    st.markdown("### Contact")
    st.write("Need assistance? Contact the awards team:")
    st.write("📧 awards@example.com")
    st.write("📞 (555) 123-4567")

    st.divider()

    st.caption("Last updated: March 2024")
    st.caption("Version 1.0.0")
