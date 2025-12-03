from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle


def drawSquare(PDwg: Drawing, left, top, sideLength, color, strokeColor) -> None:
    square = Rect(
        insert=(left, top),
        size=(sideLength, sideLength),
        fill=color,
        stroke=strokeColor,
    )
    PDwg.add(square)


def drawCircle(PDwg: Drawing, centerX, centerY, radius, color, stroke) -> None:
    circle = Circle(center=(centerX, centerY), r=radius, fill=color, stroke=stroke)
    PDwg.add(circle)


def saveSvg(PDwg: Drawing, file) -> None:
    PDwg.saveas(file, pretty=True, indent=2)
