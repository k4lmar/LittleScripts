        #x,y
points=[[1,2],
        [4,5],
        [4,1],
        [7,4],
        [9,4],
        [5,5],
        [2,1],
        [7,6],
        [9,6],
        [4,7],
        [4,2],
        [4,4],
            ]

class Node():
    def __init__(self, x,y,w,h,pts):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.pts=pts
        self.children=[]

class Qtree():
    def __init__(self, th, points):
        self.rootnode=Node(0,0,10,10,points)
        self.th=th
    def buildtree(self):
        self.recdiv(self.rootnode, self.th)
    def pts_in_area(self, points, x,y,w,h):
        pts=[]
        for p in points:
            if p[0]>=x and p[0]<=x+w and p[1]>=y and p[1]<=y+h:
                pts.append(p)
        return pts
    def recdiv(self, node, th):
        if not len(node.pts)<=th:
            
            _w = float(node.w/2)
            _h = float(node.h/2)
            
            p= self.pts_in_area(node.pts, node.x, node.y, _w,_h)
            n1=Node(node.x, node.y, _w, _h, p)
            self.recdiv(n1,th)
            
            p= self.pts_in_area(node.pts, node.x+_w, node.y, _w,_h)
            n2=Node(node.x+_w, node.y, _w, _h, p)
            self.recdiv(n2,th)

            p= self.pts_in_area(node.pts, node.x, node.y+_h, _w,_h)
            n3=Node(node.x, node.y+_h, _w, _h, p)
            self.recdiv(n3,th)

            p= self.pts_in_area(node.pts, node.x+_w, node.y+_h, _w, _h)
            n4=Node(node.x+_w ,node.y+_h, _w, _h, p)
            self.recdiv(n4,th)

            node.children=[n1,n2,n3,n4]
    def searchp(self, node, p):
        for child in node.children:
            if p[0]>=child.x and p[0]<=child.x+child.w and p[1]>=child.y and p[1]<=child.y+child.h:
                print(child.pts)
                if len(child.pts)>self.th:
                    self.searchp(child, p)
                else:
                    print("end?")
                    
        

qt=Qtree(3, points)
qt.buildtree()
qt.searchp(qt.rootnode,[4,4])



        
    
