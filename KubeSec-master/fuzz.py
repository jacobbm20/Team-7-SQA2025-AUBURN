
import random
import string
import os
import tempfile
import traceback
import importlib.util
import sys

# Triggering GitHub Actions 2

# Force import of local parser.py as parser_local
parser_path = os.path.join(os.path.dirname(__file__), "parser.py")
spec = importlib.util.spec_from_file_location("parser_local", parser_path)
parser = importlib.util.module_from_spec(spec)
sys.modules["parser_local"] = parser
spec.loader.exec_module(parser)

from parser_local import loadMultiYAML, getKeyRecursively, getValuesRecursively
from scanner import scanForAllowPrivileges
from graphtaint import getTaintsFromConfigMaps

def random_yaml_content():
    keys = ["key", "value", "apiVersion", "kind", "metadata", "spec"]
    val = lambda: ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    return f"{random.choice(keys)}: {val()}\n" * random.randint(1, 10)

def write_temp_yaml():
    content = random_yaml_content()
    fd, path = tempfile.mkstemp(suffix=".yaml", text=True)
    with os.fdopen(fd, 'w') as tmp:
        tmp.write(content)
    return path

def fuzz_loadMultiYAML():
    print("\nFuzzing loadMultiYAML")
    try:
        path = write_temp_yaml()
        loadMultiYAML(path)
        print(f"✓ Success: {path}")
    except Exception as e:
        print(f"✗ Crash in loadMultiYAML: {e}\n{traceback.format_exc()}")

def fuzz_getKeyRecursively():
    print("\nFuzzing getKeyRecursively")
    try:
        fake_dict = {''.join(random.choices(string.ascii_letters, k=3)): "value" for _ in range(5)}
        result_list = []
        getKeyRecursively(fake_dict, result_list)
        print(f"✓ Output: {result_list}")
    except Exception as e:
        print(f"✗ Crash in getKeyRecursively: {e}\n{traceback.format_exc()}")

def fuzz_getValuesRecursively():
    print("\nFuzzing getValuesRecursively")
    try:
        nested_dict = {f"key{i}": {"subkey": f"val{i}"} for i in range(5)}
        result = getValuesRecursively(nested_dict)
        print(f"✓ Output: {result}")
    except Exception as e:
        print(f"✗ Crash in getValuesRecursively: {e}\n{traceback.format_exc()}")

def fuzz_scanForAllowPrivileges():
    print("\nFuzzing scanForAllowPrivileges")
    try:
        path = write_temp_yaml()
        scanForAllowPrivileges(path)
        print(f"✓ Success: {path}")
    except Exception as e:
        print(f"✗ Crash in scanForAllowPrivileges: {e}\n{traceback.format_exc()}")

def fuzz_getTaintsFromConfigMaps():
    print("\nFuzzing getTaintsFromConfigMaps")
    try:
        path = write_temp_yaml()
        getTaintsFromConfigMaps(path)
        print(f"✓ Success: {path}")
    except Exception as e:
        print(f"✗ Crash in getTaintsFromConfigMaps: {e}\n{traceback.format_exc()}")

if __name__ == "__main__":
    for _ in range(10):  # Run 10 times for each
        fuzz_loadMultiYAML()
        fuzz_getKeyRecursively()
        fuzz_getValuesRecursively()
        fuzz_scanForAllowPrivileges()
        fuzz_getTaintsFromConfigMaps()
