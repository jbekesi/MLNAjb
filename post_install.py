import os
import subprocess
import sys

def create_virtualenv(env_name='mlna_venv'):
    # Create virtual environment
    subprocess.check_call([sys.executable, '-m', 'venv', env_name])

    # Activate virtual environment
    if os.name == 'nt':
        activate_script = os.path.join(env_name, 'Scripts', 'activate')
    else:
        activate_script = os.path.join(env_name, 'bin', 'activate')

    # Install requirements
    requirements_file = 'requirements.txt'
    if os.path.exists(requirements_file):
        subprocess.check_call([activate_script, '&&', 'pip', 'install', '-r', requirements_file], shell=True)
    else:
        print(f"{requirements_file} not found, skipping installation of requirements.")

if __name__ == "__main__":
    create_virtualenv()
