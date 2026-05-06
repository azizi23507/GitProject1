import numpy as np
import matplotlib.pyplot as plt


# Function to plot lines with different slopes
def plot_slope_comparison():
    """Visualize how different m values affect line steepness"""
    x = np.linspace(-5, 5, 100)

    # Different slopes (m values) with same intercept b=0
    slopes = [0.2, 1, 3, -0.5, -2]
    labels = ['m=0.2 (gentle +)', 'm=1 (45° +)', 'm=3 (steep +)',
              'm=-0.5 (gentle -)', 'm=-2 (steep -)']
    colors = ['lightblue', 'blue', 'darkblue', 'lightcoral', 'red']

    plt.figure(figsize=(10, 8))

    # Plot each line
    for m, label, color in zip(slopes, labels, colors):
        y = m * x  # b = 0
        plt.plot(x, y, label=label, color=color, linewidth=2)
        # Add slope annotation
        plt.text(4, m * 4, f'slope={m}', fontsize=10,
                 bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

    # Add grid and labels
    plt.axhline(y=0, color='black', linewidth=0.5, alpha=0.5)
    plt.axvline(x=0, color='black', linewidth=0.5, alpha=0.5)
    plt.grid(True, alpha=0.3)
    plt.title('How Slope (m) Affects Line Steepness and Direction', fontsize=14, fontweight='bold')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.axis('equal')
    plt.xlim(-5, 5)
    plt.ylim(-10, 10)
    plt.show()


# Function to plot lines with same slope but different intercepts
def plot_intercept_comparison():
    """Visualize how different b values shift parallel lines"""
    x = np.linspace(-5, 5, 100)
    m = 2  # Fixed slope

    # Different intercepts
    intercepts = [-4, -2, 0, 2, 4]
    labels = [f'b={b}' for b in intercepts]
    colors = plt.cm.viridis(np.linspace(0, 1, len(intercepts)))

    plt.figure(figsize=(10, 8))

    # Plot each line
    for b, label, color in zip(intercepts, labels, colors):
        y = m * x + b
        plt.plot(x, y, label=label, color=color, linewidth=2)
        # Mark y-intercept point
        plt.plot(0, b, 'o', color=color, markersize=8)
        plt.text(0.3, b, f'(0,{b})', fontsize=9, verticalalignment='center')

    # Add visual guide
    for b in intercepts:
        plt.axhline(y=b, xmin=0, xmax=0.05, color='gray', linestyle=':', alpha=0.5)

    plt.axhline(y=0, color='black', linewidth=0.5, alpha=0.5)
    plt.axvline(x=0, color='black', linewidth=0.5, alpha=0.5)
    plt.grid(True, alpha=0.3)
    plt.title('How Intercept (b) Shifts Parallel Lines (Same Slope m=2)',
              fontsize=14, fontweight='bold')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(title='y = 2x + b')
    plt.xlim(-5, 5)
    plt.ylim(-10, 10)
    plt.show()


# Function to demonstrate extreme cases
def plot_extreme_cases():
    """Show horizontal, vertical, and very steep lines"""
    x = np.linspace(-5, 5, 100)

    plt.figure(figsize=(10, 8))

    # 1. Horizontal line (m=0)
    plt.axhline(y=3, color='green', linewidth=3, label='Horizontal: y=3 (m=0)')
    plt.text(-4.5, 3.2, 'm=0 (completely flat)', fontsize=10, color='green')

    # 2. Steep positive slope
    plt.plot(x, 5 * x, 'red', linewidth=2, label='Very steep: y=5x (m=5)')
    plt.text(2, 2, 'm=5\nFor 1 unit right,\n5 units up', fontsize=9, color='red',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

    # 3. Gentle positive slope
    plt.plot(x, 0.2 * x, 'blue', linewidth=2, label='Gentle: y=0.2x (m=0.2)')
    plt.text(4, 1, 'm=0.2\nFor 1 unit right,\n0.2 units up', fontsize=9, color='blue',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

    # 4. Vertical line (not a function, special case)
    plt.axvline(x=2, color='purple', linewidth=3, linestyle='--', label='Vertical: x=2 (m=∞)')
    plt.text(2.1, 8, 'Vertical line\nSlope undefined\nm = infinity', fontsize=10, color='purple')

    # Add slope triangles to illustrate
    # For steep line
    plt.arrow(1, 5, 0, 5, head_width=0.1, head_length=0.5, fc='red', ec='red', alpha=0.5)
    plt.arrow(1, 5, 1, 0, head_width=0.3, head_length=0.1, fc='red', ec='red', alpha=0.5)

    # For gentle line
    plt.arrow(1, 0.2, 0, 0.2, head_width=0.1, head_length=0.05, fc='blue', ec='blue', alpha=0.5)
    plt.arrow(1, 0.2, 1, 0, head_width=0.3, head_length=0.1, fc='blue', ec='blue', alpha=0.5)

    plt.axhline(y=0, color='black', linewidth=0.5, alpha=0.5)
    plt.axvline(x=0, color='black', linewidth=0.5, alpha=0.5)
    plt.grid(True, alpha=0.3)
    plt.title('Extreme Cases of Slope (m)', fontsize=14, fontweight='bold')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='upper left')
    plt.xlim(-5, 5)
    plt.ylim(-10, 10)
    plt.show()


# Function to show how |m| relates to angle
def plot_slope_angles():
    """Show lines with different slopes and their approximate angles"""
    x = np.linspace(0, 4, 100)

    slopes = [0, 0.5, 1, 2, 5]
    angles = ['0°', '≈27°', '45°', '≈63°', '≈79°']
    colors = plt.cm.plasma(np.linspace(0, 1, len(slopes)))

    plt.figure(figsize=(10, 8))

    for m, angle, color in zip(slopes, angles, colors):
        y = m * x
        plt.plot(x, y, color=color, linewidth=3, label=f'm={m}, angle={angle}')

        # Add angle indicator at x=2
        if m > 0:
            y_pos = m * 2
            plt.text(2.1, y_pos, f'{angle}', fontsize=9, color=color,
                     bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.8))

    plt.grid(True, alpha=0.3)
    plt.title('Slope (m) and Corresponding Angle with x-axis', fontsize=14, fontweight='bold')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.axhline(y=0, color='black', linewidth=0.5)
    plt.axvline(x=0, color='black', linewidth=0.5)
    plt.xlim(-1, 5)
    plt.ylim(-1, 10)
    plt.show()


# Interactive function to explore m and b
def interactive_line_explorer(m=1, b=0):
    """Interactive plot to see effect of changing m and b"""
    x = np.linspace(-10, 10, 400)
    y = m * x + b

    plt.figure(figsize=(12, 6))

    # Main plot
    plt.subplot(1, 2, 1)
    plt.plot(x, y, 'b-', linewidth=3, label=f'y = {m}x + {b}')
    plt.plot(0, b, 'ro', markersize=10, label=f'y-intercept (0,{b})')

    # Add slope triangle
    if m != 0:
        triangle_x = [1, 1, 2]
        triangle_y = [b + m * 1, b + m * 1, b + m * 1]
        plt.fill(triangle_x, triangle_y, 'green', alpha=0.3)
        plt.text(1.5, b + m * 1.5, f'Slope = {m}\n(rise/run)',
                 fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

    plt.axhline(y=0, color='black', linewidth=0.5, alpha=0.5)
    plt.axvline(x=0, color='black', linewidth=0.5, alpha=0.5)
    plt.grid(True, alpha=0.3)
    plt.title(f'Line: y = {m}x + {b}', fontsize=14, fontweight='bold')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    # Information panel
    plt.subplot(1, 2, 2)
    plt.axis('off')
    info_text = f"""
    LINE PROPERTIES:

    Slope (m) = {m}

    • Direction: {'Positive (uphill)' if m > 0 else 'Negative (downhill)' if m < 0 else 'Horizontal'}
    • Steepness: {'Very steep' if abs(m) > 3 else 'Steep' if abs(m) > 1 else 'Gentle' if abs(m) > 0 else 'Flat'}
    • For each 1 unit right → {abs(m)} units {'up' if m > 0 else 'down' if m < 0 else 'none'}

    Intercept (b) = {b}

    • Crosses y-axis at (0, {b})
    • Vertical shift: {'Above origin' if b > 0 else 'Below origin' if b < 0 else 'At origin'}

    Equation: y = {m}x + {b}
    """
    plt.text(0.1, 0.5, info_text, fontsize=12, family='monospace',
             bbox=dict(boxstyle="round,pad=1", facecolor="lightblue", alpha=0.8))

    plt.tight_layout()
    plt.show()


# Run all visualizations
if __name__ == "__main__":
    print("=" * 60)
    print("VISUALIZING SLOPE (m) AND INTERCEPT (b)")
    print("=" * 60)

    # 1. Show how slope affects steepness
    print("\n1. Different slopes (m values) - same intercept b=0")
    plot_slope_comparison()

    # 2. Show how intercept shifts parallel lines
    print("\n2. Same slope (m=2) - different intercepts (b values)")
    plot_intercept_comparison()

    # 3. Show extreme cases
    print("\n3. Extreme cases of slope")
    plot_extreme_cases()

    # 4. Show slopes and angles
    print("\n4. Slope values and their angles with x-axis")
    plot_slope_angles()

    # 5. Interactive example (you can change m and b values)
    print("\n5. Interactive example with m=2, b=3")
    interactive_line_explorer(m=2, b=3)  # 

    print("\n" + "=" * 60)
    print("Try changing parameters in interactive_line_explorer(m, b)")
    print("Example: interactive_line_explorer(m=0.5, b=-2)")
    print("=" * 60)