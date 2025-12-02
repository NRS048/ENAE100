import serial, re, os, time, json, csv

ser = serial.Serial('COM12', 115200)  # open serial port
print(ser.name, "\n")

absolute_path = os.path.dirname(os.path.abspath(__file__))
filename = absolute_path + '/datalog.json'

i = time.time()

test_period = 15 #time in seconds

data_dump = []

print("working")

while True:
    if time.time() - i > test_period:
        break

    print(time.time() - i)
    
    print(ser.readline().decode("utf-8"))

    data_dump.append(re.sub(",", " ", ser.readline().decode("utf-8")))

    #with open(filename, 'w+', encoding='utf-8') as f:
    #    print(json.load(f))
    #
    #    json.dump(data, f, ensure_ascii=False, indent=4)
    
with open('output.csv', 'w', newline='') as file:
    print("file")

    j = 0

    while j < len(data_dump):
        file.write(data_dump[j])
        j += 1


#print(data_dump)

print("done - SAVE DATA")
# this code makes me want to cry
