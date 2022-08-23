class ConfigLoader:
    @staticmethod
    def load():
        with open('config/appsettings.yml') as yml_file:
            import yaml
            cfg = yaml.full_load(yml_file)
            return cfg
