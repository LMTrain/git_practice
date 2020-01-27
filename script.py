# SAL'S SHIPPING
# Ground Shipping Calculation
def ground_shipping(weight):
  if (weight <= 2):
    return (weight * 1.50) + 20
  elif (weight > 2) and (weight <= 6):
    return (weight * 3) + 20
  elif (weight > 6) and (weight <= 10):
    return (weight * 4) + 20
  elif (weight > 10):
    return (weight * 4.75) + 20
cost = ground_shipping(4.8)
print(cost)

prem_grd_shipping = 125

# Drone Shipping Calculation
def drone_shipping(weight):
  if (weight <= 2):
    return (weight * 4.50) + 0
  elif (weight > 2) and (weight <= 6):
    return (weight * 9) + 0
  elif (weight > 6) and (weight <= 10):
    return (weight * 12) + 0
  elif (weight > 10):
    return (weight * 14.75) + 0
cost = drone_shipping(41.5)
print(cost)
 
def print_cheapest_shipping(weight):
  ground = ground_shipping(weight)
  premium = prem_grd_shipping
  drone = drone_shipping(weight)
  
  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium ground"
    cost = premium
  else:
    method = "drone"
    cost = drone
  print(
    "The cheapest option available is $%.2f with %s shipping,"
    % (cost, method)
  )
print_cheapest_shipping(4.8)
print_cheapest_shipping(41.5)
    