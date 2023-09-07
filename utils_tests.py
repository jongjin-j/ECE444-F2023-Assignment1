from utils import utils

u = utils()

# Testing String input
u.reverse("String test")
u.formatter("String test")

# Testing float input
u.reverse(12.34)
u.formatter(12.34)

# Testing integer input
u.reverse(174)
u.formatter(7562)