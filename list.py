list = ["bhavya",7,True]
print(list)

attendees=["bhavya","malika","saranya"]
attendees.insert(1,"chinni")
print(attendees)

attendees=["bhavya","malika","saranya"]
print(attendees.index("bhavya"))

attendees=["bhavya","malika","saranya"]
print(attendees.count("bhavya"))

attendees=["bhavya","malika","devapriyam","prasad"]
attendees[0]="bhavya saranya"
print(attendees)

attendees=["bhavya","malika","chinni"]
attendees1=["akhil","sai","siva"]
attendees.extend(attendees1)
print(attendees)

attendees=["bhavya","sirisha","malika"]
attendees.remove("malika")
print(attendees)

attendees=["bhavya","sirisha","malika"]
attendees.pop(2)
print(attendees)

attendees=["chinni","bhavya","saranya"]
attendees.pop()
print(attendees)

attendees=["chinni","bhavya","saranya"]
attendees.pop()
attendees.pop()
print(attendees)