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

