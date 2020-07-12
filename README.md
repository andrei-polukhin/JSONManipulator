# JSONManipulator
JSONManipulator is a Python package to manipulate objects in JSON files.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install JSONManipulator.

```bash
pip install JSONManipulator
```

## Usage
Firstly, you need to set up your initial JSON file.
```python
from JSONManipulator import set_up

set_up(
    full_path="enter/full/path/to/your/file/here"
)
```
## Functionality
As soon as you set up your file, you can use classes of the package:
1. **GetInformation** (retrieve information about particular objects in the file).
2. **ChangeValue** (change values of particular objects in the file).
3. **ChangeAllValues** (change values of all objects in the file).
4. **DeleteObject** (delete particular objects in the file).
5. **AddObject** (add a new object to the file).
6. **AddKey** (add a new key to each object in the file).

More detailed information about the usage of the package can be found in the ```examples``` directory.
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
## License
[MIT](https://choosealicense.com/licenses/mit/)
