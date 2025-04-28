4b. Fuzzing Activities

For the fuzzing task, we created a fuzz.py script inside the KubeSec-master directory.
The goal was to fuzz five methods from the existing codebase. We selected the following methods:

loadMultiYAML from parser.py
getKeyRecursively from parser.py
getValuesRecursively from parser.py
scanForAllowPrivileges from scanner.py
getTaintsFromConfigMaps from graphtaint.py

The script randomly generated inputs like fake YAML files and random keys to test the functions.
We set up a GitHub Actions workflow (fuzz.yml) to automatically run fuzz.py on every push and pull request.
Most functions handled fuzzing well. At first, scanForAllowPrivileges caused an error due to a missing method, but it was fixed by adjusting imports.
After that, fuzzing completed without major issues.