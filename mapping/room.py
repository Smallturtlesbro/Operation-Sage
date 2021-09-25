class Room:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.size = (length, width)
        self.contents = []

class MapTile():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create subclass instead.")

cell = Room(4, 2)
contents = ['bed', 'leg shackles', 'bucket', 'wooden plate', 'wooden cup',]
for item in contents:
    cell.contents.append(item)

print(cell.contents)
