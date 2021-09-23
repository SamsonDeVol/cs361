#Samson DeVol, CS361, 9/22/21
#Exercise 0, Racers

#Header
print("\n")
print("==============================")
print("2021 F1 Drivers Alphabetically")
print("==============================")
print("\n")

#Open and read Driver text file
f = open('CS361 Exercise 0 2021 F1 Drivers.txt', 'r')
content = f.read()
content_list = content.splitlines()

#Dict to store drivers by last name
alphabetical = {}

#Extract key[last_name] (always second word)
for driver in content_list:
    last_name = driver.split(" ")[1]
    alphabetical[last_name] = driver

#Sort by key[Last name]     
sorted_alphabetical = sorted(alphabetical)

#Print value[driver] by sorted key[last name]
for driver in sorted_alphabetical:
    print(alphabetical[driver])

#Header 2
print("\n")
print("==============================")
print("2021 F1 Drivers Numerically")
print("==============================")
print("\n")

#Dict to store drivers by number
numerical  = {}

#Extract key[racer number]
driver_idx = 0
for driver in content_list:
    for i in content_list[driver_idx].split():
        #Find number within driver string using .isdigit() method
        if i.isdigit():
            driver_num = int(i)
            #Add key[driver number] and value [driver]
            numerical[driver_num] = driver
    driver_idx += 1

#Sort dict by key[driver number]
sorted_numerical = sorted(numerical)

#Print value[driver] in order of key[driver number]
for driver in sorted_numerical:
    print(numerical[driver])

f.close()