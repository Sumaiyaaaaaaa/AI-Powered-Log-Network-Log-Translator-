import time

def analyze_log(log):

    # ✅ Handle dict input safely
    if isinstance(log, dict):

        # 🚨 BRUTE FORCE
        if log.get("STATUS") == "FAILED" and log.get("SERVICE") == "SSH":
            return "ATTACK", "Multiple failed SSH login attempts detected"

        # 🚨 PORT SCAN
        if log.get("DPT") in ["21", "22", "23"]:
            return "ATTACK", "Port scanning activity detected"

        # 🚨 DDOS
        if log.get("FLAGS") == "SYN" and log.get("DPT") == "80":
            return "SUSPICIOUS", "Possible SYN flood attack"

        # 🚨 DATA EXFILTRATION
        if "BYTES_SENT" in log:
            try:
                if int(log["BYTES_SENT"]) > 5000000:
                    return "SUSPICIOUS", "Large data transfer detected"
            except:
                pass

        # 🚨 BLOCKED ACCESS
        if log.get("ACTION") == "BLOCK":
            return "SUSPICIOUS", "Blocked unauthorized access attempt"

    # ✅ Handle string input (backup case)
    else:
        log = str(log).upper()

        if "FAILED" in log and "SSH" in log:
            return "ATTACK", "Multiple failed SSH login attempts detected"

        if "DPT=21" in log or "DPT=22" in log or "DPT=23" in log:
            return "ATTACK", "Port scanning activity detected"

        if "FLAGS=SYN" in log and "DPT=80" in log:
            return "SUSPICIOUS", "Possible SYN flood attack"

        if "BYTES_SENT=" in log:
            try:
                bytes_sent = int(log.split("BYTES_SENT=")[1].split()[0])
                if bytes_sent > 5000000:
                    return "SUSPICIOUS", "Large data transfer detected"
            except:
                pass

        if "ACTION=BLOCK" in log:
            return "SUSPICIOUS", "Blocked unauthorized access attempt"

    # ✅ Default
    return "NORMAL", "General system activity detected"


def translate_log(log):
    start = time.time()

    status, explanation = analyze_log(log)

    end = time.time()

    return f"""
Status: {status}

Explanation: {explanation}

Time to Clarity: {round(end - start, 5)} seconds
"""
