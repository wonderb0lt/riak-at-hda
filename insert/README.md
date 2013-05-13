# Insert Script
## Installation

To install, follow these steps:

1. Obtain Python 2.7 (Should be included in most Linux Distributions)
2. Obtain pip (Is in Debian/Ubuntu as "python-pip", elsewise download & install from [PyPi](https://pypi.python.org/pypi/pip))
3. Install prerequisities for the insert script (pip install -r insert/requirements.txt)

...you should now be able to run the script!

## Usage

Review host and port in conf.py (and, if nessecary, change the bucket name)

After that you can run the script with the following commands:

`./insert.py data/006MME.json` to insert a specific file
`./insert.py data/file1.json data/file2.json ...` to insert multiple files at once
`./insert.py --generate` to generate a number of files. Set the `number_of_entries` in the conf.py to your needs!
