
import turtle

canvas = turtle.getcanvas()  # 터틀에서 실제로 사용할 화면을 가져온다.
drawFlag = False    # 지금 클릭이 된 상태인지 체크하는 플레그변수  draw_line에서 사용한다.
color = 'black'   #펜 색상
bgcolor = 'white'  # 배경색상

canvas.config(background = bgcolor)  #켄버스에다가 배경색을 입혀준다.


last_point = (-1, -1)  # 최초에는 포인트가 보이면 안되므로 (-1,-1) 지점으로 보낸다.


def penClick(event):   #누른 상태 최초에 호출되는 함수
    global last_point
    x = canvas.canvasx(event.x)  #현재 화면에 띄워져있는 캔버스의 x사이즈를 가져온다.
    y = canvas.canvasy(event.y)  #현재 화면에 띄워져있는 캔버스의 y사이즈를 가져온다.
    last_point = (x, y)         #최종포인트를 바꿔준다. (클릭한지점이 마지막 포인트지점이므로)


def draw_line(event):  #누른상태에서 움직이는 상태(드래그상태) 에서 작동하는 함수

    global drawFlag, last_point
    if(drawFlag):   # 플래그 상태에 따라서 선을 그을지 말지 정한다.
        return
    drawFlag = True
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    canvas.create_line(\
        last_point[0], last_point[1], x, y, fill = color)    # 선을 긋는다.  last_point지점부터 현재 마우스가 위치한 (x,y) 지점까지
    last_point = (x, y)  #last_point지점을 새로 정해서 다음 draw_line 호출시에 시작점인 last_line을 정한다.
    drawFlag = False

def stop_drawing(event):
    global last_point
    last_point = (-1, -1)  # 마우스를 땔때 동작하는 함수로 포인트를 (-1,-1)로 보낸다.


def main():
    canvas.bind('<Button-1>', penClick)   # 버튼을 눌렀을때 호출될 함수를 지정한다.
    canvas.bind('<B1-Motion>', draw_line)  # 버튼을 누른상태로 움직일때 호출될 함수를 지정한다.
    canvas.bind('<ButtonRelease-1>', stop_drawing)   # 버튼을 땠을떄 동작할 함수를 지정한다.


if __name__=="__main__": # 이 소스를 동작시킬경우 이 지점이 시작지점 즉 main지점이면
    main()  # main()함수를 동작시킨다.
turtle.mainloop()   # mainloop()함수를 동작시켜야 제대로 turtle이 동작한다.