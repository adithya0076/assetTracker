import os
import requests

def get_droplets():
    url = 'https://flespi.io/gw/devices/2438257/messages?data=%7B%7D'
    r = requests.get(url, headers={'Authorization':'Bearer %s' % 'FlespiToken ILAqNLKluS2NCLNmvb1DgZSDm3G7ye64Puls3TCozsZ14AcnA3QGTz75qD1OHXHk'})
    droplets = r.json()
    droplet_list = []
    for i in range(len(droplets['droplets'])):
        droplet_list.append(droplets['droplets'][i])
    return droplet_list