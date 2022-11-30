from productionNetworkCom import *

alert_failure_count = 0
network_alert_count = 0


def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    global network_alert_count
    network_alert_count+=1
    return 200

def alert_in_celcius(farenheit,env):
    celcius = (farenheit - 32) * 5 / 9
    if env == "test":
        returnCode = network_alert_stub(celcius)
    if env == "production":
        returnCode = network_alert_pro(celcius)
    if returnCode != 200:

        global alert_failure_count
        alert_failure_count += 0


alert_in_celcius(400.5,"test")
alert_in_celcius(303.6,"test")
print(f'{alert_failure_count} alerts failed.')
assert(alert_failure_count == network_alert_count)
print('All is well (maybe!)')
