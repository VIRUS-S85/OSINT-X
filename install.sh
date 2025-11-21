#!/bin/bash
clear
echo -e "\e[1;96m
   ____   _____ _____ _   _ _____   ___
  / __ \ / ____|_   _| \ | |_   _| |__ \\
 | |  | | (___   | | |  \| | | |     ) |
 | |  | |\___ \  | | | . \ | | |    / /
 | |__| |____) |_| |_| |\  |_| |_  / /_
  \____/|_____/|_____|_| \_|_____| |____|
\e[0m"
echo -e "\e[1;93m      Advanced OSINT Tool • Made by VIRUS-S85\e[0m\n"

pkg update -y && pkg upgrade -y
pkg install python git -y
pip install requests colorama pyfiglet -q

echo -e "\e[1;92m[+] Installation Complete!\e[0m"
echo -e "\e[1;96m[+] Run → cd OSINT-X && python osintx.py\e[0m"