import yaml


def yaml_coerce(value):
    # Convert value to proper Python

    if isinstance(value, str):
        # yaml.load returns a Python object (we are just creating some quick yaml data with a dummy key)
        # Converts string dict "{'apples': 1, 'bacon': 2}" to Python dict
        # Useful because sometimes we need to stringify settings this way (like in Dockerfiles)
        return yaml.load('dummy: ' + value, Loader=yaml.SafeLoader)['dummy']

    return value
