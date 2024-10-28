import yaml
import subprocess

# Read the environment.yml file
with open("environment.yml", "r") as file:
    env_data = yaml.safe_load(file)

# Get the dependencies list
dependencies = env_data.get("dependencies", [])

# Iterate through dependencies and add each to poetry
for dependency in dependencies:
    # Check if it is a pip-installed item
    if isinstance(dependency, dict) and "pip" in dependency:
        pip_deps = dependency["pip"]
        for pip_dep in pip_deps:
            subprocess.run(["poetry", "add", pip_dep])
    elif isinstance(dependency, str):
        # Standard dependency
        subprocess.run(["poetry", "add", dependency])
    elif isinstance(dependency, dict):
        # Versioned dependency
        for dep_name, dep_version in dependency.items():
            subprocess.run(["poetry", "add", f"{dep_name}=={dep_version}"])
