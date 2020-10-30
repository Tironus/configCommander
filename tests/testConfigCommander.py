from configCommander import configCommander

payload = {
    "device": {
        "hostname": "71.229.230.0",
        "username": "admin",
        "password": "admin",
        "device_type": "fortigate",
        "firmware_version": "5.6.4",
        "configuration": {
            "interface": [
                {
                    "id": "port5",
                    "ipv4_address": "192.168.52.43",
                    "ipv4_prefix_len": "24",
                    "allow_access": [
                        " ping",
                        " ssh",
                        " http",
                        " https",
                        " snmp"
                    ]
                },
                {
                    "id": "port6",
                    "ipv4_address": "192.168.72.43",
                    "ipv4_prefix_len": "24",
                    "allow_access": [
                        " ping",
                        " ssh",
                        " http",
                        " snmp"
                    ]
                },
                {
                    "id": "port7",
                    "ipv4_address": "192.168.74.43",
                    "ipv4_prefix_len": "24",
                    "allow_access": [
                        " ping"
                    ]
                }
            ],
            "static_route": [
                {
                    "id": "100",
                    "dst_ip": "10.10.10.0",
                    "dst_prefix_len": "24",
                    "device": "port5",
                    "gateway": "192.168.52.44"
                },
                {
                    "id": "101",
                    "dst_ip": "10.10.11.0",
                    "dst_prefix_len": "24",
                    "device": "port5",
                    "gateway": "192.168.52.44"
                },
                {
                    "id": "102",
                    "dst_ip": "10.10.12.0",
                    "dst_prefix_len": "24",
                    "device": "port5",
                    "gateway": "192.168.52.44"
                }
            ]
        }
    }
}

def test_find_validation():
    testConfig = configCommander(payload)
    results = testConfig.find_validation()
    assert results is not None

def test_runConfig():
    testConfig = configCommander(payload)
    r1, r2, r3 = testConfig.runConfig()
    assert r2 == "success"