x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(f"x is y: {x is y}")      # False → x aur y same data rakhte hain, par alag memory objects hain
print(f"x is z: {x is z}")      # True → x aur z ek hi memory location share karte hain
print(f"x is not y: {x is not y}")  # True → x aur y alag objects hain
print(f"x is not z: {x is not z}")  # False → x aur z same object hain