from datetime import datetime

# function: sample response
def sample_response(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "hey", "sup", "yo"):
        return "Hello, how are you?"

    if user_message in ("who are you?", "who are you", "what is your name?"):
        return "I am dprincecoder BOT"

    if user_message in ("time", "what time is it?", "what is the time?"):
        now  = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return "The time is: " + str(date_time)

    return "I don't understand you"