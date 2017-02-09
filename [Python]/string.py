str1 = "monkies monkey around like monkies do"
print str1.find("monkies")
print str1.replace("monkies","sharks")
list1 = [6,6,6,7,1]
print max(list1)
print min(list1)
list2 = ["Good morning",6,6,6,"Starshine"]
print list2[:1]
print list2[4:]
list22 = []
list22.append(list2[0])
list22.append(list2[4])
print list22
list4 = [6,6,666,-666,4,5]
list4.sort()
list5 = []
list5.append(list4[0])
list4.pop(0)
list4.insert(0,list5)
print list4
