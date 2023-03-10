def estimate_reading_time(text):
    
    if type(text) is str:
        word_list = text.split()
        num_words = len(word_list)
        minutes = num_words / 200
        reply = " Minutes to read this text"
        result = str(minutes) + reply
        return result
    else:
        return "This function will only accept a string"