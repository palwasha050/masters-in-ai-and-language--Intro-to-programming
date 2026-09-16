def is_un_able(word):
    """Check if a word follows the un-X-able pattern."""
    if word == "unable":
        return False
    return word.startswith("un") and word.endswith("able")
