class Map:
    def __init__(self,lvl_map,):
        self.lvlmap = lvl_map
        self.tile_size = 64
        self.screen_width = 1280
        self.screen_height = 780
        pass

level_map = [
'                          ',
'                          ',
'                          ',
'X  P             XX        ',
'XXXXXXXX     XX      XX   ',
'XXXX       XXXX    XXXX   ',
'                          ',
'XXXXXXXX XXXXXX XX XX     ',
'XXXXXXXX XXXXXX XX XXX    ',
'XXXXXXXX XXXXXX XX XXXX   ',
'XXXXXXXX XXXXXX XX XXXX   ']

tile_size = 64
screen_width = 1280
screen_height = len(level_map) * tile_size #makes screen height relative to level map height
print(screen_height)
