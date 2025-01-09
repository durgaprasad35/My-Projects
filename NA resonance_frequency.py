import math 
def resonance_frequency_series():
     res= (1) / (2 * 3.14 * math.sqrt(inductor_value * capacitor_value))
     return res
def band_width_series():
    band_width = (resistance_value) / (2 * 3.14 * inductor_value)
    return band_width
def suspectability():
    s = resonance_frequency_series() / band_width_series()
    return s
inductor_value = int(input("Enter your inductor value: ")) * math.pow(10,-3)
capacitor_value = float(input("Enter your capacitor value : ")) * math.pow(10,-6)
resistance_value = int(input("Enter your resistance value : "))
print(resonance_frequency_series())
print(band_width_series())
print(suspectability())
def resonance_frequency_parallel():
     resonance_frequency = (1) / (2 * 3.14 * math.sqrt(inductor_value * resistance_value))
     return resonance_frequency
def band_width():
     band_width = (1) / (resistance_value * inductor_value * capacitor_value)
     return band_width
inductor_value = int(input("Enter your inductor value: ")) 
capacitor_value = float(input("Enter your capacitor value : "))
resistance_value = int(input("Enter your resistance value : "))
print(resonance_frequency_parallel())
print(band_width())
def Q_factor_inductor_res():
     Q_factor = voltage_drop_across_inductor / voltage_drop_across_resistor

     return Q_factor
#current_IL = float(input("Enter the current value : "))
frequency_value = int(input("Enter your frequency value : "))
voltage_drop_across_resistor = float(input("Enter ur voltage across the resister : "))
voltage_drop_across_inductor = (2 * 3.14 * (frequency_value )) / (voltage_drop_across_resistor)
print(Q_factor_inductor_res())

def Q_factor_capacitor_res():
     Q_factor = voltage_drop_across_capacitor / voltage_drop_across_resistor

     return Q_factor
voltage_drop_across_capacitor = (1) / (2 * 3.14 * frequency_value * voltage_drop_across_resistor)

print(Q_factor_capacitor_res())

def Q_factor():
     Q_factor1 = (1 / resistance_value1) * math.sqrt(inductor / capacitor )
     return Q_factor
inductor = float(input("Enter your inductance value : "))
capacitor = float(input("Enter your capacitance value : "))
resistance_value1 = float(input("Enter your resistance value : "))
print(Q_factor())
