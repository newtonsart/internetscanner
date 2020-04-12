# internetscanner
Scans every public IPV4 for the open ports you specify.

Please don't use this for illegal purposes.

## Installing
```
cd internetscanner
./install.sh
```

## Usage
### If not installed
```
sudo python3 internetscanner <PORT> <OUTPUT_FILE> <SECONDS_TIMEOUT> <MAX_THREADS>
```
### If it's installed
```
internetscanner <PORT> <OUTPUT_FILE> <SECONDS_TIMEOUT> <MAX_THREADS>
```

## Built with
* [Python 3](https://www.python.org/downloads/) - The language used.
* Python modules used: Socket, sys, os, ipaddress and threading.

## Authors
* **[[LolArt](https://github.com/LilArt)]**
