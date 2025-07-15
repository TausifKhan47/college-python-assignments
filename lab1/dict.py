dict1={"comp":"computer","sci":"science"}
print(dict1["comp"])
dict2={"123":"computer","456":"maths"}
print(dict2["123"])
print(dict1["comp"]+dict2["123"])
#Check 
#print(dict1+ dict2)
#print(dict1[“computer”]+ dict2[“computer”])
#Python does not allow adding dictionaries directly using +.
#"computer" is not a key in dict1.
#The key in dict1 is "comp", not "computer".
#Similarly, "computer" is also not a key in dict2.

