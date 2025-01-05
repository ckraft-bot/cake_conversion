import streamlit as st
import math
import measurements
import re

# Title of the app
st.title("Cake 🍰 Converter")

# Slider for selecting the diameter
original_diameter = st.slider(
    "Select original cake diameter (in inches):",
    min_value=4,
    max_value=12,
    value=8,  # Default value
    step=1  # Step size
)

# Slider for selecting the diameter
desired_diameter = st.slider(
    "Select desired cake diameter (in inches):",
    min_value=4,
    max_value=12,
    value=8,  # Default value
    step=1  # Step size
)

# Display selected diameter
st.write(f"Selected original diameter: {original_diameter} inches")
st.write(f"Selected desired diameter: {desired_diameter} inches")

# Display the explanation in the sidebar
st.sidebar.subheader("Scaling Factor Explanation")
st.sidebar.write("""
### Explanation of the Scaling Factor:

When scaling a cake recipe, we assume the **height** of the cake remains constant, so the scaling is determined by the ratio of the **areas of the circular bases** of the two cakes.

---

#### Key Concepts:

1. **Area of a circle** is proportional to the square of its diameter.  
   Since the height remains constant, the **volume** of the cake is directly proportional to the area of its base.  
   Therefore, to scale the recipe, we need to compute the ratio of the areas of the two cake bases.

2. **Base volume** is calculated as:  
   Base Volume = (Original Diameter)²  
   This represents the proportional area of the original cake.

3. **Desired volume** is calculated as:  
   Desired Volume = (Desired Diameter)²  
   This represents the proportional area of the desired cake.

4. **Scaling Factor**:  
   Scaling Factor = Desired Volume / Base Volume = (Desired Diameter)² / (Original Diameter)²  
   This ratio tells you how much to multiply each ingredient by to achieve the correct size for the new cake.

---

#### Example:

- If your original cake has an **8-inch diameter** and you want a **5-inch diameter** cake:  
  Base Volume = 8² = 64  
  Desired Volume = 4² = 16  
  Scaling Factor = 16 / 64 ≈ 0.25 

This means you should multiply **all ingredients by 0.25** to create a cake with the desired 5-inch diameter.

""")

# Define the base diameter
base_diameter = original_diameter

# Calculate scaling factor
base_volume = original_diameter ** 2
desired_volume = desired_diameter ** 2 
scaling_factor = desired_volume / base_volume
st.write(f"Scaling factor from {base_diameter} inches to {desired_diameter} inches: {scaling_factor:.2f}")

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
