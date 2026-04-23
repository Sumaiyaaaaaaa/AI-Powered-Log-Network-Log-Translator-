def analyze_log(log):
    log = log.upper()

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
        return "SUSPICIOUS", "Blocked unauthorized access"

    return "NORMAL", "General system activity detected"
