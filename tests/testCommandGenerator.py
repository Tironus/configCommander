import commandGenerator

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

def test_update_config_type():
    testGenerator = commandGenerator.commandGenerator(payload, 'configure')
    testGenerator.update_config_type('test')
    assert "test" in testGenerator.config_type

def test_generate_commands():
    testGenerator = commandGenerator.commandGenerator(payload, 'configure')
    results = testGenerator.generateCommands()
    print(results)
    assert results is not []

if __name__ == "__main__":
    test_generate_commands()
    test_update_config_type()