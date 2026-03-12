import serial
import csv
import os

ser = serial.Serial("COM3",115200)
line = ser.readline().decode("utf-8",errors="ignore").strip()


for x in range(4):
    print(line)
    parts = line.split(",")
    #print(parts)
    BR3_sim_result = parts[0]
    moisture = parts[1]
    extTemp = parts[2]
    print("MySimResult is ", BR3_sim_result, "My Moisture is ", moisture, "MyTemp is ", extTemp, )
    
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([BR3_sim_result,moisture,extTemp,])

