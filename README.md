<div align="center">
 <img src="https://github.com/vernonthedev/conmon/assets/108737724/dbef586a-bd26-4853-9381-c1a264ecb92b" width="500px"/>

</div>
<h1 align="center">Impressive Website Connectivity Checker Documentation</h1>

## Table of Contents
<ul>
 <li>Introduction</li>
 <li>Features</li>
 <li>Installation Guide</li>
 <li>Usage</li>
  <li>Command line Arguments</li>
  <li>Checking Websites</li>
 <li>Examples</li>
 <li>Contributing</li>
 <li>License</li>
</ul>

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
    
## Introduction
Conmon is an exceptional Python terminal application that allows users to effortlessly check the connectivity of websites by sending a HEAD request to the server. It can efficiently detect if a website is online or offline and can also read URLs from a text file for batch checking.

Whether you're a system administrator, developer, or just curious about the status of your favorite websites, Conmon makes it simple to monitor website connectivity.

## Features
Conmon boasts an impressive array of features that set it apart from other website connectivity checkers:

<strong>Website Connectivity Check</strong>: Conmon can determine whether a website is online or offline by sending a HEAD request to the server. This provides quick and efficient results.

<strong>Batch URL Checking</strong>: Not just limited to checking a single website, Conmon can read a list of URLs from a text file and loop through them, displaying the status (online or offline) for each website.

<strong>Informative Output</strong>: Conmon provides clear and informative output that includes the status of each checked website. If a website is offline, it also displays an error message to help diagnose the issue.

<strong>Command-Line Interface (CLI)</strong>: Conmon offers a user-friendly CLI with options to specify URLs directly as arguments or to read them from a file, making it versatile for different use cases.

<strong>Developer-Friendly</strong>: Conmon is an open-source project, which means you can explore its code, contribute to its development, or even use it as a base for your own projects.


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
> Help Usage
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

### Command Line Arguments...
Conmon provides a user-friendly command-line interface with the following options:

```-u```, ```--urls```: Specify one or more website URLs directly as arguments.

```-f```, ```--input-file```: Read a list of URLs from a text file.

### Checking Websites
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


## Examples
Let's illustrate some real-world usage scenarios for Conmon:

<strong>Website Administrator</strong>: You can use Conmon to regularly check the status of your company's website. By scheduling it to run periodically, you can proactively detect downtime and address issues promptly.

<strong>Web Developer</strong>: Conmon is a handy tool for web developers who want to monitor the websites they are working on. It helps ensure that the sites are up and running, especially during critical development and testing phases.....

<strong>Network Administrator</strong>: In a corporate network environment, you can use Conmon to monitor various web services and check their accessibility. This can help you identify network-related problems.

## Contributing
Conmon is an open-source project, and contributions from the community are highly valued. If you'd like to contribute to its development, please check out the <a href="https://github.com/vernonthedev/conmon.git">GitHub repository</a> and follow the contribution guidelines.

## License
Conmon is released under the MIT License. You can find the detailed license information in the project's LICENSE file.

Thank you for choosing Conmon for your website connectivity checking needs! We hope you find it a valuable tool for monitoring the online presence of your favorite websites. If you have any questions or encounter issues, please don't hesitate to reach out to our community of users and developers.

Happy website monitoring! 🚀🌐
