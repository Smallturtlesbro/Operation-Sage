import unittest
import mapping.room

class TestRoomClass(unittest.TestCase):

    def setUp(self):
        self.test = mapping.room.Room(3, 3)

    def testRoomExists(self):
        self.assertTrue(self.test is not None)

    def testInitSize(self):
        self.assertTrue(self.test.size is not None)
        self.assertEqual(self.test.size, (3, 3))
        self.assertEqual(mapping.room.Room(9, 9).size, (9, 9))

    def testContents(self):
        self.assertTrue(self.test.contents is not None)
        new_room = mapping.room.Room(3,3); new_room.contents.append('dagger')
        self.assertEqual(new_room.contents, ['dagger'])


class TestMapTile(unittest.TestCase):

    def setUp(self):
        self.test = mapping.room.MapTile(1, 3)

    def testMapTile(self):
        self.assertEqual(self.test.x, 1)
        self.assertEqual(self.test.y, 3)



if __name__ == '__main__':
    unittest.main()
