import svgwrite
import math


def calculate_hexagon_points(cx, cy, apothem):
    R = 2 * apothem / math.sqrt(3)

    angles_deg = [30, 90, 150, 210, 270, 330]

    points = []
    for angle in angles_deg:
        rad = math.radians(angle)
        x = round(cx + R * math.cos(rad))
        y = round(cy - R * math.sin(rad))
        points.append((x, y))

    return points


def draw_square(dwg):
    x = int(input("Top-left X: "))
    y = int(input("Top-left Y: "))
    size = int(input("Side length: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")
    dwg.add(dwg.rect(insert=(x, y), size=(size, size), fill=fill, stroke=stroke))


def draw_circle(dwg):
    cx = int(input("Center X: "))
    cy = int(input("Center Y: "))
    r = int(input("Radius: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")
    dwg.add(dwg.circle(center=(cx, cy), r=r, fill=fill, stroke=stroke))


def draw_hexagon(dwg):
    cx = int(input("Middle point X: "))
    cy = int(input("Middle point Y: "))
    apothem = int(input("Apothem length: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")

    points = calculate_hexagon_points(cx, cy, apothem)
    dwg.add(dwg.polygon(points=points, fill=fill, stroke=stroke))


def save_svg(dwg):
    filename = input("Insert filename: ")
    proceed = input(f'Saving file to "{filename}"\nProceed (y/n)?: ').lower()
    if proceed == "y":
        dwg.save()
        print("Vector saved successfully!")


def main():
    print("Program starting.")
    dwg = svgwrite.Drawing(size=("500px", "500px"))

    while True:
        print("\nOptions:")
        print("1 - Draw square")
        print("2 - Draw circle")
        print("3 - Draw hexagon")
        print("4 - Save svg")
        print("0 - Exit")

        choice = input("Your choice: ")

        if choice == "1":
            draw_square(dwg)
        elif choice == "2":
            draw_circle(dwg)
        elif choice == "3":
            draw_hexagon(dwg)
        elif choice == "4":
            save_svg(dwg)
        elif choice == "0":
            print("Exiting program.\n\nProgram ending.")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
