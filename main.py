#Main program
from subprocess import call
import json

config = {"Loot_System": [],"Negative_Bids": [], "Decay": [], "Percent_Decay": [], "Freq_Decay_M": [], "DKP_per_30m": [], "Open_or_Closed": [], "DKP_Cap": [] }
#Pick your loot system
lootsys = input("Choose your loot system: Standard, Fixed, SK, Nikarma, LootC, Zerosum. ")
config["Loot_System"].append(lootsys)
if lootsys == 'Standard':
    neg = input('Do you want to allow negative bids?')
    if neg == "Y":
        config["Negative_Bids"].append(neg)
    elif neg == "N":
        pass
    decay = input("How about decay? Y or N. ")
    config["Decay"].append(decay)
    if decay == 'Y':
        pctdec = input("What percent decay would you like?")
        config["Percent_Decay"].append(pctdec)
        timedec = input("How often would you like decay to occur? In months. ")
        config["Freq_Decay_M"].append(timedec)
    elif decay == 'N':
        pass
    amtdkp = input("How much dkp per 30 minutes would you like members to accrue? ")
    if not amtdkp.isdigit:
        print("You need to enter a number.")
    elif amtdkp.isdigit:
        config["DKP_per_30m"].append(amtdkp)
    ocbids = input("Would you like your bids to be open or closed? State O or C. ")
    config["Open_or_Closed"].append(ocbids)
    dkpcap = input("Do you want a dkp cap? Y or N. ")
    if dkpcap == "Y":
        amtdkpcap = input("What do you want your DKP cap to be?")
        if not amtdkpcap.isdigit:
            print("You need to choose a number.")
        elif amtdkpcap.isdigit:
            config["DKP_Cap"].append(amtdkpcap)
            pass
    elif dkpcap == 'N':
        pass
print(config)

with open('lootsysconfig.json', 'w') as outfile:
    json.dump(config, outfile)





    #call(['python', 'Standarddkp.py'])
#Pick the parameters for it
#Run the files










