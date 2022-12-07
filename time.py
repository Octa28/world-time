import time

#Capital cities + time zones
capital_cities = {
    'Tokyo': 'Asia/Tokyo',
    'Moscow': 'Europe/Moscow',
    'New Delhi': 'Asia/Kolkata',
    'Washington D.C.': 'America/New_York',
    'London': 'Europe/London',
    'Beijing': 'Asia/Shanghai',
    'Canberra': 'Australia/Sydney',
    'Ottawa': 'America/Toronto',
    'Paris': 'Europe/Paris',
    'Madrid': 'Europe/Madrid',
    'Mexico City': 'America/Mexico_City',
}

while True:
    city = input('Enter the name of a capital city: ')
    if city not in capital_cities:
        print('Sorry, that city is not in the list.')
        continue

# Get the current time (using the city's time zone)
    timezone = capital_cities[city]
    local_time = time.strftime('%I:%M %p', time.localtime(time.time()))
    print(f'{city}: {local_time}')
    print()