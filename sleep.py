import time

def calm_message():
    messages = [
        "Breathe in... slow and deep.",
        "Hold... feel the calm.",
        "Breathe out... release the stress.",
        "Your mind is safe here.",
        "Peace grows with every breath."
    ]
    
    for msg in messages:
        print(msg)
        time.sleep(3)  # pause for 3 seconds to let the message sink in

calm_message()
