import SystemColors
rectangles=[]

def entradadades():
    finish = False
    while not finish:
        rectangle=input().split()
        if rectangle[0]==';q' or rectangle[0] ==';Q':
            finish = True
        else:
            rectangles.append(rectangle)
