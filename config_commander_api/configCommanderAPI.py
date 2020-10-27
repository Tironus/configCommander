import sys
import os

cwd = os.getcwd()
fmt_path = cwd.split('/')
fmt_path.pop(-1)
app_dir = ('/').join(fmt_path)
print(app_dir)

sys.path.append(os.getcwd())
sys.path.append(f'{app_dir}/models')
sys.path.append(app_dir)

import models
from configCommander import configCommander
from fastapi import FastAPI

app = FastAPI()


@app.post("/config_interface", response_model=models.ConfigResponse)
async def post_config(config_data: models.ConfigDeviceInterface):
    c = configCommander(config_data)
    results, status, msg = c.runConfig()
    return results


@app.post("/config_static_routes", response_model=models.ConfigResponse)
async def post_config(config_data: models.ConfigDeviceRoute):
    c = configCommander(config_data)
    results, status, msg = c.runConfig()
    return results
