import streamlit as st
import math
import measurements
import re

# Title of the app
st.title("Cake 🍰 Converter")

# Slider for selecting the diameter
original_diameter = st.slider(
    "Select Original Cake Diameter (in inches):",
    min_value=4,
    max_value=12,
    value=8,  # Default value
    step=1  # Step size
)

# Slider for selecting the diameter
desired_diameter = st.slider(
    "Select Desired Cake Diameter (in inches):",
    min_value=4,
    max_value=12,
    value=8,  # Default value
    step=1  # Step size
)

# Display selected diameter
st.write(f"Selected Original Diameter: {original_diameter} inches")
st.write(f"Selected Desired Diameter: {desired_diameter} inches")

# Display the explanation in the sidebar
st.sidebar.subheader("Scaling Factor Explanation")
st.sidebar.write("""
The scaling factor is based on the fact that the volume of a cake is proportional to the area of its base when the height remains constant.
scaling factor = desired diameter/original diameter.
""")

# Define the base diameter
# Define the base diameter (use original_diameter directly)
base_diameter = original_diameter

# Calculate scaling factor
# scaling_factor = (desired_diameter / base_diameter) ** 2
base_volume = original_diameter ** 2
desired_volume = desired_diameter ** 2 
scaling_factor = desired_volume/ base_volume
st.write(f"Scaling Factor from the {base_diameter} inches to {desired_diameter} inches: {scaling_factor:.2f}")

# Function to parse the ingredients input
def parse_ingredient_line(line):
    # Match with a pattern: number (optional) + space + unit + space + ingredient name
    match = re.match(r"(\d+\.?\d*)\s*(\w+)\s*(.+)", line)
    if match:
        amount = match.group(1).strip()
        unit = match.group(2).strip()
        name = match.group(3).strip()
        return (name, amount, unit)
    else:
        return None

# Streamlit UI for inputting ingredients
st.subheader("Input Your Ingredients")
ingredients_input = st.text_area(
    "Enter ingredients (one per line, e.g., '1.5 cups butter'):",
    placeholder="e.g. 1.5 cups butter\n8 oz cream cheese\n6 large eggs"
)

if st.button("Convert"):
    # Parse ingredients input
    ingredients = []
    if ingredients_input:
        for line in ingredients_input.strip().split("\n"):
            ingredient = parse_ingredient_line(line)
            if ingredient:
                name, amount, unit = ingredient
                ingredients.append((name, amount, unit))
            else:
                st.warning(f"Could not parse line: {line}")

    # Display the list of ingredients
    if ingredients:
        st.subheader("Your Ingredients")
        for name, amount, unit in ingredients:
            st.write(f"{name}: {amount} {unit}")

    # Scale ingredients based on the selected diameter
    if ingredients:
        st.subheader("Scaled Ingredients")
        for name, amount, unit in ingredients:
            try:
                numeric_amount = eval(amount.replace(" ", "+"))  # Handle mixed fractions like '1 1/2'
                scaled_amount = numeric_amount * scaling_factor
                st.write(f"{name}: {scaled_amount:.2f} {unit}")
            except Exception as e:
                st.error(f"Could not scale ingredient '{name}': {e}")
