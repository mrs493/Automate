#assertions serve as sanity checks that will crash code if they are not fulfilled
#they can be disable from the command line by passing the -0 switch after python and before the name of the file
#i.e. python -0 trafficLights.py

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key]=='green':
            stoplight[key] = 'yellow'
        elif stoplight[key]=='yellow':
            stoplight[key] = 'red'
        elif stoplight[key]=='red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither light is red!' + str(stoplight)

switchLights(market_2nd)