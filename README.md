# mac2vendor
Mac address to Vendor information

# Usage
m2v mac_address

eg : `m2v XX:XX:XX:XX:XX:XX`

# Requirement
1. python2
2. Internet connection

# Note
This script uses the API from [macvendorlookup.com](http://www.macvendorlookup.com/mac-address-api)   
Symlink it to /usr/bin to be able to use it anywhere as a linux command.
```sh
sudo chmod +x m2v
sudo ln -s ~/Downloads/mac2vendor/m2v /usr/bin/m2v
```
