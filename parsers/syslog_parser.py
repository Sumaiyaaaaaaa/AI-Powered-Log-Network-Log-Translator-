from models.schema import create_log

def parse_syslog(log):
    try:
        parts = log.split()

        return create_log(
            timestamp=" ".join(parts[0:3]),
            source=parts[3],
            event=" ".join(parts[5:]),
            severity="medium",
            protocol="SYSLOG"
        )

    except:
        return {"error": "Failed to parse log", "raw": log}
