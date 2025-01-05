# Cake 🍰 Converter

This [Streamlit app](https://cakeconversion-lcwogxrkysagthk6nazcaw.streamlit.app/) helps you scale cake recipes based on the volume of the cake. It adjusts ingredient amounts by calculating the scaling factor, ensuring the same proportions are maintained when changing the size of the cake.

## Features

- **Interactive Slider**: Choose the diameter of the cake pan (from 4 to 12 inches).
- **Scaling Factor Calculation**: Automatically calculates the scaling factor based on the ratio of the square of the diameters.
- **Ingredient Conversion**: Input your ingredients, and the app will scale them according to the selected cake diameter.
- **Ingredient Input**: Enter ingredients in a clear format (e.g., `1.5 cups butter`), and the app will parse and scale them.

## How It Works

The volume of a cake is proportional to the square of the diameter. This app uses the formula:

1. **Area of a circle** is proportional to the square of its diameter.  
   Since the height remains constant, the **volume** of the cake is directly proportional to the area of its base.  
   Therefore, to scale the recipe, we need to compute the ratio of the areas of the two cake bases.

2. **Base volume** is calculated as:  
   ```Base Volume = (Original Diameter)²```
   This represents the proportional area of the original cake.

3. **Desired volume** is calculated as:  
   ```Desired Volume = (Desired Diameter)²``` 
   This represents the proportional area of the desired cake.

4. **Scaling Factor**:  
   Scaling Factor = Desired Volume / Base Volume = (Desired Diameter)² / (Original Diameter)²  
   This ratio tells you how much to multiply each ingredient by to achieve the correct size for the new cake.

When you select a new diameter, the app scales the recipe ingredients proportionally to the new volume using the scaling factor.

## How to Use

1. **Select Base Diameter**: Use the slider to choose the original diameter (in inches).
2. **Select Desired Diameter**: Use the slider to choose the desired diameter (in inches).
3. **Input Ingredients**: In the text area, enter ingredients, one per line. For example:
4. **Click Convert**: Press the "Convert" button to see the scaled ingredients for the new cake diameter.

### Example
If your original cake has an 8-inch diameter and you want a 5-inch diameter cake:
- Base Volume = 8² = 64
- Desired Volume = 4² = 16
- Scaling Factor = 16 / 64 ≈ 0.25
  
This means you should multiply all ingredients by **0.25** to create a cake with the desired 4-inch diameter.

## Installation

To run the app locally, make sure you have Python and Streamlit installed. If not, install them via:

```bash
pip install streamlit
