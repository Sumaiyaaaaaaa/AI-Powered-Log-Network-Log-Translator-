from models.schema import create_log

def parse_vpc(log):
    try:
        parts = log.split()

        return create_log(
            timestamp=parts[10],
            source=parts[2],
            event=f"{parts[3]} -> {parts[4]} action: {parts[12]}",
            severity="low",
            protocol="VPC"
        )

    except:
        return {
            "error": "Failed to parse VPC log",
            "raw": log
        }
