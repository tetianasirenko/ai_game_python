from model.player_view import PlayerView


class ResourceProcessor:
    def __init__(self, player_id, entities):
        self.__player_id = player_id
        self.__current_resources = 0
        self.__entities = entities

    def checkCoordinates(self, x, y):

        for entity in self.__entities:
            if entity.player_id != self.__player_id and entity.position.x == x and entity.position.y == y and entity.entity_type == None:
                return 1
        return 0

    def getMyPlayerResources(self, player_view):
        for player in player_view.players:
            if player.id == self.__player_id:
                self.__current_resources = player.resource
        return self.__current_resources

    def canBuildHouse(self):
        if self.__current_resources > 100:
            return 1

    def findHouseCoordinates(self, map_size, map):
        house_size = 3
        x_step = 0
        y_step = 0

        start_x = 0
        start_y = 0

        for x in range(start_x + 1, map_size - 1):
            for y in range(start_y + 1, map_size - 1):
                can_build = True
                for x_check in range(x - 1, x + 1):
                    for y_check in range(y - 1, y + 1):
                        if map[x_check, y_check] is not None:
                            can_build = False
                if can_build:
                    return x, y
