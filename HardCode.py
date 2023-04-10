import argparse
import os
import sys
import subprocess
from time import sleep 

def banner():
    os.system('clear')
    print("Made with <3 by nik0\n")


def check_apktool_installed():
    try:
        subprocess.run(['apktool', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        return False
    else:
        return True


def main():

    banner()
    parser = argparse.ArgumentParser(description='HardCode - v1.0')
    parser.add_argument('-f', '--file', help='APK file for decompiling', required=True)
    parser.add_argument('-s', '--string', help='Specify string for searching into decompiled APK', required=False)
    parser.add_argument('-i', '--input', help='Specify file with hardcoded strings for searching into decompiled APK', required=False)
    parser.add_argument('-o', '--output', help='Save to file', required=False)
    args = parser.parse_args()

    
    decompiled_dir = 'decompiled'
    search_dir = decompiled_dir
    decompiled_path = os.getcwd() + "/" + decompiled_dir

    try:
        print("Decompiling...")
        decompile_apk = subprocess.run(['apktool', 'd', args.file, '-o', decompiled_dir], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        os.system("clear")
        banner()
        sleep(0.5)
        print("Everything is fine, now searching...")
        sleep(1)
        print("\nDirectory saved in: %s\n\n" % decompiled_path)   
    except Exception as err:
        print(err)
        
    if args.string:
        if args.output:
            with open(args.output, 'w') as f:
                subprocess.run(['grep', '-r', args.string, search_dir], stdout=f)
                sleep(1)
                print("\nFile saved as %s" % args.output)
    else:
        subprocess.run(['grep', '-r', args.string, search_dir])

    if args.input:
        with open(args.input, 'r') as file:
            strings = file.read().splitlines()
            for string in strings:
                subprocess.run(['grep', '-r', string, search_dir])

if __name__ == '__main__':
    banner()
    if check_apktool_installed():
        print("apktool installed.")
        sleep(1)
        os.system("clear")
        main()
    else:
        print("You have to install apktool ¯\_(ツ)_/¯")
        sys.exit(1)
