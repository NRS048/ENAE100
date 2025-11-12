import serial, re, os, time, json

ser = serial.Serial('COM12', 9600)  # open serial port
print(ser.name, "\n")

absolute_path = os.path.dirname(os.path.abspath(__file__))
filename = absolute_path + '/datalog.json'

i = time.time()

test_period = 10

while True:
    if time.time() - i > test_period:
        break

    data = re.split("\s", ser.readline().decode("utf-8"))
    del data[3]
    del data[3]

    print(data)

    with open(filename, 'w+', encoding='utf-8') as f:
        print(json.load(f))

        json.dump(data, f, ensure_ascii=False, indent=4)
    
print("done")