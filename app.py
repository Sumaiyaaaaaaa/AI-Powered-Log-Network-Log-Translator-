import streamlit as st
import time

from main import process_log
from models.translator import translate_log

st.title("AI-Powered Network Log Translator")

log_input = st.text_area("Enter Network Log:")

if st.button("Analyze Log"):
    if log_input:
        start_time = time.time()

        # 🔹 Parse log
        parsed = process_log(log_input)

        # 🔹 Analyze log (ONLY ONCE)
        result = translate_log(parsed)

        end_time = time.time()
        t2c = end_time - start_time

        # 🔹 Output
        st.subheader("Results")
        st.json(parsed)

        # ✅ Clean output (no duplication)
        st.text(result)

    else:
        st.warning("Please enter a log")
