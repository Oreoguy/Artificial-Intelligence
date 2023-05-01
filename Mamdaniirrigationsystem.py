# Importing required libraries
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Defining fuzzy domains for each factor
soil_moisture = np.arange(0, 1.01, 0.01)
soil_type = np.arange(0, 11, 1)
crop_type = np.arange(0, 11, 1)
weather_type = np.arange(0, 11, 1)

# Defining membership functions for each factor and domain
# Soil Moisture
moisture_dry = fuzz.trimf(soil_moisture, [0, 0, 40])
moisture_moderate = fuzz.trimf(soil_moisture, [30, 60, 100])
moisture_wet = fuzz.trimf(soil_moisture, [60, 80, 100])

# Soil Type
soil_sandy = fuzz.trimf(soil_type, [0, 0, 5])
soil_clayey = fuzz.trimf(soil_type, [0, 5, 10])
soil_loamy = fuzz.trimf(soil_type, [5, 10, 10])

# Crop Type
crop_wheat = fuzz.trimf(crop_type, [0, 0, 5])
crop_maize = fuzz.trimf(crop_type, [0, 5, 10])
crop_rice = fuzz.trimf(crop_type, [5, 10, 10])

# Weather Type
weather_cold = fuzz.trimf(weather_type, [0, 0, 5])
weather_warm = fuzz.trimf(weather_type, [0, 5, 10])

# Plotting membership functions for each factor and domain
fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4, figsize=(8, 8))

ax0.plot(soil_moisture, moisture_dry, 'b', linewidth=1.5, label='Dry')
ax0.plot(soil_moisture, moisture_moderate, 'g', linewidth=1.5, label='Moderate')
ax0.plot(soil_moisture, moisture_wet, 'r', linewidth=1.5, label='Wet')
ax0.set_title('Soil Moisture')
ax0.legend()

ax1.plot(soil_type, soil_sandy, 'b', linewidth=1.5, label='Sandy')
ax1.plot(soil_type, soil_clayey, 'g', linewidth=1.5, label='Clayey')
ax1.plot(soil_type, soil_loamy, 'r', linewidth=1.5, label='Loamy')
ax1.set_title('Soil Type')
ax1.legend()

ax2.plot(crop_type, crop_wheat, 'b', linewidth=1.5, label='Wheat')
ax2.plot(crop_type, crop_maize, 'g', linewidth=1.5, label='Maize')
ax2.plot(crop_type, crop_rice, 'r', linewidth=1.5, label='Rice')
ax2.set_title('Crop Type')
ax2.legend()

ax3.plot(weather_type, weather_cold, 'b', linewidth=1.5, label='Cold')
ax3.plot(weather_type, weather_warm, 'g', linewidth=1.5, label='Warm')
ax3.set_title('Weather Type')
ax3.legend()

# Defining fuzzy rules for controlling the pump
rule1 = (np.fmax(moisture_dry, np.fmax(soil_sandy, np.fmax(crop_wheat, weather_cold))))
rule2 = (np.fmax(moisture_wet, np.fmax(soil_loamy, np.fmax(crop_rice, weather_warm))))
rule3 = moisture_moderate
rules = [rule1, rule2, rule3]

# Defining the Mamdani inference system
defuzzy_pump = fuzz.defuzz(soil_moisture, np.fmax(moisture_dry, np.fmax(moisture_wet, moisture_moderate)))
pump_activation_dry = fuzz.interp_membership(soil_moisture, moisture_dry, defuzzy_pump)
pump_activation_wet = fuzz.interp_membership(soil_moisture, moisture_wet, defuzzy_pump)
pump_activation_moderate = fuzz.interp_membership(soil_moisture, moisture_moderate, defuzzy_pump)

activation_rules = np.fmax(np.fmin(pump_activation_dry, rule1), np.fmax(np.fmin(pump_activation_wet, rule2), np.fmin(pump_activation_moderate, rule3)))

# Defuzzifying the output
pump_power = fuzz.defuzz(soil_moisture, activation_rules, 'centroid')
pump_power_activation = fuzz.interp_membership(soil_moisture, activation_rules, pump_power)

# Plotting the output
fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.plot(soil_moisture, moisture_dry, 'b', linewidth=0.5, linestyle='--', )
ax0.plot(soil_moisture, moisture_moderate, 'g', linewidth=0.5, linestyle='--')
ax0.plot(soil_moisture, moisture_wet, 'r', linewidth=0.5, linestyle='--')
ax0.fill_between(soil_moisture, np.zeros_like(soil_moisture), activation_rules, facecolor='Orange', alpha=0.7)
ax0.plot([pump_power, pump_power], [0, pump_power_activation], 'k', linewidth=1.5, alpha=0.9)
ax0.set_title('Output Membership Activity')

# Turning off top and right axis lines
for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()
