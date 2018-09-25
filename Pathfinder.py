'''
The Pathfinder class is responsible for finding a solution (i.e., a
sequence of actions) that takes the agent from the initial state to all
of the goals with optimal cost.

This task is done in the solve method, as parameterized
by a maze pathfinding problem, and is aided by the SearchTreeNode DS.
'''

from MazeProblem import MazeProblem
from SearchTreeNode import SearchTreeNode
import unittest
import heapq

def solve (problem, initial, goals):
    possible_moves = problem.transitions(initial)
    print(possible_moves)
    best_cost_move = possible_moves[0]
    print(best_cost_move)




class PathfinderTests(unittest.TestCase):

    def test_maze1(self):
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.M.X",
                "X.X.X.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (1, 3)
        goals   = [(5, 3)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 8)

    # def test_maze2(self):
    #     maze = ["XXXXXXX",
    #             "X.....X",
    #             "X.M.M.X",
    #             "X.X.X.X",
    #             "XXXXXXX"]
    #     problem = MazeProblem(maze)
    #     initial = (1, 3)
    #     goals   = [(3, 3),(5, 3)]
    #     soln = solve(problem, initial, goals)
    #     (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
    #     self.assertTrue(is_soln)
    #     self.assertEqual(soln_cost, 12)
    #
    # def test_maze3(self):
    #     maze = ["XXXXXXX",
    #             "X.....X",
    #             "X.M.MMX",
    #             "X...M.X",
    #             "XXXXXXX"]
    #     problem = MazeProblem(maze)
    #     initial = (5, 1)
    #     goals   = [(5, 3), (1, 3), (1, 1)]
    #     soln = solve(problem, initial, goals)
    #     (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
    #     self.assertTrue(is_soln)
    #     self.assertEqual(soln_cost, 12)
    #
    # def test_maze4(self):
    #     maze = ["XXXXXXX",
    #             "X.....X",
    #             "X.M.XXX",
    #             "X...X.X",
    #             "XXXXXXX"]
    #     problem = MazeProblem(maze)
    #     initial = (5, 1)
    #     goals   = [(5, 3), (1, 3), (1, 1)]
    #     soln = solve(problem, initial, goals)
    #     self.assertTrue(soln == None)


if __name__ == '__main__':
    unittest.main()