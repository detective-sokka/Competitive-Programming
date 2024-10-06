# Note : BFS seems to run faster compared to my DFS solution. Not exactly sure why that is. 

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_rooms = set()
        visited_rooms.add(0)
        stack = []
        stack.append(0)

        while len(stack) > 0:
            visit_room = stack.pop()
            visited_rooms.add(visit_room)

            for room_key in rooms[visit_room]:
                if room_key > 0 and room_key < len(rooms) and (room_key not in visited_rooms):
                    stack.append(room_key)
        
        if len(visited_rooms) == len(rooms):
            return True

        return False
            