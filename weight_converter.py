weight = float(input("Weight: "))

choice = input("(K)g or (L)bs: ")

if choice.upper() == 'K':
    print(f"Weight in Lbs: {weight / 0.45}")
elif choice.upper() == 'L':
    print(f"Weight in Kg: {weight * 0.45}")
else:
    print("please enter a valid choice")
