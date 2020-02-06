# Import pygame into our program
import pygame
import pygame.freetype
import time
import math

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
    res_x = 1280
    res_y = 720

    move = 0.02
    sens = 10

    forward = False
    backwards = False
    left = False
    right = False

    # Create a window and a display surface
    screen = pygame.display.set_mode((res_x, res_y))

    # Create a scene
    scene = Scene("TestScene")
    scene.camera = Camera(False, res_x, res_y)

    # Moves the camera back 2 units
    scene.camera.position -= vector3(0,0,2)
    pygame.mouse.set_pos(res_x/2, res_y/2)

    #Creates object 1
    obj1 = Object3d("Object1")
    obj1.scale = vector3(1, 1, 1)
    obj1.position = vector3(0, 0, 0)
    obj1.mesh = Mesh.create_legend((1, 1, 1))
    obj1.material = Material(color(1,1,0,1), "Material1")
    scene.add_object(obj1)

    #Creates object 2
    obj2 = Object3d("Object2")
    obj2.scale = vector3(2, 2, 2)
    obj2.position = vector3(3, 0, 4)
    obj2.mesh = Mesh.create_legend((1, 1, 1))
    obj2.material = Material(color(1,1,0,1), "Material2")
    scene.add_object(obj2)

    #Creates object 3
    obj3 = Object3d("Object3")
    obj3.scale = vector3(3, 3, 3)
    obj3.position = vector3(6, 0, 2)
    obj3.mesh = Mesh.create_legend((1, 1, 1))
    obj3.material = Material(color(1,1,0,1), "Material3")
    scene.add_object(obj3)

    #Creates object 4
    obj4 = Object3d("Object4")
    obj4.scale = vector3(1, 1, 1)
    obj4.position = vector3(1, 0, 5)
    obj4.mesh = Mesh.create_legend((1, 1, 1))
    obj4.material = Material(color(1,1,0,1), "Material4")
    scene.add_object(obj4)

    # Setting the rotation to 0 with 15 angle
    angle = 15
    axis = vector3(0,0,0)

    # Timer
    delta_time = 0
    prev_time = time.time()

    #Cursor not visible, get events
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

            #Check for key presses (WASD) to calculate movement
            if (pygame.key.get_pressed()[pygame.K_w]):
                forward = True
            else:
                forward = False
            if (pygame.key.get_pressed()[pygame.K_s]):
                backwards = True
            else:
                backwards = False
            if (pygame.key.get_pressed()[pygame.K_a]):
                left = True
            else:
                left = False
            if (pygame.key.get_pressed()[pygame.K_d]):
                right = True
            else:
                right = False
            
        #Executes the movement
        if forward:
            scene.camera.position += scene.camera.forward() * move
        if backwards:
            scene.camera.position -= scene.camera.forward() * move
        if left:
            scene.camera.position -= scene.camera.right() * move
        if right:
            scene.camera.position += scene.camera.right() * move
        scene.camera.position = vector3(scene.camera.position.x, 0, scene.camera.position.z)




        #Camera Movement Up
        if(pygame.mouse.get_pos()[1] < res_y / 2):
            axis += scene.camera.right() * sens
           
        #Camera Movement Down
        if(pygame.mouse.get_pos()[1] > res_y / 2):
            axis -= scene.camera.right() * sens

            #Camera Movement Left
        if(pygame.mouse.get_pos()[0] < res_x / 2):
            mouse_x = pygame.mouse.get_pos()[0] - (res_x/2)
            axis -= vector3(0,mouse_x,0)

            #Camera Movement Right    
        if(pygame.mouse.get_pos()[0] > res_x / 2):
            mouse_x = pygame.mouse.get_pos()[0] - (res_x/2)
            axis -= vector3(0,mouse_x,0)

        pygame.mouse.set_pos((res_x / 2, res_y / 2))

        #Set's the camera to rotate according to the mouse movement calculated above
        camera_rotation = from_rotation_vector((axis * math.radians(angle) * delta_time).to_np3()) 
        scene.camera.rotation *= camera_rotation

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,0))

        scene.render(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()

        # Updates the timer, so we we know how long has it been since the last frame
        delta_time = time.time() - prev_time
        prev_time = time.time()

        axis = vector3(0, 0, 0)


# Run the main function
main()
