
class MapTile:
    def __init__(self):
        self.x = x
        self.y = y

        def intro_text(self):
            raise NotImplementedError("Create a subclass instead!")


class StartTile(MapTile):
    def intro_text(self):
        return '''
        You wake up in a cell with nothing but a bed, bucket, bowl, and plate.
        There is a torch on the other side of the bars and a cellar wind at the 
        top of the wall behind you.
        '''


class BoringTile(MapTile):
    def intro_text(self):
        return '''
        There isn't much to this part of your cell, all you can hear is the bustle of the busy
        streets out of the window.
        '''


class CellarWindowTile(MapTile):
    def intro_text(self):
        return '''
        The window is a semicircle with 6 iron bars. When you peak through, all you can really
        see is the feet of different races and animals. 
        It seems like the brick at the bottom of one of the bars is a little loose. 
        As you grab the bar to get a peak the brick underneath gives way and the bar pulls out 
        of the window.
        \x1B[3mIron bar has been added to your inventory.\x1B[0m
        '''


world_map = [
    [None, CellarWindowTile(1, 0), None],
    [None, BoringTile(1, 1), None],
    [BoringTile(0, 2), StartTile(1, 2), BoringTile(2, 2)],
    [None, BoringTile(1, 3), None]
]


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[x][y]
    except IndexError:
        return None
