# Import pygame into our program
import pygame
import pygame.freetype
import time

from scene import *
from object3d import *
from mesh import *
from material import *
from color import *

# Define a main function, just to keep things nice and tidy
def main():
    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window
    res_x = 640
    res_y = 480

    # Create a window and a display surface
    screen = pygame.display.set_mode((res_x, res_y))

    # Create a scene
    scene = Scene("TestScene")
    scene.camera = Camera(False, res_x, res_y)

    # Moves the camera back 2 units
    scene.camera.position -= vector3(0,0,2)

    obj1 = Object3d("Object1")
    obj1.scale = vector3(1, 1, 1)
    obj1.position = vector3(0, 0, 0)
    obj1.mesh = Mesh.create_legend((1, 1, 1))
    obj1.material = Material(color(1,1,0,1), "Material1")
    scene.add_object(obj1)

    obj2 = Object3d("Object2")
    obj2.scale = vector3(2, 2, 2)
    obj2.position = vector3(3, 0, 4)
    obj2.mesh = Mesh.create_legend((1, 1, 1))
    obj2.material = Material(color(1,1,0,1), "Material2")
    scene.add_object(obj2)

    obj3 = Object3d("Object3")
    obj3.scale = vector3(3, 3, 3)
    obj3.position = vector3(6, 0, 2)
    obj3.mesh = Mesh.create_legend((1, 1, 1))
    obj3.material = Material(color(1,1,0,1), "Material3")
    scene.add_object(obj3)

    obj4 = Object3d("Object4")
    obj4.scale = vector3(1, 1, 1)
    obj4.position = vector3(1, 0, 5)
    obj4.mesh = Mesh.create_legend((1, 1, 1))
    obj4.material = Material(color(1,1,0,1), "Material4")
    scene.add_object(obj4)

    # Timer
    delta_time = 0
    prev_time = time.time()

    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)

    # Game loop, runs forever
    while (True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                return
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    return
            
        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,0))

        scene.render(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()

        # Updates the timer, so we we know how long has it been since the last frame
        delta_time = time.time() - prev_time
        prev_time = time.time()


# Run the main function
main()
