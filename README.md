# Simple Commandline TODO application

### Installation
1. Clone Repo
2. Set full Todo Path in `config.json`
3. optional: set (permanent) alias for `todo.py` 
### Usage
```bash
python3 todo.py #Shows all Active Todos
python3 todo.py show #Shows all Active Todos
python3 todo.py showall #Shows all Todos
python3 todo.py add #Start todo Constructor
python3 todo.py add "Tag" "Name" "Date" #Add Todo Directly
python3 todo.py check #Start checking Constructor
python3 todo.py check "Index" #Checks of Index
```
### Configuration:
```json
"path":"todo.txt", //Path to Todo File
"renderASCII":false, //If Boxes should be rendered with Ascii Compatible Chars
"filetype":"txt" //Not yet used
```

### Planned Features
- Support for formatting Files in `.txt`, `.json`, `.toml`, `.yaml`, `.xml`, `.cfg`, `.md`,`.html`
- Functions for editing `config.json`
