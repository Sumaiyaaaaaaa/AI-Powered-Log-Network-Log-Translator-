import time

def analyze_log(log):
    try:
        # ✅ FORCE SAFE STRING CONVERSION
        log_str = str(log) if log is not None else ""

        log_str = log_str.upper()

        # 🚨 BRUTE FORCE
        if "FAILED" in log_str:
            return "ATTACK", "Multiple failed login attempts detected"

        # 🚨 PORT SCAN
        if any(p in log_str for p in ["DPT=21", "DPT=22", "DPT=23"]):
            return "ATTACK", "Port scanning activity detected"

        # 🚨 BLOCKED
        if "BLOCK" in log_str:
            return "SUSPICIOUS", "Blocked unauthorized access attempt"

        return "NORMAL", "General system activity detected"

    except Exception as e:
        return "ERROR", f"Processing failed: {str(e)}"


def translate_log(log):
    start = time.time()

    status, explanation = analyze_log(log)

    end = time.time()

    return f"""Status: {status}
Explanation: {explanation}
Time to Clarity: {round(end - start, 5)} seconds"""
