class fortigate_config():
    def __init__(self, config):
        self.config = config

    def interface_config(self, params):
        cfg = self.config["device"]["configuration"]["interface"]
        print(cfg)
        intf_params = {
            "id": intf["id"],
            "ipv4_address": intf["ipv4_address"],
            "ipv4_prefix_len": intf["ipv4_prefix_len"],
            "allow_access": intf["allow_access"]
        }
        return intf_params

    def static_route_config(self, params):
        params['static_route'] = []
        sr = self.config['device']['configuration']['static_route']
        route_params = {
            "id": static_route["id"],
            "dst_ip": static_route["dst_ip"],
            "dst_prefix_len": static_route["dst_prefix_len"],
            "device": static_route["device"],
            "gateway": static_route["gateway"]
        }
        params['static_route'].append(route_params)
        return params