python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
pip install -e .

# Try with pyright - doesn't see docstrings for MyClass and it's methods, defined in base classes
pyright --verifytypes docstring_example
pyright --verifytypes docstring_example --outputjson >> docstring-example-verifytypes.json

# Try with Python's inspect.getdoc - does see the docstrings (source in getdoc.py)
python3 -m getdoc