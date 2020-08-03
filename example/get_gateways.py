from mihome.base import XiaomiConnection
from mihome.gateway import Gateway
from mihome.config_manager import YamlConfig
import ast
import pprint
import json

debug=False

conn = XiaomiConnection()
#gateway_data = conn.whois()
gateways_data = conn.list_gateways()

if debug: print gateways_data

# JSON export file
jfile={}

for gateway_data in gateways_data:

    if debug: print "\n>>>\n>>> gateway_data"+ '\n>>> '
    if debug: print gateway_data

    # Detect Gateway IP
    try:
        ip=gateway_data['ip'],
    except:
        try:
            dip=ast.literal_eval(gateway_data[u'data'])
            ip=dip['ip']
        except:
            ip=None

    # Detect Gateway Port
    try:
        port=gateway_data['port'],
    except:
        port=''

    if ip:
        gateway = Gateway(
	        connection=conn,
            sid=gateway_data['sid'],
            ip=ip,
            port=port,
        )


        if debug: print "\n>>>\n>>> gateway.get_subdevices()" + '\n>>> '
        gateway.get_subdevices()
        a=gateway.subdevices
        if debug: pprint.pprint(a)
        nb_obj=1
        for obj in gateway.subdevices:
            jfile[ obj['sid'] ] = "obj_%s %s" % (nb_obj, obj['model'])
            nb_obj+=1

        #gateway.register_subdevices()
        if debug: print "\n>>>\n>>> gateway.list_subdevices"+ '\n>>> '
        b=gateway.list_subdevices()
        if debug: pprint.pprint(b)

        if debug: print "\n>>>\n>>> gateway.connected_devices"+ '\n>>> '
        if debug: pprint.pprint(gateway.connected_devices)

jfile["gateways"] = {}
for gateway_data in gateways_data:
    jfile["gateways"][gateway_data['sid']] = "xxxxxxx"


j=json.dumps(jfile, sort_keys=True, indent=4)
print j

with open('devices.json', 'w') as outfile:
    json.dump(jfile, outfile, sort_keys=True, indent=4)


