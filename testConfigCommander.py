from configCommander import configCommander
from commandGenerator import commandGenerator

import configCommander

payload = {
    "device": {
        "hostname": "192.168.20.55",
        "username": "admin",
        "password": "admin",
        "device_type": "fortigate",
        "firmware_version": "5.6.4",
        "configuration": {
            "interfaces": [
                {
                    "id": "port5",
                    "ipv4_address": "192.168.5.5",
                    "ipv4_prefix_len": "24"
                },
                {
                    "id": "port6",
                    "ipv4_address": "192.168.6.6",
                    "ipv4_prefix_len": "24"
                },
                {
                    "id": "port7",
                    "ipv4_address": "192.168.7.7",
                    "ipv4_prefix_len": "24"
                }
            ],
            "static_routes": [
                {
                    "id": "100",
                    "dst_ip": "10.10.10.0",
                    "dst_prefix_len": "24",
                    "device": "port5",
                    "gateway": "192.168.5.50"
                },
                {
                    "id": "101",
                    "dst_ip": "11.11.11.0",
                    "dst_prefix_len": "24",
                    "device": "port6",
                    "gateway": "192.168.6.60"
                },
                {
                    "id": "102",
                    "dst_ip": "12.12.12.0",
                    "dst_prefix_len": "24",
                    "device": "port7",
                    "gateway": "192.168.7.70"
                }
            ]
        }
    }
}

test_api = {
  "device": {
    "hostname": "192.168.20.8",
    "username": "admin",
    "password": "admin",
    "device_type": "fortigate",
    "firmware_version": "5.6.4",
    "configuration": {
      "id": "500",
      "dst_ip": "50.50.50.0",
      "dst_prefix_len": "24",
      "device": [
        "port2"
      ],
      "gateway": "192.168.52.44"
    }
  }
}

c = configCommander.configCommander(payload)
ret, status, msg = c.runConfig()


print(f'COMMAND RESULTS: {status}')
print(f'msg: {msg}')
print('=================================')
print('=================================\n')
for result in ret:
    print(f'command: {result}')
    print(f'command submitted: {ret[result]["submit_config_result"]}')
    print(f'command result: {ret[result]["device_accepted_result"]}\n')
    print(f'{ret[result]["device_output"]}')
    print('=================================')
    print('=================================\n')