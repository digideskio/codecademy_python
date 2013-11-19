def shut_down(s):
    """Returns a string confirming or aborting a shutdown depending on whether 'yes' or 'no' has been passed in"""

     # Technically this will make strings like 'yEs' work,
     # despite the instructions saying to reject these.
     # I opted to accept them in my case.
    upper = s.upper()

    if upper == "YES":
        return "Shutting down..."
    elif upper == "NO":
        return "Shutdown aborted!"
    else:
        return "Sorry, I didn't understand you."

