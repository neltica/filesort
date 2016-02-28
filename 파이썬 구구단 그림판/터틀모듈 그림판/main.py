
import turtle

canvas = turtle.getcanvas()  # ��Ʋ���� ������ ����� ȭ���� �����´�.
drawFlag = False    # ���� Ŭ���� �� �������� üũ�ϴ� �÷��׺���  draw_line���� ����Ѵ�.
color = 'black'   #�� ����
bgcolor = 'white'  # ������

canvas.config(background = bgcolor)  #�˹������ٰ� ������ �����ش�.


last_point = (-1, -1)  # ���ʿ��� ����Ʈ�� ���̸� �ȵǹǷ� (-1,-1) �������� ������.


def penClick(event):   #���� ���� ���ʿ� ȣ��Ǵ� �Լ�
    global last_point
    x = canvas.canvasx(event.x)  #���� ȭ�鿡 ������ִ� ĵ������ x����� �����´�.
    y = canvas.canvasy(event.y)  #���� ȭ�鿡 ������ִ� ĵ������ y����� �����´�.
    last_point = (x, y)         #��������Ʈ�� �ٲ��ش�. (Ŭ���������� ������ ����Ʈ�����̹Ƿ�)


def draw_line(event):  #�������¿��� �����̴� ����(�巡�׻���) ���� �۵��ϴ� �Լ�

    global drawFlag, last_point
    if(drawFlag):   # �÷��� ���¿� ���� ���� ������ ���� ���Ѵ�.
        return
    drawFlag = True
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    canvas.create_line(\
        last_point[0], last_point[1], x, y, fill = color)    # ���� �ߴ´�.  last_point�������� ���� ���콺�� ��ġ�� (x,y) ��������
    last_point = (x, y)  #last_point������ ���� ���ؼ� ���� draw_line ȣ��ÿ� �������� last_line�� ���Ѵ�.
    drawFlag = False

def stop_drawing(event):
    global last_point
    last_point = (-1, -1)  # ���콺�� ���� �����ϴ� �Լ��� ����Ʈ�� (-1,-1)�� ������.


def main():
    canvas.bind('<Button-1>', penClick)   # ��ư�� �������� ȣ��� �Լ��� �����Ѵ�.
    canvas.bind('<B1-Motion>', draw_line)  # ��ư�� �������·� �����϶� ȣ��� �Լ��� �����Ѵ�.
    canvas.bind('<ButtonRelease-1>', stop_drawing)   # ��ư�� ������ ������ �Լ��� �����Ѵ�.


if __name__=="__main__": # �� �ҽ��� ���۽�ų��� �� ������ �������� �� main�����̸�
    main()  # main()�Լ��� ���۽�Ų��.
turtle.mainloop()   # mainloop()�Լ��� ���۽��Ѿ� ����� turtle�� �����Ѵ�.