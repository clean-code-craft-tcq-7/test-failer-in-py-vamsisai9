prod_network_alert_count = 0

def network_alert_pro(celcius):
    print(f'ALERT: Temperature is {celcius} celcius') 
    global prod_network_alert_count
    prod_network_alert_count+=1

    return 200 