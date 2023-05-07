# ppu

A simple utility to pack (concatenate) and unpack (reconstruct) tiny Python projects. It allows you to concatenate all `.py` files in a project into a single text file, and then reconstruct the original project structure from the concatenated file.

This is made for my own very specific use case and it's offered as is with no guarantees that it will work for you.

## Installation

```bash
pip install git+https://github.com/niccolofavari/ppu.git
```

## Usage
### pack
To concatenate a project:

```bash
ppu pack <project_folder>
```

This will create a file named `<project_folder>.txt` with the concatenated source code.

### unpack
To reconstruct a project:

```bash
ppu unpack <project_folder>
```

This will read the `<project_folder>.txt` file and reconstruct the original project structure in the specified folder.

## License
This project is licensed under the MIT License. See the LICENSE file for details.