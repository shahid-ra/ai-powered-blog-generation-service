import os
import re
import yaml

class EnvValLoader(yaml.SafeLoader):
		pass

pattern = re.compile(r'\$\{(\w+)\}')

def env_val_constructor(loader, node):
		value = loader.construct_scalar(node)
		matches = pattern.findall(value)
		if matches:
			for match in matches:
					env_value = os.getenv(match, '')
					value = value.replace(f'${{{match}}}', env_value)
		return value

EnvValLoader.add_implicit_resolver('!ENV', pattern, None)
EnvValLoader.add_constructor('!ENV', env_val_constructor)

def read_settings(env: str) -> dict:
	with open(f'./app/configs/config_{env}.yml', 'r') as file:
		config = yaml.load(file, Loader=EnvValLoader)
	return config

environment = os.getenv('ENVIRONMENT', 'dev').lower()
config = read_settings(environment)