pepData = [
    {"name" : "samim", "FatherName" : "Nader", "age" : 15, "livedCity": ["Herat", "Islam Abad", "Kabul"]},
    {"name" : "shayan", "FatherName" : "Ghafar", "age" : 14, "livedCity": ["Herat",  "Kabul"]}

           ]
for i in pepData[0]["livedCity"]:

    print(f"{pepData[1]["name"]} lived in {i} ")