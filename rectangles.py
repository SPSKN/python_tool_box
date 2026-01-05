class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, p1: Point, p2: Point):
        # Normalize coordinates
        self.left = min(p1.x, p2.x)
        self.right = max(p1.x, p2.x)
        self.top = max(p1.y, p2.y)
        self.bottom = min(p1.y, p2.y)

    def is_valid(self):
        return self.left < self.right and self.bottom < self.top


def intersects(r1: Rectangle, r2: Rectangle) -> bool:
    return not (
        r1.right <= r2.left or
        r1.left >= r2.right or
        r1.top <= r2.bottom or
        r1.bottom >= r2.top
    )


def contains(r1: Rectangle, r2: Rectangle) -> bool:
    return (
        r1.left <= r2.left and
        r1.right >= r2.right and
        r1.top >= r2.top and
        r1.bottom <= r2.bottom
    )


def adjacent(r1: Rectangle, r2: Rectangle) -> bool:
    vertical_touch = (
        r1.right == r2.left or r1.left == r2.right
    ) and not (
        r1.top <= r2.bottom or r1.bottom >= r2.top
    )

    horizontal_touch = (
        r1.top == r2.bottom or r1.bottom == r2.top
    ) and not (
        r1.right <= r2.left or r1.left >= r2.right
    )

    return vertical_touch or horizontal_touch


def main():
    """
    Interactive Rectangle Checker.
    After each check, user can:
        - Check another rectangle
        - Go back to main menu
    """
    while True:
        print("\nRectangle Checker\n-----------------")
        try:
            r1 = Rectangle(
                Point(int(input("Rect 1 X1: ")), int(input("Rect 1 Y1: "))),
                Point(int(input("Rect 1 X2: ")), int(input("Rect 1 Y2: ")))
            )

            r2 = Rectangle(
                Point(int(input("Rect 2 X1: ")), int(input("Rect 2 Y1: "))),
                Point(int(input("Rect 2 X2: ")), int(input("Rect 2 Y2: ")))
            )
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if not r1.is_valid() or not r2.is_valid():
            print("Invalid rectangle dimensions. Make sure width and height are > 0.")
            continue

        # Check containment
        if contains(r1, r2):
            print("Rectangle 2 is contained within Rectangle 1")
        elif contains(r2, r1):
            print("Rectangle 1 is contained within Rectangle 2")
        else:
            print("No containment detected")

        # Check adjacency
        if adjacent(r1, r2):
            print("Rectangles are adjacent")
        else:
            print("Not adjacent")

        # Check intersection
        if intersects(r1, r2):
            print("Rectangles intersect")
        else:
            print("Rectangles do not intersect")

        # Ask user if they want to continue
        while True:
            again = input("\nCheck another rectangle? (Y/N) or B to go back: ").strip().upper()
            if again == "Y":
                break  # repeat the loop
            elif again == "B" or again == "N":
                print("Returning to main menu...")
                return
            else:
                print("Invalid input. Enter Y, N, or B.")
