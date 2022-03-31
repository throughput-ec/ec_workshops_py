#Create the dictionary

dataset1 = {
            "archiveType":"marinesediment",
            "geo":{"lat":-5,"lon":140},
            "data":{"values":[1,2,3],"units":"N/A"}
            }

print(dataset1)
# return latitude into a variable

latitude = dataset1["geo"]["lat"]

print(latitude)
