import time

def analyze_log(log):

    # Convert dict OR string → unified string
    if isinstance(log, dict):
        log_str = " ".join([f"{k}={v}" for k, v in log.items()])
    else:
        log_str = str(log)

    log_str = log_str.upper()

    # 🚨 BRUTE FORCE
    if "FAILED" in log_str and ("SSH" in log_str or "LOGIN" in log_str):
        return "ATTACK", "Multiple failed login attempts detected"

    # 🚨 PORT SCAN
    if any(p in log_str for p in ["DPT=21", "DPT=22", "DPT=23"]):
        return "ATTACK", "Port scanning activity detected"

    # 🚨 DDOS
    if "FLAGS=SYN" in log_str and "DPT=80" in log_str:
        return "SUSPICIOUS", "Possible SYN flood attack"

    # 🚨 DATA EXFILTRATION
    if "BYTES_SENT" in log_str:
        try:
            bytes_sent = int(log_str.split("BYTES_SENT=")[1].split()[0])
            if bytes_sent > 5000000:
                return "SUSPICIOUS", "Large data transfer detected"
        except:
            pass

    # 🚨 BLOCKED ACCESS
    if "ACTION=BLOCK" in log_str:
        return "SUSPICIOUS", "Blocked unauthorized access attempt"

    # 🚨 Sensitive ports
    if "DPT=3389" in log_str or "DPT=22" in log_str:
        return "SUSPICIOUS", "Access attempt to sensitive service port"

    return "NORMAL", "General system activity detected"


def translate_log(log):
    start = time.time()

    status, explanation = analyze_log(log)

    end = time.time()

    return f"""Status: {status}
Explanation: {explanation}
Time to Clarity: {round(end - start, 5)} seconds"""
