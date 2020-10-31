from jinja2 import Environment, FileSystemLoader
from config_params import fortigate_config_params
import os


class commandGenerator():

    def __init__(self, config, config_type):
        self.config = config
        self.config_type = config_type
        self.commands = []
        cwdir = os.getcwd()
        if "tests" in os.getcwd() or "api" in os.getcwd():
            split_dir = cwdir.split('/')
            split_dir.pop(-1)
            cwdir = ('/').join(split_dir)

        os.environ['APP_DIR'] = cwdir

    def update_config_type(self, config_type):
        self.config_type = config_type

    def config_fortigate(self, template_path):
        params = {}
        command_list = []
        template_name = None

        cp = fortigate_config_params.fortigate_config(self.config)
        if 'interface' in self.config['device']['configuration']:
            params = cp.interface_config(self.config['device']['configuration']['interface'])
            if self.config_type == 'configure':
                template_name = f"{self.config['device']['device_type']}_interface"
            elif self.config_type == 'backout':
                template_name = f"{self.config['device']['device_type']}_backout_interface"

        if 'static_route' in self.config['device']['configuration']:
            params = cp.static_route_config(self.config['device']['configuration']['static_route'])
            if self.config_type == 'configure':
                template_name = f"{self.config['device']['device_type']}_static_route"
            elif self.config_type == 'backout':
                template_name = f"{self.config['device']['device_type']}_backout_static_route"

        file_loader = FileSystemLoader(template_path)
        env = Environment(loader=file_loader, keep_trailing_newline=True, trim_blocks=True)
        template = env.get_template(template_name)
        output = template.render(params=params)
        command_list.append(output)

        self.commands = command_list

    def generateCommands(self):
        template_path = None
        app_dir = os.getenv("APP_DIR")
        if self.config_type == 'configure':
            template_path = f"{app_dir}/command_templates/config"
        elif self.config_type == 'backout':
            template_path = f"{app_dir}/command_templates/backout"
        else:
            print(f'invalid config type: {self.config_type}')

        if self.config['device']['device_type'] == 'fortigate':
            self.config_fortigate(template_path)

        return self.commands

if __name__ == "__main__":
    cg = commandGenerator(None, None)