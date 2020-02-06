+import pygame
from vector3 import *

class Mesh:
    def __init__(self, name = "UnknownMesh"):
        self.name = name
        self.polygons = []

    def offset(self, v):
        new_polys = []
        for poly in self.polygons:
            new_poly = []
            for p in poly:
                new_poly.append(p + v)
            new_polys.append(new_poly)

        self.polygons = new_polys

    def render(self, screen, matrix, material):
        c = material.color.tuple3()        

        for poly in self.polygons:
            tpoly = []
            for v in poly:
                vout = v.to_np4()
                vout = vout @ matrix
                
                tpoly.append( ( screen.get_width() * 0.5 + vout[0] / vout[3], screen.get_height() * 0.5 - vout[1] / vout[3]) )

            pygame.draw.polygon(screen, c, tpoly, material.line_width)


    @staticmethod
    #Creating triangular prism
    def create_legend(size, mesh = None):
        if (mesh == None):
            mesh = Mesh("LegendaryLegend")

        Mesh.create_triangle(vector3(0, 0, size[0] * 0.5), vector3(size[1] * 0.5 , 0, 0), vector3(0, size[2] * 0.5, 0), mesh)
        Mesh.create_triangle(vector3(0, 0, -size[0] * 0.5), vector3(size[1] * 0.5, 0, 0), vector3(0, size[2] * 0.5, 0), mesh)

        Mesh.create_square(vector3(-size[0] * 0.5, 0, 0), vector3(0, size[1] * 0.5, 0), vector3(0, 0, size[2] * 0.5), mesh)
        Mesh.create_square(vector3(0, -size[0] * 0.5, 0), vector3(size[1] * 0.5, 0, 0), vector3(0, 0, size[2] * 0.5), mesh)
        Mesh.create_square(vector3(0, 0, 0), vector3(-size[1] * 0.5, size[1] * 0.5, 0), vector3(0,0, size[2] * 0.5), mesh)

        return mesh

    @staticmethod
    #Creating child triangular prism
    def create_childlegend(size, mesh = None):
        if (mesh == None):
            mesh = Mesh("LegendaryLegend")

        Mesh.create_triangle(vector3(0, 0, -size[0] * 0.5), vector3(size[1] * 0.5 , 0, 0), vector3(0, -size[2] * 0.5, 0), mesh)
        Mesh.create_triangle(vector3(0, 0, size[0] * 0.5), vector3(size[1] * 0.5, 0, 0), vector3(0, -size[2] * 0.5, 0), mesh)

        Mesh.create_square(vector3(-size[0] * 0.5, 0, 0), vector3(0, -size[1] * 0.5, 0), vector3(0, 0, -size[2] * 0.5), mesh)
        Mesh.create_square(vector3(0, size[0] * 0.5, 0), vector3(size[1] * 0.5, 0, 0), vector3(0, 0, -size[2] * 0.5), mesh)
        Mesh.create_square(vector3(0, 0, 0), vector3(-size[1] * 0.5, -size[1] * 0.5, 0), vector3(0,0, -size[2] * 0.5), mesh)

        return mesh


    @staticmethod
    #Creating square
    def create_square(origin, axis0, axis1, mesh):
        if (mesh == None):
            mesh = Mesh("LegendarySquare")

        poly = []
        poly.append(origin + axis0 + axis1)
        poly.append(origin + axis0 - axis1)
        poly.append(origin - axis0 - axis1)
        poly.append(origin - axis0 + axis1)

        mesh.polygons.append(poly)

        return mesh

    
    @staticmethod
    #Creating triangle
    def create_triangle(origin, axis0, axis1, mesh):
        if (mesh == None):
            mesh = Mesh("LegendaryTriangle")

        poly = []
        poly.append(origin - axis0 + axis1)
        poly.append(origin - axis0 - axis1)
        poly.append(origin + axis0 - axis1)

        mesh.polygons.append(poly)

        return mesh

