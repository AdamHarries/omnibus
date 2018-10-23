#!/usr/bin/python3
try: 
    import requests
    import json

    # This is the specific stop ID for the busses that I want.
    stop_id = "6200203090"
    # And the specific bus number: 
    service_name = "2"

    # Query the URL, and check the result
    r = requests.get("https://tfeapp.com/api/website/stop_times.php?stop_id=%s" % stop_id)
    if r.status_code != 200: 
        raise Exception

    bus_data = r.json()

    # Select the services.
    services = bus_data['services']
    
    service = None 
    for s in services: 
        if s['service_name'] == service_name: 
            service = s
    if service == None: 
        raise Exception("No service (%s) found." % service_name)

    # Now we have our service, get the next few departures
    times = []
    for d in service['departures']: 
        times.append(d['minutes'])

    # Print min(n,3) bus times.
    if len(times) > 3: 
        times = times[:3]

    tstr = '/'.join(map(str,times))

    output = "Next #%s bus in %s minutes" % (service_name, tstr)
    print(output)
    

except Exception as e:
    if e.args == []:
        print("Failed to get bus data.")
    else: 
        print(str(e.args[0]))


