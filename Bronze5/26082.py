r_price,r_ability,price = map(int, input().split())
r_abilityPrice = r_ability / r_price
abilityPrice = r_abilityPrice*3
ability = abilityPrice * price
print(int(ability))