#!/bin/sh
checkroot() {

if [[ "$(id -u)" -ne 0 ]]; then
   printf "\e[1;77mPlease, run this program as root!\n\e[0m"
   exit 1
fi
}

while :
 do
    clear
                  figlet -f "poison" "Mixed Up"
                  date '+%d %B %Y %T' | toilet -f term -F border | lolcat
                  echo "\033[0;32m---------------------------------------------------------------------"
                  echo "    Mixed Up uses the worlds largest database of cocktails and drinks          "
                  echo "                                                                               "
                  echo "    Find drinks by category, name, ingredient or random....                    "
                  echo "                                                                               "
                  echo "    Random beverage party game anyone?                                         "
                  echo "\033[0;32m---------------------------------------------------------------------"
                  echo  "\033[01;33m[1]   List Drinks by Letter"
                  echo  "\033[01;33m[2]   List Drinks by Name"
                  echo  "\033[01;33m[3]   Random Drink"
                  echo  "\033[01;33m[4]   Search by Ingedient"
                  echo  "\033[01;33m[5]   Ingedient Knowledge"

                  echo "\033[01;31m[0]  Exit"
                  echo "\033[01;31m=====================================================================\033[0m"
                  echo "\033[01;37m Enter your choice [1-7]:\033[0m "

    read choice


    case $choice in

      1) cd ~/Projects/mixedUp/scripts && python3 drinkbyletter.py; echo "Press any key" | lolcat; read;;
      2) cd ~/Projects/mixedUp/scripts && python3 drinkbyname.py; echo "Press any key" | lolcat; read;;
      3) cd ~/Projects/mixedUp/scripts && python3 randomDrink.py; echo "Press any key" | lolcat; read;;
      4) cd ~/Projects/mixedUp/scripts && python3 ingredient.py; echo "Press any key" | lolcat; read;;
      5) cd ~/Projects/mixedUp/scripts && python3 ingredientData.py; echo "Press any key" | lolcat; read;;


      0) exit 0 ;;
      *) echo "Oops!!! 😜  Please select a correct choice" | lolcat;
         echo "\033[01;33m Press any key" | lolcat ; read ;;
 esac
done
