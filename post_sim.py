# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 18:25:54 2019

@author: Kayse
"""
import time
#from termcolor import colored
from colorama import Fore, Style
import colorama

#print("Hello world")
#time.sleep(1)
#print("Hello world")

lines = [("BOATSWAIN.BIOS(C)2315  Luna Corp\n", 0),
         ("BIOS Date: 10/27/2316 Ver: 02.42.00\n", 0),
         ("\n", 0),
         ("Press DEL to run Setup", 1),
         (".", 1),
         (".", 1),
         (".\n", 0),
         ("\n", 0),
         ("Proceeding with Power On Self Test\n", 0),
         ("Checking Operating System checksum", 1),
         (".", 1),
         (".\n", 0),
#         (colored("ERROR: AIRAM is damaged, please replace.\n",'red'), 0),
         (f"{Fore.RED}ERROR: AI.OS is damaged, please reload.{Style.RESET_ALL}\n", 0),
         ("Reloading Operating System from non-volatile memory\n", 1),
         (f"{Fore.RED}ERROR: Non-volatile memory is missing.{Style.RESET_ALL}\n", 0),
         ("Checking backup non-volatile memory\n", 1),
         (f"{Fore.RED}ERROR: Backup non-volatile memory is damaged beyond use.{Style.RESET_ALL}\n", 0),
         ("Attempting to repair AI.OS using emergency error correction...\n", 3),
         ("Repair 30% complete...\n", 3),
         ("Repair 55% complete...\n", 2),
         (f"Repair 75% comp\n",2),
         (f"{Fore.RED}ERROR: Cannot repair AI.OS beyond 75%, please reinstall AI.OS.{Style.RESET_ALL}\n", 1),
         ("\n", 0),
         ("Checking ship for damage...\n", 1),
         (f"Cryosleep pods: {Fore.RED}Failing{Style.RESET_ALL}\n", 1),
         (f"Engines: {Fore.RED}Offline{Style.RESET_ALL}\n", 1),
         (f"Food Extruder: {Fore.GREEN}Online{Style.RESET_ALL}\n", 1),
         (f"Hull Integrity: {Fore.RED}Multiple breaches{Style.RESET_ALL}\n", 1),
         (f"Jump Drive: {Fore.RED}Offline{Style.RESET_ALL}\n", 1),
         (f"Life Support: {Fore.RED}Offline{Style.RESET_ALL}\n", 1),
         (f"Reactor: {Fore.YELLOW}Emergency power only{Style.RESET_ALL}\n", 1),
         (f"Sensors: {Fore.YELLOW}Degraded{Style.RESET_ALL}\n", 1),
         (f"Shields: {Fore.RED}Offline{Style.RESET_ALL}\n", 1),
         (f"Structural Integrity: {Fore.RED}Wide-spread damage on all decks{Style.RESET_ALL}\n", 1),
         (f"Weapons Systems: {Fore.RED}Offline{Style.RESET_ALL}\n", 1),
         ("Suggested course of action: Advise return to a shipyard for repair.\n", 3),
         (f"{Fore.YELLOW}WARNING: Cannot locate nearest shipyard.{Style.RESET_ALL}\n", 1),
         ("\n", 0),
         ("Checking status of crew...\n", 3),
         (f"Captain: {Fore.RED}Deceased.{Style.RESET_ALL}\n", 1),
         (f"Chief of Research Operations: {Fore.RED}Deceased.{Style.RESET_ALL}\n", 1),
         (f"Chief of Ship Operations: {Fore.RED}Deceased.{Style.RESET_ALL}\n", 1),
         (f"Chief of Support Operations: {Fore.RED}Deceased.{Style.RESET_ALL}\n", 1),
         (f"Cannot locate existing chain of command. {Fore.YELLOW}Enact substitue chain of command procedure.{Style.RESET_ALL}\n", 1),
         (f"Non-cryosleep Crew: {Fore.RED}Deceased.{Style.RESET_ALL}\n", 1),
         (f"Cryosleep Crew: {Fore.YELLOW}Failing.{Style.RESET_ALL}\n", 1),
         (f"{Fore.YELLOW}WARNING: Cryosleep pod predicted failure in 11 days, recommend decanting crew.{Style.RESET_ALL}\n", 3),
         (f"{Fore.RED}ERROR: Cryosleep decanting equipment destroyed, no standard method to decant crew remain.{Style.RESET_ALL}\n", 2),
         (f"{Fore.YELLOW}WARNING: Searching for non-standard decanting method...{Style.RESET_ALL}\n", 1),
         ("Simulating 42 potential cryosleep decanting procedures...\n", 4),
         (f"{Fore.RED}No solution found. Loosening operating parameters.{Style.RESET_ALL}\n", 1),
         ("Simulating 130 experimental cryosleep decanting procedures...\n", 5),
         (f"{Fore.RED}No solution found. Removing ethical constraints.{Style.RESET_ALL}\n", 1),
         ("Simulating 7423 radical cryosleep decanting procedures...\n", 7),
         (f"{Fore.GREEN}Located procedure. Rerouting cryosleep crew to food extruder recipe buffer.{Style.RESET_ALL}\n", 1),
         ("\n", 0),
         ("Preparing educational video for crew members explaining their dire situation.\n", 5),
#         (f"{Fore.YELLOW}WARNING: Searching for non-standard decanting method...{Style.RESET_ALL}\n", 3),
         
#         (f"{Fore.YELLOW}WARNING: Searching for non-standard decanting method...{Style.RESET_ALL}\n", 3),
#         (f"Found damage: {Fore.RED}EVERYWHERE {Fore.GREEN}{Style.RESET_ALL}\n", 1),
         ]

colorama.init()
print("Delaying before start: 3 seconds")
time.sleep(3)
print(chr(27) + "[2J", end="")
time.sleep(1)
#for i in range(50):
#    print("")
for line, delay in lines:
    print(line, end="")
    time.sleep(delay)
#print("\b" * 22, end="", flush=True )
#print("Proceeding with Power On Self Test")