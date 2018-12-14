s = """Мой дядя самых честных правил, Когда не в шутку 
занемог, Он уважать себя заставил И лучше выдумать не
мог"""

words = s.split()
new_words = [word for word in words if not word.startswith("м")]
print(" ".join(new_words))
