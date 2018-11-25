s = "У лукоморья 123 дуб зеленый 456"
print (s.find("я"))
print (s.count("у"))
if s.isalpha() == False:
    print (s.upper())
if len(s) > 4:
    print (s.lower())
b = s[:5] + "М" + s[6:]
print (b)
