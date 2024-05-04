import os, platform, time, sys
os.system("clear")
def lo(word):
    heron = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;91m■■\x1b[0m□□□□□□□□]", "[\x1b[1;91m■■■\x1b[0m□□□□□□□]", "[\x1b[1;92m■■■■\x1b[0m□□□□□□]", "[\x1b[1;91m■■■■■\x1b[0m□□□□□]", "[\x1b[1;92m■■■■■■\x1b[0m□□□□]", "[\x1b[1;92m■■■■■■■\x1b[0m□□□]", "[\x1b[1;92m■■■■■■■■\x1b[0m□□]", "[\x1b[1;92m■■■■■■■■■\x1b[0m□]", "[\x1b[1;92m■■■■■■■■■■\x1b[0m]"]
    for i in range(3):
        for x in range(len(heron)):
            sys.stdout.write(('\r{}{}').format(str(word), heron[x]))
            time.sleep(0.1)
            sys.stdout.flush()
lo("\033[91;1m [\033[97;1m•\033[91;1m] \033[97;1mLoading System Please Wait...!")
time.sleep(1)
#os.system("clear")
#os.system('pkg install espeak -y')
os.system("clear")
print("\033[91;1m [\033[97;1m•\033[91;1m] \033[97;1mJoin Whatsapp Group...!")
time.sleep(1)
os.system("clear")
os.system("xdg-open ")
os.system("clear")
print("\033[91;1m [\033[97;1m•\033[91;1m] \033[97;1mChecking For Update...!")
time.sleep(1)
os.system("clear")
os.system('git pull --quiet 2>/dev/null')
habibxd = platform.architecture()[0]
if habibxd == '64bit':
    print("\033[91;1m [\033[97;1m•\033[91;1m] \033[97;1mYour Device is 64bit")
    import P64
elif habibxd == '32bit':
    print("\033[91;1m [\033[97;1m•\033[91;1m] \033[97;1mYour Devive is 32Bit")
    os.system("clear");exit("\033[91;1m [\033[97;1m•\033[91;1m] \033[91;1m32Bit Device Not Supported")
