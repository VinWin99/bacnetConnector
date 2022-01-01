import BAC0
import PySimpleGUI as sg
import tkinter as tk

print("Connecting to Bacnet devices")
myIp = "xxx"
backnet = BAC0.connect(ip=myIp, port=47808)
mac, deviceId = backnet.whois()[0]
print("who is results: ", mac, deviceId)
# print(backnet.devices)
deviceName = backnet.devices[0][0]
# print(backnet.read(f' {mac} device {deviceId} objectList'))
#
# for x in range(11):
#     print(backnet.read(f' {mac} analogValue {x} presentValue'))
#
#
_rpm = {'address': mac,
        'objects': {
            'analogValue:17': ['objectName', 'presentValue', 'statusFlags', 'units', 'description'],
            'analogValue:18': ['objectName', 'presentValue', 'statusFlags', 'units', 'description']
            }
        }

print(backnet.readMultiple(mac,_rpm))
dictO = backnet.readMultiple(mac,_rpm)

keys = list(dictO.keys())

d1 = dictO.get(keys[0])
d2 = dictO.get(keys[1])

print(d1[0])
#
# backnet.write(f' {mac} analogValue 17 presentValue 61')

# define layout
layout1 = [[sg.Text('Set Value', size=(10, 1)), sg.Input('', key='eName')],
           [sg.Button('Update Value')]]
layout2 = [[sg.Text('Set Value', size=(10, 1)), sg.Input('', key='eName')],
           [sg.Button('Update Value')]]
layout3 = [[sg.Text('Set Value', size=(10, 1)), sg.Input('', key='eName')],
           [sg.Button('Update Value')]]
# Define Layout with Tabs




tabgrp = [
    [sg.TabGroup([[sg.Tab(d1[0][1], layout1, title_color='Indian Red', border_width=10, background_color='Ivory'),
                   sg.Tab('Education', layout2, title_color='Indian Red', background_color='Ivory'),
                   sg.Tab('Experience', layout3, title_color='Indian Red', background_color='Ivory')]], tab_location='centertop',
                 title_color='Indian Red', tab_background_color='Ivory', selected_title_color='Black',
                 selected_background_color='Indian Red', border_width=5), sg.Button('Close')]]

# Define Window
window = sg.Window(deviceName, tabgrp)
# Read  values entered by user
event, values = window.read()
# access all the values and if selected add them to a string
window.close()

# while True:
#     event, values = window.read()
#     if event == "CLOSE" or event == sg.WIN_CLOSED:
#         break
#
# window.close()

# window = tk.Tk()
#
# frame_a = tk.Frame(master=window)
#
# tag_a = tk.Label(master=frame_a, text="Analog Value 0: ")
# tag_a.pack()
#
# frame_b = tk.Frame(master=window)
#
# tag_b = tk.Label(master=frame_b, text="Analog Value 1: ")
# tag_b.pack()
#
# frame_c = tk.Frame(master=window)
#
# tag_c = tk.Label(master=frame_c, text="Analog Value 2: ")
# tag_c.pack()
#
# frame_d = tk.Frame(master=window)
#
# tag_d = tk.Label(master=frame_d, text="Analog Value 3: ")
# tag_d.pack()
#
# frame_a.pack()
# frame_b.pack()
# frame_c.pack()
# frame_d.pack()
#
# window.mainloop()
