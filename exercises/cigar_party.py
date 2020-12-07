def cigar_party(cigars, is_weekend):
    if not is_weekend and (cigars < 40 or cigars > 60):
        return False
    elif is_weekend and cigars < 40:
        return False
    elif is_weekend and cigars >= 40 :
        return True
