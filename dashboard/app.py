import streamlit as st
import time

from main import process_log
from models.anomaly_detector import AnomalyDetector
from models.translator import translate_log

st.title("AI-Powered Network Log Translator")

log_input = st.text_area("Enter Network Log:")

if st.button("Analyze Log"):
    if log_input:
        start_time = time.time()

        parsed = process_log(log_input)

        # Train model with sample logs (simple demo approach)
        sample_logs = [
            process_log("<34>Oct 11 22:14:15 server sshd: Failed password for root"),
            process_log("SNMP Trap: Link Down"),
            process_log("SNMP Trap: CPU High")
        ]

        detector = AnomalyDetector()
        detector.train(sample_logs)

        status = detector.predict(parsed)
        explanation = translate_log(parsed)

        end_time = time.time()
        t2c = end_time - start_time

        st.subheader("Results")
        st.json(parsed)
        st.write("**Status:**", status)
        st.write("**Explanation:**", explanation)
        st.write("**Time to Clarity:**", round(t2c, 5), "seconds")

    else:
        st.warning("Please enter a log")