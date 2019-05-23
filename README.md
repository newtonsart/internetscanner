# internetscanner
Scans every public IPV4 for the open ports you specify.

## Installing
```
mkdir /usr/share/internetscanner
chmod +x my_program.py
cp scanner.py /usr/local/bin
cp -r data /usr/share/internetscanner
echo Installation completed
```

## Usage
```
sudo python3 scanner.py <PORT> <OUTPUT_FILE> <SECONDS_TIMEOUT> <MAX_THREADS>
```

## Built with
* [Python 3](https://www.python.org/downloads/)-The language used.
* Python modules used: Socket, sys, os, ipaddress and threading.

## Authors
* **[LolArt]**(https://github.com/PurpleBooth)
