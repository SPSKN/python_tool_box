import unittest

class Point: # The object to hold the values of the points of the rectangles
    def __init__(self,x,y,):
        self.x = x
        self.y = y


def intersection(l1,r1,l2,r2):
    if(l1.x == r1.x or l1.y == r1.y or l2.x == r2.x or l2.y == r2.y): # Checking if the points are a line and not a rectangle
        return False
    if(l1.x >= r2.x or r2.y >= l1.y): # checking if the points are beside the first rectangle
        return False
    if(r1.y >= l2.y or r2.y >= l1.y): # checking if the points are above the first rectangle
        return False
    return True


def containment(l1,r1,l2,r2):
    if(l1.x == r1.x or l1.y == r1.y or l2.x == r2.x or l2.y == r2.y): # Checking if the points are a line and not a rectangle
        return False
    if(l1.y < l2.y or r1.x < r2.x): # Checking if the points are outside the first rectangle
        return False
    return True
    


def adjacency(l1,r1,l2,r2):
    if(l1.x == r1.x or l1.y == r1.y or l2.x == r2.x or l2.y == r2.y): # Checking if the points are a line and not a rectangle
        return False
    if(r1.x == l2.x or r2.y == l1.y): # Checking if one side is adjacent to the other
        return True


def main():# Main function

    topLeft1 = Point(int(input('Top left 1 X \n')),int(input('Top left 1 Y \n')))
    bottomRight1 = Point(int(input('bottom Right 1 X \n')),int(input('bottom Right 1 Y \n')))
    topLeft2 = Point(int(input('Top left 2 X \n')),int(input('Top left 2 Y \n')))
    bottomRight2 = Point(int(input('bottom Right 2 X \n')),int(input('bottom Right 2 Y \n')))

    if (containment(topLeft1,bottomRight1,topLeft2,bottomRight2)): # First check if the points of the second rectangle are within the first retangle
        print('Rectangle is Contained within the other')
        print('Not adjacent')
        print('They do not intersect')
    else:
        print('No Containment')
        if (adjacency(topLeft1,bottomRight1,topLeft2,bottomRight2)): # Next check if the rectangles are adjacent
            print('They are Adjacent')
            print('They do not intersect')
        else:
            print('Not adjacent')
            if (intersection(topLeft1,bottomRight1,topLeft2,bottomRight2)): # Finally check if they intersect
                print('Rectangles intersect')
            else:
                print('They do not intersect')

class TestProgram (unittest.TestCase):
        def test_Containment(self):
            topLeft1 = Point(0,10)
            bottomRight1 = Point(10,0)
            topLeft2 = Point(5,5)
            bottomRight2 = Point(6,1)
            self.assertEquals(containment(topLeft1,bottomRight1,topLeft2,bottomRight2),True)
            
        def test_adjacent(self): 
            topLeft1 = Point(0,10)
            bottomRight1 = Point(10,0)
            topLeft2 = Point(10,5)
            bottomRight2 = Point(15,0) 
            self.assertEquals(adjacency(topLeft1,bottomRight1,topLeft2,bottomRight2),True)

        def test_intersection(self): 
            topLeft1 = Point(0,10)
            bottomRight1 = Point(10,0)
            topLeft2 = Point(10,5)
            bottomRight2 = Point(15,0) 
            self.assertEquals(intersection(topLeft1,bottomRight1,topLeft2,bottomRight2),True)


if __name__ == '__main__':
    main()
    unittest.main()
    