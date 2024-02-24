string="umbrellai"
vowel="aeiou"
collector_str=""
finalstring=""
for i in string:
    if i in vowel:
        collector_str+=i
collector_str=collector_str[::-1]
j=0
for i in string:
    if i in collector_str:
        finalstring+=collector_str[j]
        j+=1
    else:
        finalstring+=i
print(finalstring)