import random
import time

# Play through a game of blackjack and if dealer goes over 21 then everyone wins

def deal(cardNumber):
    card = random.randint(1, 11)
    if card == 11:
        if cardNumber == 0:
            card = 1
        else:
            card = 11
    return card

# Checks if there are CPUs, returns false if there is none
def cpuCheck(cpus):
    if cpus == 0:
        return False
    elif cpus != 0:
        tempCpuBalances = []
        for i in range(cpus):
            tempCpuBalances.append(random.randint(50, 250))
        return tempCpuBalances
    else:
        return False

# Checks if there are players, returns false if there is none
def playerCheck(players):
    if players == 0:
        return False
    elif players != 0:
        tempPlayerBalances = []
        for i in range(players):
            tempPlayerBalances.append(random.randint(50, 250))
        return tempPlayerBalances
    else:
        return False

def gameplay(cpus, players, games):
    print(f"Game {games}")
    playerCardCount = []
    if players != False:
        for i in range(len(players)):
            cardCount = []
            # Deals first 2 cards
            cardCount.append(deal(1))
            cardCount.append(deal(0))
            tempFlag = False

            while tempFlag == False:
                playerInput = input(f"Player {i+1}. Balance {players[i]}. Your hand: {cardCount} ({sum(cardCount)}). Hit or stand?: ").lower()
                if playerInput == "hit":
                    cardCount.append(deal(0))
                elif playerInput == "stand":
                    playerCardCount.append(sum(cardCount))
                    tempFlag = True
                if sum(cardCount) > 21:
                    print(f"Player {i+1} busted! Going onto the next player/cpu...")
                    playerCardCount.append(sum(cardCount))
                    tempFlag = True
                elif sum(cardCount) == 21:
                    print(f"Player {i+1} hit blackjack!! {sum(cardCount)} Going onto the next player/cpu...")
                    playerCardCount.append(sum(cardCount))
                    tempFlag = True
    else:
        playerCardCount = False

    cpuCardCount = []
    if cpus != False:    
        for i in range(len(cpus)):
            if cpus[i] == False:
                cpuCardCount.append(False)
                continue
            else:
                cardCount = []
                # Deals first 2 cards
                cardCount.append(deal(1))
                cardCount.append(deal(0))
                tempFlag = False

                while tempFlag == False:
                    if sum(cardCount) <= 17:
                        print(f"Cpu {i+1} with cards {cardCount} ({sum(cardCount)}) hits.")
                        cardCount.append(deal(0))
                    elif sum(cardCount) > 17 and sum(cardCount) < 21:
                        print(f"Cpu {i+1} stands with cards {cardCount} ({sum(cardCount)}).")
                        cpuCardCount.append(sum(cardCount))
                        tempFlag = True
                    elif sum(cardCount) == 21:
                        print(f"Cpu {i+1} stands with blackjack! {cardCount} ({sum(cardCount)})")
                        cpuCardCount.append(sum(cardCount))
                        tempFlag = True
                    elif sum(cardCount) > 21:
                        print(f"Cpu {i+1} busted. {cardCount} ({sum(cardCount)})")
                        cpuCardCount.append(sum(cardCount))
                        tempFlag = True
    else:
        cpuCardCount = False

    dealerCardCount = 0
    cardCount = []
    cardCount.append(deal(1))
    cardCount.append(deal(0))
    tempFlag = False

    while tempFlag == False:
        if sum(cardCount) <= 17:
            print(f"Dealer with cards {cardCount} {sum(cardCount)} hits.")
            cardCount.append(deal(0))
        if sum(cardCount) > 17 and sum(cardCount) < 21:
            print(f"Dealer stands with cards {cardCount} ({sum(cardCount)}).")
            dealerCardCount = sum(cardCount)
            tempFlag = True
        elif sum(cardCount) == 21:
            print(f"Dealer stands with blackjack! {cardCount}")
            dealerCardCount = sum(cardCount)
            tempFlag = True
        elif sum(cardCount) > 21:
            print(f"Dealer busted. {cardCount} ({sum(cardCount)})")
            dealerCardCount = sum(cardCount)
            tempFlag = True

    return [playerCardCount, cpuCardCount, dealerCardCount]

