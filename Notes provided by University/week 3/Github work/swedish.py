def lemmatize_regular_verb(verb):
    """Convert regular Swedish verbs to infinitive form."""
    if verb.endswith("ar"):
        return verb[:-2] + "a"
    elif verb.endswith("ade"):
        return verb[:-3] + "a"
    elif verb.endswith("at"):
        return verb[:-2] + "a"
    else:
        return verb
