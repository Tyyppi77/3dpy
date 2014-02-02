import vec3
import polygon


class BaseObject(object):
    """
    Defines a base class for any object, that can be
    created using polygons. The class has a list of polygons, that
    form the object.
    """
    def __init__(self):
        """
        Initializes the object
        """
        self.polys = []

    def add_polygon(self, poly):
        """
        Adds a polygon to the list of polygons
        """
        self.polys.append(poly)

    def render(self):
        """
        Renders the polygons.
        """
        for p in self.polys:
            p.render()


class CubeObject(BaseObject, object):
    """
    Defines a class for creating a 3D Cube. The cube gets a widht, a height
    and a depth. The polygons of the cube are calculated using these values.
    """

    def __init__(self, position_vector=None, width=1.0, height=1.0, depth=1.0):
        """
        Initializes the cube
        """
        BaseObject.__init__(self)

        self.position = position_vector
        if not position_vector:
            self.position = vec3.Vec3f()

        self.verts = []

        #Calculates the corners of the cube and adds them to the list
        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                for k in range(-1, 2, 2):
                    v = vec3.Vec3f(
                        self.position.x + (i * width / 2),
                        self.position.y + (j * height / 2),
                        self.position.z + (k * depth / 2)
                    )
                    self.verts.append(v)

        #Creates the polygons
        self.poly4(0, 1, 3, 2)
        self.poly4(2, 3, 7, 6)
        self.poly4(6, 7, 5, 4)
        self.poly4(4, 5, 1, 0)
        self.poly4(3, 1, 5, 7)
        self.poly4(0, 2, 6, 4)

    def poly4(self, i1, i2, i3, i4):
        """
        Creates a polygon for the cube. The method gets 4 corner points
        of the polygon, and the actual polygon is formed between these.
        """
        vertices = (
            self.verts[i1],
            self.verts[i2],
            self.verts[i3],
            self.verts[i4]
        )
        self.polys.append(polygon.Polygon(vertices=vertices))


class TexturedCubeObject(CubeObject, object):
    """
    Defines a class for a cube that has texture assigned to it.
    The texture will be used in the polygons that the cube creates.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the cube.
        """
        self.args = args

        CubeObject.__init__(self, **kwargs)

    def poly4(self, i1, i2, i3, i4):
        """
        Creates a polygon for the cube. The method gets 4 corner points
        of the polygon, and the actual polygon is formed between these.
        """
        vertices = (
            self.verts[i1],
            self.verts[i2],
            self.verts[i3],
            self.verts[i4]
        )
        self.polys.append(polygon.TexturedPolygon(*self.args, vertices=vertices))