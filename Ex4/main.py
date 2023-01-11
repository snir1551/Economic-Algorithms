import search_state_space

if __name__ == '__main__':
    a = [[11,22,33],[11,22,44],[55,33,0]]
    d = search_state_space.state_space_search_BFS(a)
    print(d)

    a = [[0, 0, 0],[0,0,0]]
    d = search_state_space.state_space_search_BFS(a)
    print(d)

    a = [[1, 2, 3], [4, 5, 6]]
    d = search_state_space.state_space_search_BFS(a)
    print(d)



    #search_state_space.draw_tree(d)