def create_log(timestamp, source, event, severity, protocol):
    return {
        "timestamp": timestamp,
        "source": source,
        "event": event,
        "severity": severity,
        "protocol": protocol
    }
