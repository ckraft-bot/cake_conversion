# Cake 🍰 Converter

This Streamlit app helps you scale cake recipes based on the diameter of the cake pan. It adjusts ingredient amounts by calculating the scaling factor, ensuring the same proportions are maintained when changing the size of the cake.

## Features

- **Interactive Slider**: Choose the diameter of the cake pan (from 4 to 12 inches).
- **Scaling Factor Calculation**: Automatically calculates the scaling factor based on the ratio of the square of the diameters.
- **Ingredient Conversion**: Input your ingredients, and the app will scale them according to the selected cake diameter.
- **Ingredient Input**: Enter ingredients in a clear format (e.g., `1.5 cups butter`), and the app will parse and scale them.

## How It Works

The volume of a cake is proportional to the square of the diameter. This app uses the formula:

```V = π * (diameter / 2)^2 * height```

The scaling factor is derived as:

```Scaling Factor = (new_diameter / base_diameter)^2```

When you select a new diameter, the app scales the recipe ingredients proportionally to the new volume using the scaling factor.

## How to Use

1. **Select Cake Diameter**: Use the slider to choose the cake pan diameter (in inches).
2. **Input Ingredients**: In the text area, enter ingredients, one per line. For example:
3. **Click Convert**: Press the "Convert" button to see the scaled ingredients for the new cake diameter.

### Example
Given the base diameter of 4 inches and a selected diameter of 6 inches, if your ingredient is 2 cups sugar, the app will calculate the new amount as:
```New_amount = 2 * (6 / 4)^2 = 4.5 cups sugar```

## Installation

To run the app locally, make sure you have Python and Streamlit installed. If not, install them via:

```bash
pip install streamlit
