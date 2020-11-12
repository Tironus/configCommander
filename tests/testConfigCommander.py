import configCommander

payload = {
    "device": {
        "hostname": "192.168.20.55",
        "username": "admin",
        "password": "admin",
        "device_type": "fortigate",
        "firmware_version": "5.6.4",
        "configuration": {
            "interface": {
                "id": "port5",
                "ipv4_address": "192.168.52.43",
                "ipv4_prefix_len": "24",
            },
            "static_route": {
                    "id": "100",
                    "dst_ip": "10.10.10.0",
                    "dst_prefix_len": "24",
                    "device": "port5",
                    "gateway": "192.168.52.44"
            }
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
    assert r2 == "failed"

if __name__ == "__main__":
    test_find_validation()
    test_runConfig()