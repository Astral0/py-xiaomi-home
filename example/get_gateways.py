from mihome.base import XiaomiConnection
from mihome.gateway import Gateway
from mihome.config_manager import YamlConfig

conn = XiaomiConnection()
#gateway_data = conn.whois()
gateway_data = conn.list_gateways()


