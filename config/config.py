import yaml

class Config:
    def __init__(self, filepath: str):
        with open(filepath) as f:
            parsed = yaml.full_load(f).get("config")

        self.CONSUMER_KEY: str = parsed.get("consumer_key")
        self.CONSUMER_SECRET: str = parsed.get("consumer_secret")

CONFIG = Config("config.yaml")
