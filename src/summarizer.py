def summarize(text):
    if len(text) > 150:
        return text[:150] + "..."
    return text