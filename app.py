import streamlit as st
import math
import measurements
import re

# Title of the app
st.title("Cake 🍰 Converter")

# Slider for selecting the diameter
diameter = st.slider(
    "Select Cake Diameter (in inches):",
    min_value=4,
    max_value=12,
    value=4,  # Default value
    step=1  # Step size
)

# Display selected diameter
st.write(f"Selected Diameter: {diameter} inches")

# Display the explanation in the sidebar
st.sidebar.subheader("Scaling Factor Explanation")
st.sidebar.write("""
The scaling factor is based on the fact that the volume of a cake is proportional to the area of its base when the height remains constant.

Volume of a cylindrical cake is given by:
V = π * r² * h
where r is the radius and h is the height.

Since r = diameter / 2, substituting gives:
V = π * (diameter / 2)² * h
   = (π * diameter² * h) / 4

This shows that the volume is proportional to the square of the diameter.

When scaling a recipe based on the new diameter, the ratio of the new volume to the original volume is proportional to the square of their diameters:

Scaling Factor = (new_diameter / base_diameter)²

Therefore, multiplying the original ingredient amounts by this scaling factor gives the adjusted amounts for the new cake size.
""")

# Define the base diameter
base_diameter = 4

# Calculate scaling factor
scaling_factor = (diameter / base_diameter) ** 2
st.write(f"Scaling Factor: {scaling_factor:.2f}")

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
