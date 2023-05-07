# codec

A simple utility to concatenate and reconstruct Python projects. It allows you to concatenate all `.py` files in a project into a single text file, and then reconstruct the original project structure from the concatenated file.

## Installation

```bash
pip install codec
```

## Usage
### concat
To concatenate a project:

```bash
codec concat <project_folder>
```

This will create a file named `<project_folder>.txt` with the concatenated source code.

### decat
To reconstruct a project:

```bash
codec decat <project_folder>
```

This will read the `<project_folder>.txt` file and reconstruct the original project structure in the specified folder.

## License
This project is licensed under the MIT License. See the LICENSE file for details.