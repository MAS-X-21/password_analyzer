import streamlit as st
from analyzer import analyze_password
from recommendations import generate_recommendations, get_educational_guide

st.set_page_config(
    page_title="Password Strength Analyzer & Security Tool",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Password Strength Analyzer & Security Suggestion Tool")
st.markdown("""
*A local-first, defensive cybersecurity application designed to evaluate password unpredictability, 
detect weak patterns, and educate users on credential hygiene without storing or logging data.*
""")

# Sidebar Context Input
st.sidebar.header("Optional Context Check")
st.sidebar.markdown("Enter personal details (like your name or pet's name) to test if your password contains predictable personal data.")
user_context_input = st.sidebar.text_input("Context Words (comma-separated)", placeholder="e.g., john, rover, 2010")
context_words = [w.strip() for w in user_context_input.split(",") if w.strip()]

# Main Input
password_input = st.text_input("Enter a password to analyze:", type="password")

if password_input:
    results = analyze_password(password_input, context_words)
    recs = generate_recommendations(results)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Security Score", f"{results['score']} / 100")
    with col2:
        st.metric("Classification", results['classification'])
    with col3:
        st.metric("Entropy", f"{results['entropy']} bits")
        
    st.markdown("---")
    
    # Detailed Breakdown
    st.subheader("🔍 Detailed Pattern & Vulnerability Analysis")
    
    c1, c2 = st.columns(2)
    with c1:
        st.write(f"**Password Length:** {results['length']} characters")
        st.write(f"**Common Breach Check:** {'🚨 MATCH FOUND' if results['is_common'] else '✅ Passed'}")
        st.write(f"**Keyboard Patterns:** {'🚨 Detected (e.g., QWERTY)' if results['keyboard_pattern'] else '✅ None Detected'}")
    with c2:
        st.write(f"**Repeated Characters:** {results['repeated_chars']} instances")
        st.write(f"**Sequential Patterns:** {results['sequential_patterns']} found")
        st.write(f"**Personal Info Overlap:** {results['personal_match']} matches found")

    st.markdown("---")
    
    # Recommendations
    st.subheader("💡 Security Recommendations")
    for rec in recs:
        if "CRITICAL" in rec:
            st.error(rec)
        elif "Warning" in rec:
            st.warning(rec)
        else:
            st.info(rec)

# Educational Guide Section
st.markdown("---")
st.subheader("📚 Passphrase Guidance & Password Hygiene Education")
guide = get_educational_guide()

st.markdown(f"**Passphrase Strategy:** {guide['passphrase']}")
st.markdown("**Core Hygiene Rules:**")
for rule in guide['hygiene']:
    st.markdown(f"- {rule}")
