import turtle

# SETUP
SetOfPoints = []
canva = turtle
FractalDrawer = None

# define the set of points for the main triangle
def setPoints(scale=5):
    return [
        [-70 * scale, -50 * scale],
        [0          , 70 * scale],
        [70 * scale, -50 * scale]
    ]

def setup():
    canva.title("Sierpinski Triangle")
    canva.bgcolor("black")
    canva.setup(1000,800)

    # create a turtle object for drawing the fractal
    drawer = canva.Turtle()
    drawer.ht() 
    drawer.speed(10)
    drawer.pencolor('white')
    return drawer

# function to find the middle point of two given points
def FindMiddlePoint(p1, p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

# function to recursively draw the Sierpinski triangle
def DrawTheTriangle(SetOfPoints, Depth=6):
    if (Depth > 0) :
        # set the color of the triangle based on the depth
        if Depth == 1:
            drawer.pencolor('red')
        elif Depth == 2:
            drawer.pencolor('green')
        elif Depth == 3:
            drawer.pencolor('blue')
        else:
            drawer.pencolor('white')
        
        # move the turtle to the first point and draw the triangle
        drawer.up()
        drawer.goto(SetOfPoints[0][0], SetOfPoints[0][1])
        drawer.down()
        drawer.goto(SetOfPoints[1][0], SetOfPoints[1][1])
        drawer.goto(SetOfPoints[2][0], SetOfPoints[2][1])
        drawer.goto(SetOfPoints[0][0], SetOfPoints[0][1])

        # recursively call the function to draw the sub-triangles
        Depth = Depth - 1
        DrawTheTriangle([SetOfPoints[0], FindMiddlePoint(SetOfPoints[0], SetOfPoints[1]), FindMiddlePoint(SetOfPoints[0], SetOfPoints[2])], Depth)
        DrawTheTriangle([SetOfPoints[1], FindMiddlePoint(SetOfPoints[1], SetOfPoints[0]), FindMiddlePoint(SetOfPoints[1], SetOfPoints[2])], Depth)
        DrawTheTriangle([SetOfPoints[2], FindMiddlePoint(SetOfPoints[2], SetOfPoints[1]), FindMiddlePoint(SetOfPoints[2], SetOfPoints[0])], Depth)


depth = input("At what depth do you want the triangles to be drawn? [2-6] \n")

drawer = setup()

# move the turtle to the center and draw a dot
drawer.up()
drawer.goto(0,0)
drawer.dot(7,'red')

# call the function to start drawing the fractal
if(depth.isnumeric()):
    DrawTheTriangle(
        setPoints(),
        int(depth)
    )
else:
    DrawTheTriangle(setPoints())


# wait for user input
input("Press ENTER to continue...")