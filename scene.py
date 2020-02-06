from camera import *
from vector3 import *
from object3d import *
from color import *

class Scene:
    def __init__(self, name):
        self.name = name
        self.camera = Camera(True, 1280, 720)
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def render(self, screen):
        camera_matrix = self.camera.get_camera_matrix()
        projection_matrix = self.camera.get_projection_matrix()

        clip_matrix = camera_matrix @ projection_matrix

        for obj in self.objects:
            if (dot_product(self.camera.forward().normalized(), - (obj.position - self.camera.position).normalized()) > -0.5):
                continue
            else:
                obj.render(screen, clip_matrix)

