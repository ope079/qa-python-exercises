def case_count(word):
    lower_count = sum(1 for c in word if c.islower() )
    upper_count = sum(1 for c in word if c.isupper())
    return f"UPPER CASE {upper_count} \nLOWER CASE {lower_count}"
