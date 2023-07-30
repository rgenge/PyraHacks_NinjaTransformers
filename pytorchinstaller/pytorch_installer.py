import os
import subprocess
import re

# Get CUDA version
nvcc_version = subprocess.check_output(['nvcc', '--version']).decode('utf8')

# Extract the version number
version_number = re.search(r'release (\d+\.\d+)', nvcc_version).group(1)

#format for pip install
version_string=str(version_number)
version_strings=version_string.split(".")
version="".join(version_strings)


print("Version: ",version_number)
command_string="pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu"+str(version)
print("Running command: ",command_string)

os.system('cmd /k "' + command_string+ '"')