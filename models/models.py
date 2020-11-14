import enum
from pydantic import BaseModel
from typing import List, Optional, Dict, Union


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


class InterfaceValues(BaseModel):
    interfaces: List[InterfaceParams]


class StaticRouteParams(BaseModel):
    id: str
    dst_ip: str
    dst_prefix_len: str
    device: str
    gateway: str


class StaticRouteValues(BaseModel):
    static_route: List[StaticRouteParams]


class Device(BaseModel):
    hostname: str
    username: str
    password: str
    device_type: str
    firmware_version: str
    configuration: Optional[
        Union[
            InterfaceValues,
            StaticRouteValues
        ]
    ]


class ConfigResponse(BaseModel):
    results: Dict
    status: str
    msg: Optional[str]


class HealthResponse(BaseModel):
    status: str
    msg: Optional[str]