from model.player_view import PlayerView

class MapProcessor:
    def __init__(self, player_view):
        self.__map = {}
        self.__player_id = player_view.my_id
        for x in range(player_view.map_size):
            for y in range(player_view.map_size):
                self.__map[(x, y)] = None

        for entity in player_view.entities:
            self.__map[(entity.position.x, entity.position.y)] = entity

    def get_map(self):
        return self.__map