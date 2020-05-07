import sys
Import binascii
Import re
from subprocess import Popen 
from subprocess import PIPE

#### this script should automate the bruteforcing of a WEP key from a cap file WEP-Advanced.cap
#### then it will atempt to bruteforce with a given wordlist and spit out the found password


f = open(sys.argv[1], 'r')

for line in f:
        wepKey = re.sub(r'\W+', '', line)
        if len(wepKey) != 5 :
                continue
                
        hexKey = binascii.hexlify(wepKey)
        print "Trying with WEP Key: " +wepKey + " Hex: " + hexKey
        p = Popen(['/usr/bin/airdecap-ng', '-w', hexKey, 'WEP-Advanced.cap'], stdout=PIPE)
        output = p.stdout.read()
        finalResult = output.split('\n')[4]
        
        if finalResult.find('1') != -1 :
                print "Key was Found: "  + wepKey
                sys.exit(0)
                
print ("Try a new wordlist, the key wasnt found")
