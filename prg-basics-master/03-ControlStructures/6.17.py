time = input('Enter time (24-hour format): ')
if time [:2] == '13':
    print(f'Time in 12-hour format: 1:{time[3:5]}')
elif time [:2] == '14':
    print(f'Time in 12-hour format: 2:{time[3:5]}')
elif time [:2] == '15':
    print(f'Time in 12-hour format: 3:{time[3:5]}')
elif time [:2] == '16':
    print(f'Time in 12-hour format: 4:{time[3:5]}')
elif time [:2] == '17':
    print(f'Time in 12-hour format: 5:{time[3:5]}')
elif time [:2] == '18':
    print(f'Time in 12-hour format: 6:{time[3:5]}')
elif time [:2] == '19':
    print(f'Time in 12-hour format: 7:{time[3:5]}')
elif time [:2] == '20':
    print(f'Time in 12-hour format: 8:{time[3:5]}')
elif time [:2] == '21':
    print(f'Time in 12-hour format: 9:{time[3:5]}')
elif time [:2] == '22':
    print(f'Time in 12-hour format: 10:{time[3:5]}')
elif time [:2] == '23':
    print(f'Time in 12-hour format: 11:{time[3:5]}')
elif time [:2] == '24' or time [:2] == '00':
    print(f'Time in 12-hour format: 12:{time[3:5]}')
else:
    print(f'Time in 12-hour format: {time}')

#time = input('Enter time (24-hour format): ')
#hour = int(time[:2])
#minutes = time[3:5]

#if hour == 0:
    #hour_12 = 12
#elif hour > 12:
    #hour_12 = hour - 12
#else:
    #hour_12 = hour
#print(f'Time in 12-hour format: {hour_12}:{minutes}')
