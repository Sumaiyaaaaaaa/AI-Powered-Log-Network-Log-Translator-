def translate_log(log):
    event = log["event"].lower()

    if "failed password" in event:
        return "A login attempt failed. This could indicate unauthorized access."

    elif "accepted password" in event:
        return "A user successfully logged into the system."

    elif "link down" in event:
        return "The network connection is down. This may impact connectivity."

    elif "cpu usage high" in event:
        return "The system CPU usage is high. Performance may be affected."

    elif "accept" in event:
        return "Network traffic was allowed between two systems."

    else:
        return "General system activity detected."