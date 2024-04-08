class Bird:
    # Attributes
    weight = 15
    size = 4
    color = "yellow"

    # Constructor - Setup every variable
    def __init__(self, weight, size, color):
        self.weight = weight
        self.size = size
        self.color = color

    def __str__(self):
        return "weight: " + str(self.weight) + " size: " + str(self.size) + " color: " + self.color


    def get_weight(self):
        return self.weight

    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def set_weight(self, new_weight):
        self.weight = new_weight
    def set_size(self, new_size):
        self.size = new_size
    def set_color(self, new_color):
        self.color = new_color

