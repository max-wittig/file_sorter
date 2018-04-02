# file_sorter
sorts files into directories, based on their file extension

## usage
1. download release .egg  
2. run release egg on the folder you want to sort `python3 file_sorter.egg /home/$USER/Download/`

```
usage: file_sorter [-h] [-s {fe,md}] directory

positional arguments:
  directory             Which directory to sort

optional arguments:
  -h, --help            show this help message and exit
  -s {fe,md}, --sort-type {fe,md}
                        What to sort --> fe = file_extension || md ==
                        modification_date
```