import re

def wrap_with_tag(string, term, pre_tag='<em>', post_tag='</em>'):
    pattern = re.compile(re.escape(term), re.IGNORECASE)
    return pattern.sub('%s\g<0>%s' % (pre_tag, post_tag), string)


sample = "hello here all text from python text which wraps texts"
search_term = "text"

r = wrap_with_tag(sample, search_term)

print(r)
# >> "hello here all <em>text</em> from python <em>text</em> which wraps <em>text</em>s"
