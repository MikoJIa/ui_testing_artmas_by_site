import os
import sys

python_path = os.path.dirname(sys.executable)
python_version = sys.version

print(python_version)
print(python_path)