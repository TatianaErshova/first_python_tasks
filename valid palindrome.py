s = "A man, a plan, a canal: Panama"
s_low = s.lower()
s_corr = s_low
for i in range(len(s_low)):
    if not(s_low[i].isalnum()):
        s_corr = s_corr.
s_rev = s_corr[::-1]
if s_corr == s_rev:
    return(True)
else:
    return(False)


