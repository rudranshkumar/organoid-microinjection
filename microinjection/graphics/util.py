# GRAPHICS UTILITY LIBRARY

def win_center_coords(screen_width, screen_height):

    '''
    Computes target x and y coords with window dimensions to center a window in user's screen

    Parameters:
        screen_width (int): Width of screen
        screen_height (int): Height of screen

    Returns:
        window_dimensions (tuple): (x coordinte of win, y coordinate of win, win width, win height)
    '''

    win_width = screen_width / 2
    win_height = screen_height / 2
    win_origin_x = (screen_width - win_width) / 2
    win_origin_y = (screen_height - win_height) / 2

    return (win_origin_x, win_origin_y, win_width, win_height)
