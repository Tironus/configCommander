import enum
from pydantic import BaseModel
from typing import List, Optional, Dict


class AllowAccess(enum.Enum):
    ssh = 'ssh'
    http = 'http'
    https = 'https'
    snmp = 'snmp'


class DevicePorts(enum.Enum):
    port1 = 'port1'
    port2 = 'port2'
    port3 = 'port3'
    port4 = 'port4'


class InterfaceParams(BaseModel):
    id: str
    ipv4_address: str
    ipv4_prefix_len: int
    allow_access: List[AllowAccess]


class InterfaceValues(BaseModel):
    interface: InterfaceParams


class StaticRouteParams(BaseModel):
    id: str
    dst_ip: str
    dst_prefix_len: str
    device: List[DevicePorts]
    gateway: str


class StaticRouteValues(BaseModel):
    static_route: StaticRouteParams


class ConfigDevice(BaseModel):
    hostname: str
    username: str
    password: str
    device_type: str
    firmware_version: str


class ConfigInterface(ConfigDevice):
    configuration: Optional[InterfaceValues]


class ConfigRoutes(ConfigDevice):
    configuration: Optional[StaticRouteValues]


class ConfigDeviceInterface(BaseModel):
    device: Optional[ConfigInterface]


class ConfigDeviceRoute(BaseModel):
    device: Optional[ConfigRoutes]


class ConfigResponse(BaseModel):
    results: Dict
    status: str
    msg: str
