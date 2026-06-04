# 4. Main UI Execution
st.title("🌊 Nant Cledlyn Water Level Analysis")
st.subheader("by Hugh Neve")

# --- INTRODUCTION SECTION ---
st.markdown("""
Welcome to the Nant Cledlyn Water Level Analysis dashboard. 

*Insert your plain text introduction here. You can use this space to describe the purpose of the dashboard, details about the Nant Cledlyn catchment, or instructions on how to use the analytical tools below.*
""")
st.markdown("---")
# -----------------------------

df = fetch_filtered_data(date_range)
# ... rest of your code ...
