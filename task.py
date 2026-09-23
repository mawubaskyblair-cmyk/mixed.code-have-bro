# Create the Point class
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return f"Point({self.x}, {self.y})"

# Create an object
p1 = Point(2, 3)

# Print it
print(p1)
