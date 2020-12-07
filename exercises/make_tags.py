def make_tags(tag, word):
    start_tag = "<"+tag+">"
    end_tag = "<"+"/"+tag+">"
    return start_tag+word+end_tag
