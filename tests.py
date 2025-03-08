import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_reset_cells_visited(self):
        # Create a small test maze (2x2)
        maze = Maze(0, 0, 2, 2, 10, 10)
        
        # First, ensure some cells are marked as visited
        maze._cells[0][0].visited = True
        maze._cells[0][1].visited = True
        maze._cells[1][0].visited = True
        maze._cells[1][1].visited = True
        
        # Call the reset function
        maze._reset_cells_visited()
        
        # Check that all cells are now marked as not visited
        self.assertFalse(maze._cells[0][0].visited)
        self.assertFalse(maze._cells[0][1].visited)
        self.assertFalse(maze._cells[1][0].visited)
        self.assertFalse(maze._cells[1][1].visited)

if __name__ == "__main__":
    unittest.main()