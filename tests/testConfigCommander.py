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
                    "ipv4_prefix_len": "24",
                },
                {
                    "id": "port6",
                    "ipv4_address": "192.168.6.6",
                    "ipv4_prefix_len": "24",
                },
                {
                    "id": "port7",
                    "ipv4_address": "192.168.7.7",
                    "ipv4_prefix_len": "24",
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


def test_find_validation():
    testConfig = configCommander.configCommander(payload)
    results = testConfig.find_validation()
    assert results is not None


def test_runConfig():
    testConfig = configCommander.configCommander(payload)
    r1, r2, r3 = testConfig.runConfig()
    print(r2)
    if r2 == "success":
        assert r2 == "success"
    else:
        assert r2 == "failed"

if __name__ == "__main__":
    test_find_validation()
    test_runConfig(local_run=True)