from jinja2 import Environment, FileSystemLoader
import os


class commandGenerator():

    def __init__(self, config, config_type):
        if isinstance(config, dict):
            self.config = config
        else:
            self.config = config.dict()
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

        for idx, cfg in enumerate(self.config['device']['configuration']):
            if "interfaces" in cfg.keys():

                params['interfaces'] = self.config['device']['configuration'][idx]['interfaces']
                if self.config_type == 'configure':
                    template_name = f"{self.config['device']['device_type']}_interface"
                elif self.config_type == 'backout':
                    template_name = f"{self.config['device']['device_type']}_backout_interface"

                command_list.append(self.jinja_process(template_path, template_name, params))
            if "static_routes" in self.config['device']['configuration'][idx].keys():
                params['static_routes'] = self.config['device']['configuration'][0]['static_routes']
                if self.config_type == 'configure':
                    template_name = f"{self.config['device']['device_type']}_static_route"
                elif self.config_type == 'backout':
                    template_name = f"{self.config['device']['device_type']}_backout_static_route"

                command_list.append(self.jinja_process(template_path, template_name, params))

        self.commands = command_list

    def jinja_process(self, template_path, template_name, params):
        file_loader = FileSystemLoader(template_path)
        env = Environment(loader=file_loader, keep_trailing_newline=True, trim_blocks=True)
        template = env.get_template(template_name)
        output = template.render(params=params)
        return output


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