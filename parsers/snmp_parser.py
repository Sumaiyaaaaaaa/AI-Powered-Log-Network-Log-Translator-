from models.schema import create_log

def parse_snmp(log):
    if "Link Down" in log:
        return create_log("unknown", "SNMP Device", "Network link down", "high", "SNMP")

    elif "CPU High" in log:
        return create_log("unknown", "SNMP Device", "CPU usage high", "medium", "SNMP")

    else:
        return create_log("unknown", "SNMP Device", "Unknown event", "low", "SNMP")
