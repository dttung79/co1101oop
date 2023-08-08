# Exercise: Pygame Shape Drawing

# Your task is to extend the basic Pygame application provided in class. Here are your instructions:

# Create a Game class similar to the one provided in class. Define it in such a way that when you create an instance of the class, you can specify the window's width and height.

# Define color variables for YELLOW, PURPLE, and CYAN within the Game class.

# Create separate methods for drawing a triangle, an ellipse, and a polygon. Each of these methods should accept parameters for the shape's position and size. The color for each shape should be one of the colors defined in step 2.

# For the triangle, consider using the pygame.draw.polygon function, which can draw any polygon, not just triangles. You just need to provide three points for the vertices of the triangle.

# For the ellipse, use the pygame.draw.ellipse function. Keep in mind that the position and size parameters for this function specify the rectangle within which the ellipse is drawn.

# For the polygon, you can also use the pygame.draw.polygon function. Try to draw a pentagon or hexagon.

# Create a draw_shapes method that calls each of the shape-drawing methods with appropriate arguments to draw the shapes at different positions and with different sizes.

# Finally, create a run method that starts the game loop. In each frame of the loop, the window should be filled with a color of your choice, the shapes should be drawn by calling the draw_shapes method, and the display should be updated.

# Outside of the Game class, create an instance of the class and call its run method to start the game.

# Remember to handle the QUIT event in your game loop to allow the user to close the game window.
