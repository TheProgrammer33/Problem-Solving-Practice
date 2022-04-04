def knapsack(weight_cap, weights, values):
    everySituation = []
    for i in range(1, pow(2, len(weights))):
        situation = str(bin(i))[2:]
        everySituation.append("0"*(len(weights)-len(situation)) + situation)
    
    bestValue = 0
    for situation in everySituation:
        currentWeight = 0
        currentValue = 0
        for item in range(len(situation)):
            if (int(situation[item])):
                currentWeight += weights[item]
                currentValue += values[item]
                if (currentWeight > weight_cap):
                    break            
        if (currentWeight > weight_cap):
            continue

        if currentValue > bestValue:
            bestValue = currentValue

    return bestValue

weight_cap = 50
weights = [31, 10, 20, 19, 4, 3, 6]
values = [70, 20, 39, 37, 7, 5, 10]
print(knapsack(weight_cap, weights, values))
