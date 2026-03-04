from config import settings
import platform
import sys


def create_allure_environment_file():
    items = settings.model_dump()
    items["os_info"] = f"{platform.system()}, {platform.release()}"
    items["python_version"] = sys.version

    properties = "\n".join([f"{key}={value}" for key, value in items.items()])

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w') as file:
        file.write(properties)
