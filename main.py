from parsers.syslog_parser import parse_syslog
from parsers.snmp_parser import parse_snmp
from parsers.vpc_parser import parse_vpc


def detect_log_type(log):
    if "SNMP" in log:
        return "SNMP"
    elif log.startswith("2 "):
        return "VPC"
    else:
        return "SYSLOG"


def process_log(log):
    log_type = detect_log_type(log)

    if log_type == "SYSLOG":
        return parse_syslog(log)
    elif log_type == "SNMP":
        return parse_snmp(log)
    elif log_type == "VPC":
        return parse_vpc(log)


# 🚀 ONLY runs when you execute main.py directly
if __name__ == "__main__":
    import time
    from models.anomaly_detector import AnomalyDetector
    from models.translator import translate_log

    logs = [
        "<34>Oct 11 22:14:15 server sshd: Failed password for root",
        "SNMP Trap: Link Down",
        "SNMP Trap: CPU High",
        "2 123456789 eni-abc123 10.0.0.1 10.0.0.2 443 51515 6 10 840 1622471123 1622471183 ACCEPT OK"
    ]

    processed_logs = [process_log(log) for log in logs]

    detector = AnomalyDetector()
    detector.train(processed_logs)

    for log in logs:
        start_time = time.time()

        parsed = process_log(log)
        status = detector.predict(parsed)
        explanation = translate_log(parsed)

        end_time = time.time()
        t2c = end_time - start_time

        print(parsed)
        print("Status:", status)
        print("Explanation:", explanation)
        print("Time to Clarity:", round(t2c, 5), "seconds")
        print("-" * 50)