def gaming(lists, bettingAmounts, cpuBalance, playerBalance):
    # LISTS = [[playerFinalCard], [cpuFinalCard], dealerFinalCard], BETTINGAMOUNTS = [[playerBetAmount], [cpuBetAmount]], CPUBALANCE = [cpuBalance], PLAYERBALANCE = [playerBalance]
    # If dealer busts
    if lists[2] > 21:
        if cpuBalance != False:
            for i in range(len(cpuBalance)):
                if cpuBalance[i] == False:
                    continue
                elif lists[1][i] <= 21:
                    cpuBalance[i] += bettingAmounts[1][i]
                    print(f"Cpu {i+1} wins {bettingAmounts[1][i]}. New balance: {cpuBalance[i]}")
                else:
                    cpuBalance[i] -= bettingAmounts[1][i]
                    print(f"Cpu {i+1} loses {bettingAmounts[1][i]}. New balance: {cpuBalance[i]}")
        if playerBalance != False:
            for i in range(len(playerBalance)):
                if playerBalance[i] == False:
                    continue
                elif lists[0][i] <= 21:
                    playerBalance[i] += bettingAmounts[0][i]
                    print(f"Player {i+1} wins {bettingAmounts[0][i]}. New balance: {playerBalance[i]}")
                else:
                    playerBalance[i] -= bettingAmounts[0][i]
                    print(f"Player {i+1} loses {bettingAmounts[0][i]}. New balance: {playerBalance[i]}")
    # If dealer hits 21
    elif lists[2] == 21:
        if cpuBalance != False:
            for i in range(len(cpuBalance)):
                if cpuBalance[i] == False:
                    continue
                elif lists[1][i] != lists[2]:
                    cpuBalance[i] -= bettingAmounts[1][i]
                    print(f"Cpu {i+1} loses {bettingAmounts[1][i]}. New balance: {cpuBalance[i]}")
        if playerBalance != False:
            for i in range(len(playerBalance)):
                if playerBalance[i] == False:
                    continue
                elif lists[0][i] != lists[2]:
                    playerBalance[i] -= bettingAmounts[0][i]
                    print(f"Player {i+1} loses {bettingAmounts[0][i]}. New balance: {playerBalance[i]}")
    # If dealer stays in range
    elif lists[2] < 21:
        if cpuBalance != False:
            for i in range(len(cpuBalance)):
                if cpuBalance[i] == False:
                    continue
                elif lists[1][i] > lists[2] and lists[1][i] <= 21:
                    cpuBalance[i] += bettingAmounts[1][i]
                    print(f"Cpu {i+1} wins {bettingAmounts[1][i]}. New balance: {cpuBalance[i]}")
                elif lists[1][i] == lists[2]:
                    # Nothing happens
                    print(f"Cpu {i+1} pushes. No changes. New balance: {cpuBalance[i]}")
                elif lists[1][i] < lists[2] or lists[1][i] > 21:
                    cpuBalance[i] -= bettingAmounts[1][i]
                    print(f"Cpu {i+1} loses {bettingAmounts[1][i]}. New balance: {cpuBalance[i]}")
        if playerBalance != False:
            for i in range(len(playerBalance)):
                if playerBalance[i] == False:
                    continue
                elif lists[0][i] > lists[2] and lists[1][i] > 21:
                    playerBalance[i] += bettingAmounts[0][i]
                    print(f"Player {i+1} wins {bettingAmounts[0][i]}. New balance: {playerBalance[i]}")
                elif lists[0][i] == lists[2]:
                    print(f"Player {i+1} pushes. No changes. New balance: {playerBalance[i]}")
                elif lists[0][i] < lists[2] or lists[0][i] > 21:
                    playerBalance[i] -= bettingAmounts[0][i]
                    print(f"Player {i+1} loses {bettingAmounts[0][i]}. New balance: {playerBalance[i]}")

    return [cpuBalance, playerBalance]

def theEliminator(list, cpuBalances, playerBalances):
    # List = [[Cpu balances], [player balance]]
    if playerBalances != False:
        for i in range(len(playerBalances)):
            if type(list[1][i]) != bool and list[1][i] <= 0:
                print(f"We are sorry player {i+1}, you cannot participate anymore.")
                list[1][i] = False
    if cpuBalances != False:
        for i in range(len(cpuBalances)):
            if type(list[0][i]) != bool and list[0][i] <= 0:
                print(f"We are sorry cpu {i+1}, you cannot participate anymore.")
                list[0][i] = False

    return list



def betting(cpuBalance, playerBalance):
    playerBetAmount = []
    cpuBetAmount = []
    if playerBalance != False:
        for i in range(len(playerBalance)):
            tempFlag = False

            while tempFlag == False:
                betAmount = int(input(f"Player {i+1}: How much would you like to bet? You currently have {playerBalance[i]}: "))
                if betAmount > playerBalance[i]:
                    print("Your bet amount is more than your balance. Please bet less than your balance.")
                else:
                    playerBetAmount.append(betAmount)
                    tempFlag = True

    if cpuBalance != False:
        for i in range(len(cpuBalance)):
            if cpuBalance[i] == False:
                betAmount = False
                cpuBetAmount.append(betAmount)
            else:
                betAmount = random.randint(0, cpuBalance[i])
                cpuBetAmount.append(betAmount)

    return [playerBetAmount, cpuBetAmount]

def cleanUp(cpuBalance, playerBalance):
    cpuTempFlag = True
    playerTempFlag = True

    if cpuBalance != False:
        for i in range(len(cpuBalance)):
            if cpuBalance[i] != False:
                cpuTempFlag = False
                break

    if playerBalance != False:
        for i in range(len(playerBalance)):
            if playerBalance[i] != False:
                playerTempFlag = False
                break

    if cpuTempFlag == True:
        cpuBalance = False
    if playerTempFlag == True:
        playerBalance = False

    return [cpuBalance, playerBalance]

def main():
    # Asks for CPU and player count
    cpuCount = int(input("How many cpus would you like to play?: "))
    playerCount = int(input("How many players is there to play?: "))

    # Goes through and checks if there are CPUs and players and if so, gives them random values
    cpuBalances = cpuCheck(cpuCount)
    playerBalances = playerCheck(playerCount)
    games = 0

    while cpuBalances != False or playerBalances != False:
        bettingAmounts = betting(cpuBalances, playerBalances)
        lists = gameplay(cpuBalances, playerBalances, games)
        FixedValue = gaming(lists, bettingAmounts, cpuBalances, playerBalances)
        returnedList = theEliminator(FixedValue, cpuBalances, playerBalances)
        fixedList = cleanUp(returnedList[0], returnedList[1])
        cpuBalances = fixedList[0]
        playerBalances = fixedList[1]
        games += 1
        time.sleep(0.1)

main()
