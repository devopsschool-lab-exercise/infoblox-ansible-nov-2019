#To create a nw on Infoblox grid
#!/usr/bin/python
# pip install infoblox-client
import json
import logging
logging.basicConfig(level=logging.DEBUG)
from infoblox_client import connector
from infoblox_client import objects

def main():
    module = AnsibleModule(
        argument_spec=dict(
            host=dict(required=True),
            username=dict(required=True),
            password=dict(required=True)
        ),
    )

    infohost = module.params['host']
    infousername = module.params['username']
    infopassword = module.params['password']

    opts = {'host': infohost, 'username': infousername, 'password': infopassword}
    conn = connector.Connector(opts)

    #curl_result_dict = json.loads(conn[1])
    #http_resp_code = curl_result_dict['cod']

    network = objects.Network.create(conn, network_view='default',
                                 cidr='12.0.0.0/24')

    module.exit_json(changed=True, decision='tp')

from ansible.module_utils.basic import *
main()
