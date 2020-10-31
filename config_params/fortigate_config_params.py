class fortigate_config():
    def __init__(self, config):
        self.config = config

    def interface_config(self, params):
        cfg = self.config["device"]["configuration"]["interface"]
        print(cfg["allow_access"])
        intf_params = {
            "id": cfg["id"],
            "ipv4_address": cfg["ipv4_address"],
            "ipv4_prefix_len": cfg["ipv4_prefix_len"],
            "allow_access": [i.value for i in cfg["allow_access"]]
        }
        return intf_params

    def static_route_config(self, params):
        params['static_route'] = []
        sr = self.config['device']['configuration']['static_route']
        route_params = {
            "id": sr["id"],
            "dst_ip": sr["dst_ip"],
            "dst_prefix_len": sr["dst_prefix_len"],
            "device": sr["device"],
            "gateway": sr["gateway"]
        }
        params['static_route'].append(route_params)
        return params