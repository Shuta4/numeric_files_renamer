# Numeric files renamer
Renames files from directory from "title_ch01_asd.mp4" to "01.mp4" using text before and after number.
## Example:
before_number="ch" and after_number="_as.ds" will rename "title_ch01_as.dsd.mp4" to "01.mp4" and "ch02_as.ds.mkv" to "02.mkv".
## Usage:
### Get help: 
#### Exec: 
```commandline
python3 numeric_files_renamer.py -h
```
#### Output:
```
usage: numeric_files_renamer.py [-h] path before_number after_number

Renames files from directory from "title_ch01_asd.mp4" to "01.mp4" using text
before and after number. Example: before_number="ch" and after_number="_as.ds"
will rename "title_ch01_as.dsd.mp4" to "01.mp4" and "ch02_as.ds.mkv" to
"02.mkv".

positional arguments:
  path           Path to directory with files.
  before_number  Text of filename before number.
  after_number   Text of filename after number (without extension).

optional arguments:
  -h, --help     show this help message and exit
```
### Rename files:
#### Directory:
```
ls ~/Downloads/test/
test1s.mkv  test2s.mkv  test3s.mkv
```
#### Exec: 
```commandline
python3 numeric_files_renamer.py ~/Downloads/test/ test s
```
#### Output:
```
Changing filename from "test1s.mkv" to "1.mkv"
Changing filename from "test3s.mkv" to "3.mkv"
Changing filename from "test2s.mkv" to "2.mkv"
```
#### Result:
```
ls ~/Downloads/test/
1.mkv  2.mkv  3.mkv
```