from model import *
from resource_processor import ResourceProcessor
from map_processor import MapProcessor
import constants


class MyStrategy:
    def get_action(self, player_view, debug_interface):
        result = Action({})
        my_id = player_view.my_id
        house_coord = None
        house_builder = constants.HOUSE_BUILDERS

        resource_processor = ResourceProcessor(my_id, player_view.entities)
        map_processor = MapProcessor(player_view)

        current_resource = resource_processor.getMyPlayerResources(player_view)
        print (current_resource)

        for entity in player_view.entities:

            if entity.player_id != my_id:
                continue
            properties = player_view.entity_properties[entity.entity_type]
            print(properties)

            move_action = None
            build_action = None

            #if properties.build == EntityType.HOUSE:
            #    continue

            if house_builder > 0 and resource_processor.canBuildHouse() and entity.entity_type == EntityType.BUILDER_UNIT:
                if house_coord is None:
                    house_coord = resource_processor.findHouseCoordinates(player_view.map_size, map_processor.get_map())
                print("House=", house_coord)

                if house_coord:
                    build_action = BuildAction(
                        EntityType.HOUSE,
                        Vec2Int(house_coord[0], house_coord[1]))
                    house_builder = house_builder-1

            elif current_resource > constants.POPULATION_LIMIT:
                build_action = BuildAction(
                        EntityType.BUILDER_UNIT,
                        Vec2Int(entity.position.x + properties.size, entity.position.y + properties.size - 1))
                if properties.can_move:
                    move_action = MoveAction(
                        Vec2Int(player_view.map_size - 1,
                                player_view.map_size - 1),
                        True,
                        True)

            result.entity_actions[entity.id] = EntityAction(
                move_action,
                build_action,
                AttackAction(None, AutoAttack(properties.sight_range, [
                    EntityType.RESOURCE] if entity.entity_type == EntityType.BUILDER_UNIT else [])),
                None
            )
        return result

    def debug_update(self, player_view, debug_interface):
        debug_interface.send(DebugCommand.Clear())
        debug_interface.get_state()
