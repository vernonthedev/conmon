<div align="center">
 <img src="https://github.com/vernonthedev/conmon/assets/108737724/dbef586a-bd26-4853-9381-c1a264ecb92b" width="500px"/>

</div>
<h1 align="center">Conmon Connection Checker</h1>

> Python Application that checks whether a website is online or offline.

### Top Level Directory Structure

    .
    ├── conmon/                        # Source files (alternatively `lib` or `app`)
      ├── __pycache__.py 
      ├── __init__.py 
      ├── __main__.py 
      ├── connection_checker.py 
      ├── cli.py 
    ├── requirements.txt              # Required installation packages
    ├── README.md                     # Documentation files (alternatively `doc`)
    ├── .gitignore                    # Virtual environment files ignored

  ## Installation Guide
  <ul>
      <li>Download the Zip File above or Clone the repository using </li>
  </ul>
  
```
git clone https://github.com/vernonthedev/conmon.git
```
<ul>
      <li>Create a virtual environment Using the following Commands in the terminal </li>
</ul>

```python
python -m venv env
```
<ul>
      <li>Activate Virtual Environment</li>
</ul>

>Windows
```python
call /env/scripts/activate.bat
```

>Linux
```python
source /bin/env/activate
```
<ul>
      <li>Install the packages required by running </li>
</ul>

```python
pip install -r requirements.txt
```

## Usage
> You can run the help command in the terminal for a more detailed help documentation.
```python
python -m conmon -h
```
#### Help Usage
```
Usage: Conmon [-h] [-u URLs [URLs ...]] [-f FILE]
Developed by vernonthedev
Check Availability of Websites.

options:
  -h, --help            show this help message and exit
  -u URLs [URLs ...], --urls URLs [URLs ...]
                        Enter one or more website URLs.
  -f FILE, --input-file FILE
                        Read URLs from a File.
```

## Examples
The ```-u``` Argument supports arguments as urls that the user would like to test connectivity to.
```python
python -m conmon -u google.com
#=================OUTPUT=====================
The Status of "google.com" is : "Online!" 👍
```
The ```-f``` Argument enables the user to add a file as input to the program that contains all the website urls that the user would require to test their connectivity
```python
python -m conmon -f U:\Developments\urlSites.txt
#===============OUTPUT=======================
The Status of "google.com" is : "Online!" 👍
The Status of "facebook.com" is : "Offline?" 👎 
 Error: "timed out"
The Status of "idontexisthere.com" is : "Offline?" 👎 
 Error: "[Errno 11001] getaddrinfo failed"
The Status of "laucher.com" is : "Online!" 👍
The Status of "microsoft.com" is : "Online!" 👍
```

