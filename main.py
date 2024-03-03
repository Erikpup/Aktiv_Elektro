import traceback
# python3,kivy,plyer,jnius,fpdf,android,pandas,xlrd,XlsxWriter,openpyxl
def win():
    from kivy.config import Config
    Config.set('graphics', 'fullscreen', '0')


win()
try:


    from items import Material
    import datetime
    from kivy.uix.dropdown import DropDown
    import sqlite3
    from kivy.clock import Clock
    from kivy.uix.layout import Layout
    from kivy.uix.checkbox import CheckBox
    from kivy.app import App
    from kivy.core.window import Window
    from kivy.graphics import Color, Rectangle
    from kivy.graphics.vertex_instructions import Line
    from kivy.lang import Builder
    from kivy.metrics import dp
    from kivy.properties import ObjectProperty
    from kivy.uix.button import Button
    from kivy.uix.gridlayout import GridLayout
    from kivy.uix.label import Label
    from kivy.uix.popup import Popup
    from kivy.uix.recycleview import RecycleView
    from kivy.uix.relativelayout import RelativeLayout
    from kivy.uix.screenmanager import ScreenManager, Screen
    from kivy.uix.textinput import TextInput
    import smtplib
    from pathlib import Path
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText
    from email.utils import COMMASPACE, formatdate
    from email import encoders
    from plyer import notification
    from fpdf import FPDF
    import pathlib

    Window.clearcolor = (1, 1, 1, 1)

    Builder.load_string("""
    
<FullApp>:
    lable1: address
    lable2: name
    lable3: number
    lable4: player
    lable5: high
    checkbox1: CheckBox1
    checkbox2: CheckBox2
    RelativeLayout:
        pos_hint: {'center_x': .48, 'center_y': .435}
        size_hint: (.92, .75)
        canvas:
            Color:
                rgba: 0, 0, 1, 1    # Blue
      
            # size and position of Canvas
            Rectangle:
                pos: self.pos
                size: self.size
    FloatLayout:
        CheckBox:
            id:CheckBox1 
            text: 'Check'
            active: False
            pos_hint: {'center_x': .6, 'center_y': .395}
            size_hint: (.05, .05)
            color: [1, 1, 1, 100]
        CheckBox:
            id:CheckBox2 
            text: 'Box'
            active: False
            pos_hint: {'center_x': .82, 'center_y': .395}
            size_hint: (.05, .05)
            color: [1, 1, 1, 100]  
    Label:
        text: 'Монтаж:'
        font_size: 50
        pos_hint: {'center_x': .55, 'center_y': .4}
        color: [1,1,1,1]
        id: i3
        halign: "left"
        valign: "middle"
        text_size: i3.size
    Label:
        id: i3
        halign: "left"
        valign: "middle"
        text_size: i3.size
        text: 'Введите адрес объекта'
        font_size: 25
        pos_hint: {'center_x': .55, 'center_y': .78}
        color: [1,1,1,1]
    Label:
        id: i3
        halign: "left"
        valign: "middle"
        text_size: i3.size
        text: 'Введите ФИО'
        font_size: 25
        pos_hint: {'center_x': .55, 'center_y': .665}
        color: [1,1,1,1]
    Label:
        id: i3
        halign: "left"
        valign: "middle"
        text_size: i3.size
        text: 'Введите номер телефона'
        font_size: 25
        pos_hint: {'center_x': .55, 'center_y': .55}
        color: [1,1,1,1]
    Label:
        text: 'Адрес объекта'
        font_size: 55
        pos_hint: {'center_x': .55, 'center_y': .85}
        color: [1,1,1,1]
        id: i3
        halign: "left"
        valign: "middle"
        text_size: i3.size
        
    Label:
        id: i3
        halign: "left"
        valign: "middle"
        text_size: i3.size
        text: 'Имя Клиента'
        font_size: 55
        pos_hint: {'center_x': .55, 'center_y': .74}
        color: [1,1,1,1]
    Label:
        text: 'Номер Телефона'
        font_size: 55
        pos_hint: {'center_x': .55, 'center_y': .625}
        color: [1,1,1,1]
        id: i3
        halign: "left"
        valign: "middle"
        text_size: i3.size
    TextInput:
        id: address
        text: ''
        multiline: False
        height: dp(30)
        pos_hint: {'center_x': .5, 'center_y': .815}
        size_hint_y: None
        size_hint_x: .9
        foreground_color: (0,0,1,1) 
        background_color: [1, 1, 1, 100]
        background_normal: ''
        hint_text_color: (0,0,1,1)
    TextInput:
        id: name
        text: ''
        multiline: False
        height: dp(30)
        pos_hint: {'center_x': .5, 'center_y': .705}
        size_hint_y: None
        size_hint_x: .9
        foreground_color: (0,0,1,1) 
        background_color: [1, 1, 1, 100]
        background_normal: ''
        hint_text_color: (0,0,1,1)
    TextInput:
        id: number
        text: ''
        multiline: False
        height: dp(30)
        pos_hint: {'center_x': .5, 'center_y': .59}
        size_hint_y: None
        size_hint_x: .9
        foreground_color: (0,0,1,1) 
        background_color: [1, 1, 1, 100]
        background_normal: ''
        hint_text_color: (0,0,1,1)
    TextInput:
        id: player
        text: ''
        multiline: False
        height: dp(30)
        pos_hint: {'center_x': .5, 'center_y': .475}
        size_hint_y: None
        size_hint_x: .9
        foreground_color: (0,0,1,1) 
        background_color: [1, 1, 1, 100]
        background_normal: ''
        hint_text_color: (0,0,1,1)
    Label:
        id: play1
        text: 'Введите исполнителя'
        font_size: 25
        pos_hint: {'center_x': .55, 'center_y': .435}
        color: [1,1,1,1]
        halign: "left"
        valign: "middle"
        text_size: play1.size

    Label:
        text: 'Исполнитель'
        font_size: 55
        pos_hint: {'center_x': .55, 'center_y': .51}
        color: [1,1,1,1]
        id: i3
        halign: "left"
        valign: "middle"
        text_size: i3.size
    
    Label:
        text: 'Высота потолка'
        font_size: 45
        pos_hint: {'center_x': .55, 'center_y': .36}
        color: [1,1,1,1]
        id: i3
        halign: "left"
        valign: "middle"
        text_size: i3.size
    
    TextInput:
        id: high
        text: ''
        multiline: False
        pos_hint: {'center_x': .5, 'center_y': .36}
        size_hint_y: .03
        size_hint_x: .2
        foreground_color: (0,0,1,1) 
        background_color: [1, 1, 1, 100]
        background_normal: ''
        hint_text_color: (0,0,1,1)
    
    Label:
        text: 'Материал стен'
        font_size: 45
        pos_hint: {'center_x': .55, 'center_y': .32}
        color: [1,1,1,1]
        id: i3
        halign: "left"
        valign: "middle"
        text_size: i3.size
    Label:
        text: 'Расп коробки'
        font_size: 45
        pos_hint: {'center_x': .55, 'center_y': .28}
        color: [1,1,1,1]
        id: i3
        halign: "left"
        valign: "middle"
        text_size: i3.size
    Label:
        text: 'Щит'
        font_size: 45
        pos_hint: {'center_x': .55, 'center_y': .24}
        color: [1,1,1,1]
        id: i3
        halign: "left"
        valign: "middle"
        text_size: i3.size
    Label:
        text: 'Сеть'
        font_size: 45
        pos_hint: {'center_x': .55, 'center_y': .20}
        color: [1,1,1,1]
        id: i3
        halign: "left"
        valign: "middle"
        text_size: i3.size
        
    Button:
        background_color: [0, 0, 1, 100]
        background_normal:  ''
        height: dp(110)
        size_hint_y: None
        pos_hint: {'center_x': .5, 'center_y': .97}
    Label:
        text: 'ПРОЕКТ'
        font_size: 80
        pos_hint: {'center_x': .5, 'center_y': .95}
        color: [1,1,1,1]
    Button:
        text: '≡'
        background_color: [0, 0, 1, 100]
        background_normal: ''
        font_size: 80
        color: [1, 1, 1, 1]
        font_name: "DejaVuSans.ttf"
        size_hint: (.1, .1)
        pos_hint: {'center_x': .05, 'center_y': .95}
        on_press: root.manager.current = 'menu'
    Label:
        id: error1
        text: ''
        font_size: 30
        pos_hint: {'center_x': .5, 'center_y': .815}
        color: [1,0,0,1]
    Label:
        id: error2
        text: ''
        font_size: 30
        pos_hint: {'center_x': .5, 'center_y': .705}
        color: [1,0,0,1]
    Label:
        id: error3
        text: ''
        font_size: 30
        pos_hint: {'center_x': .5, 'center_y': .59}
        color: [1,0,0,1]
    Label:
        id: error4
        text: ''
        font_size: 30
        pos_hint: {'center_x': .5, 'center_y': .475}
        color: [1,0,0,1]
    Label:
        text: 'Внешний'
        font_size: 35
        pos_hint: {'center_x': .82, 'center_y': .42}
        color: [1,1,1,1]
    Label:
        text: 'Внутренний'
        font_size: 35
        pos_hint: {'center_x': .6, 'center_y': .42}
        color: [1,1,1,1]
    Button:
        text: 'Сохранить'
        size_hint: (.49, .1)
        pos_hint: {'center_x': .25, 'center_y': .05}
        background_color: [0, 0, 1, 100]
        background_normal: ''
        font_size: 40
        color: [1, 1, 1,1]
        on_press: root.func_error(address, name, number, error1, error2, error3, CheckBox1,CheckBox2,player,error4)
    Button:
        text: 'Отменить'
        size_hint: (.49, .1)
        background_color: [0, 0, 1, 100]
        background_normal: ''
        font_size: 40
        color: [1, 1, 1,1]
        pos_hint: {'center_x': .75, 'center_y': .05}
        on_press: root.manager.current = 'main'

<MenuApp>:
    Label:
        text: 'My Program'
        font_size: 40
        pos_hint: {'center_x': .5, 'center_y': .95}
    Button:
        text: 'Мои проекты'
        size_hint: (1, .1)
        pos_hint: {'center_x': .5, 'center_y': .7}
        on_press: root.manager.current = 'main'
        background_color: [1, 1, 1, 100]
        background_normal: 'button.png'
        font_size: 60
        color: [0, 0, 1, 1]
    Button:
        text: 'Полезное'
        size_hint: (1, .1)
        pos_hint: {'center_x': .5, 'center_y': .4}
        on_press: root.manager.current = 'addinfo'
        background_color: [1, 1, 1, 100]
        background_normal: 'button.png'
        font_size: 60
        color: [0, 0, 1, 1]


<MainApp>:
    Button:
        background_color: [0, 0, 1, 100]
        background_normal:  ''
        height: dp(110)
        size_hint_y: None
        pos_hint: {'center_x': .5, 'center_y': .97}
    Label:
        id: title
        text: 'Мои проекты'
        font_size: 80
        pos_hint: {'center_x': .5, 'center_y': .95}
        color: [1,1,1,1]
    Button:
        id: back
        text: '≡'
        background_color: [0, 0, 1, 100]
        background_normal: ''
        font_size: 90
        color: [1, 1, 1, 1]
        font_name: "DejaVuSans.ttf"
        size_hint: (.1, .1)
        pos_hint: {'center_x': .05, 'center_y': .95}
    Button:
        id: add
        text: '+'
        background_color: [0, 0, 1, 100]
        background_normal: ''
        font_size: 90
        color: [1, 1, 1, 1]
        size_hint: (.15, .1)
        pos_hint: {'center_x': .95, 'center_y': .95}
    Button:
        id: button_add 
        text: 'Добавить проект'
        background_color: [0, 0, 1, 100]
        background_normal: ''
        font_size: 80
        color: [1, 1, 1, 1]
        size_hint: (1, .1)
        pos_hint: {'center_x': .5, 'center_y': .05}
        on_press: root.manager.current = 'full'

<Addinfo>:

    Button:
        background_color: [0, 0, 1, 100]
        background_normal:  ''
        height: dp(110)
        size_hint_y: None
        pos_hint: {'center_x': .5, 'center_y': .97}
    Label:
        id: title
        text: 'Полезное'
        font_size: 80
        pos_hint: {'center_x': .5, 'center_y': .95}
        color: [1,1,1,1]
    Button:
        text: '≡'
        background_color: [0, 0, 1, 100]
        background_normal: ''
        font_size: 90
        color: [1, 1, 1, 1]
        font_name: "DejaVuSans.ttf"
        size_hint: (.1, .1)
        pos_hint: {'center_x': .05, 'center_y': .95}
        on_press: root.manager.current = 'menu'
    Button:
        text: 'Сечение кабеля'
        size_hint: (.9, .1)
        pos_hint: {'center_x': .5, 'center_y': .8}
        on_press: root.manager.current = 'cechenia'
        background_color: [1, 1, 1, 100]
        background_normal: 'button.png'
        font_size: 60
        color: [0, 0, 1, 1]
    Button:
        text: 'Контур заземления'
        size_hint: (.9, .1)
        pos_hint: {'center_x': .5, 'center_y': .6}
        on_press: root.manager.current = 'zemle'
        background_color: [1, 1, 1, 100]
        background_normal: 'button.png'
        font_size: 60
        color: [0, 0, 1, 1]
        
<Zemle>:

    Button:
        background_color: [0, 0, 1, 100]
        background_normal:  ''
        height: dp(110)
        size_hint_y: None
        pos_hint: {'center_x': .5, 'center_y': .97}
    Label:
        id: title
        text: 'Контур заземления'
        font_size: 80
        pos_hint: {'center_x': .5, 'center_y': .95}
        color: [1,1,1,1]
    Button:
        text: '<'
        background_color: [0, 0, 1, 100]
        background_normal: ''
        font_size: 90
        color: [1, 1, 1, 1]
        font_name: "DejaVuSans.ttf"
        size_hint: (.1, .1)
        pos_hint: {'center_x': .05, 'center_y': .95}
        on_press: root.manager.current = 'addinfo'
    Image:

        source: 'zemle.jpeg'
        pos_hint: {'center_x': .5, 'center_y': .45}
        allow_stretch : True
        keep_ratio: False
        size_hint_x:.9
        size_hint_y:.85
        
<Cechenia>:

    Button:
        background_color: [0, 0, 1, 100]
        background_normal:  ''
        height: dp(110)
        size_hint_y: None
        pos_hint: {'center_x': .5, 'center_y': .97}
    Label:
        id: title
        text: 'Сечение кабеля'
        font_size: 80
        pos_hint: {'center_x': .5, 'center_y': .95}
        color: [1,1,1,1]
    Button:
        text: '<'
        background_color: [0, 0, 1, 100]
        background_normal: ''
        font_size: 90
        color: [1, 1, 1, 1]
        font_name: "DejaVuSans.ttf"
        size_hint: (.1, .1)
        pos_hint: {'center_x': .05, 'center_y': .95}
        on_press: root.manager.current = 'addinfo'
    Image:

        source: 'cechenia.jpg'
        pos_hint: {'center_x': .5, 'center_y': .45}
        allow_stretch : True
        keep_ratio: False
        size_hint_x:.9
        size_hint_y:.85
        
<Settings>:
    canvas:
        Color:
            rgba: 1, 1, 1, 1    # Blue
  
        # size and position of Canvas
        Rectangle:
            pos: self.pos
            size: self.size
    Button:
        background_color: [0, 0, 1, 100]
        background_normal:  ''
        height: dp(110)
        size_hint_y: None
        pos_hint: {'center_x': .5, 'center_y': .97}
    Label:
        id: title
        text: 'Настройки'
        font_size: 80
        pos_hint: {'center_x': .5, 'center_y': .95}
        color: [1,1,1,1]
    Button:
        id: back1
        text: '≡'
        background_color: [0, 0, 1, 100]
        background_normal: ''
        font_size: 90
        color: [1, 1, 1, 1]
        font_name: "DejaVuSans.ttf"
        size_hint: (.1, .1)
        pos_hint: {'center_x': .05, 'center_y': .95}
    Button:
        id: add
        text: '+'
        background_color: [0, 0, 1, 100]
        background_normal: ''
        font_size: 90
        color: [1, 1, 1, 1]
        size_hint: (.1, .1)
        pos_hint: {'center_x': .95, 'center_y': .95}


""")


    class Zemle(Screen):
        pass


    class Cechenia(Screen):
        pass


    class CustomLayout(RelativeLayout):

        def __init__(self, col, list_work, col_work_list, len_list, cost_list, sum_list, sum_all, **kwargs):
            super(CustomLayout, self).__init__(**kwargs)

            if col == 0:
                text = '№'
            else:
                text = col
            with self.canvas:
                Color(0, 0, 0, 1)
                self.rect = Line(width=2.,
                                 rectangle=(Window.size[0] * .005, self.pos[1], Window.size[0] * .99, self.height))
                self.rect = Line(width=2.,
                                 points=(Window.size[0] * 0.055, self.pos[1], Window.size[0] * 0.055, self.height))
                self.rect = Line(width=2.,
                                 points=(Window.size[0] * 0.5, self.pos[1], Window.size[0] * 0.5, self.height))
                self.rect = Line(width=2.,
                                 points=(Window.size[0] * 0.62, self.pos[1], Window.size[0] * 0.62, self.height))
                self.rect = Line(width=2.,
                                 points=(Window.size[0] * 0.67, self.pos[1], Window.size[0] * 0.67, self.height))
                self.rect = Line(width=2.,
                                 points=(Window.size[0] * 0.76, self.pos[1], Window.size[0] * 0.76, self.height))
                label_col = Label(pos=(-(Window.size[0] * .47), 0), text=str(text), color=(0, 0, 0, 1), font_size=30)
                label_col_work = Label(pos=((Window.size[0] * .06), 0), text=str(col_work_list), font_size=30,
                                       color=(0, 0, 0, 1))
                len_list_work = Label(pos=((Window.size[0] * .145), 0), text=str(len_list), font_size=30,
                                      color=(0, 0, 0, 1))
                self.add_widget(len_list_work)
                sum_list_work = Label(pos=((Window.size[0] * .38), 0), text=str(sum_list), font_size=30,
                                      color=(0, 0, 0, 1))
                self.add_widget(sum_list_work)
                cost_list_work = Label(pos=((Window.size[0] * .215), 0), text=str(cost_list), font_size=30,
                                       color=(0, 0, 0, 1))
                self.add_widget(cost_list_work)
                self.add_widget(label_col_work)
                self.add_widget(label_col)
                if len(str(list_work)) <= 40:
                    label_col = Label(pos=(-(Window.size[0] * .21), 0), font_size=30, text=str(list_work),
                                      color=(0, 0, 0, 1))
                    self.add_widget(label_col)
                else:
                    text = str(list_work)[:36] + '\n' + str(list_work)[36:]
                    label_col = Label(pos=(-(Window.size[0] * .21), 0), font_size=21, text=text, color=(0, 0, 0, 1))
                    self.add_widget(label_col)


    class FullApp(Screen):
        lable1 = ObjectProperty(None)
        lable2 = ObjectProperty(None)
        lable3 = ObjectProperty(None)
        lable4 = ObjectProperty(None)
        lable5 = ObjectProperty(None)
        checkbox1 = ObjectProperty(None)
        checkbox2 = ObjectProperty(None)

        def __init__(self, info=None, **kw):
            super().__init__(**kw)
            self.windows_app = 'main'
            self.windows = Window.size
            self.remove = 'save'
            list_list = [['кирпич', 'бетон', 'кирпич/бетон'], ['накладные', 'встроенные', 'накладные/встроенные'],
                         ['накладные', 'встроенные', 'накладные/встроенные'], ['220', '380', '220/380']]
            dropdown1 = DropDown()
            for index in list_list[0]:
                btn = Button(text=f'{index}', size_hint_y=None, height=80)
                btn.bind(on_release=lambda btn: dropdown1.select(btn.text))
                dropdown1.add_widget(btn)
            self.mainbutton = Button(color=(0, 0, 1, 1),
                                     background_color=[1, 1, 1, 100],
                                     background_normal='', text=f'{list_list[0][2]}',
                                     pos_hint={'center_x': .65, 'center_y': .32}, size_hint=(.5, .03))

            self.add_widget(self.mainbutton)
            self.mainbutton.bind(on_release=dropdown1.open)

            dropdown1.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))
            dropdown2 = DropDown()
            for index in list_list[1]:
                btn = Button(text=f'{index}', size_hint_y=None, height=80)
                btn.bind(on_release=lambda btn: dropdown2.select(btn.text))
                dropdown2.add_widget(btn)
            self.mainbutton1 = Button(color=(0, 0, 1, 1),
                                      background_color=[1, 1, 1, 100],
                                      background_normal='', text=f'{list_list[1][2]}',
                                      pos_hint={'center_x': .65, 'center_y': .28}, size_hint=(.5, .03))

            self.add_widget(self.mainbutton1)
            self.mainbutton1.bind(on_release=dropdown2.open)

            dropdown2.bind(on_select=lambda instance, x: setattr(self.mainbutton1, 'text', x))
            dropdown3 = DropDown()
            for index in list_list[2]:
                btn = Button(text=f'{index}', size_hint_y=None, height=80)
                btn.bind(on_release=lambda btn: dropdown3.select(btn.text))
                dropdown3.add_widget(btn)
            self.mainbutton2 = Button(color=(0, 0, 1, 1),
                                      background_color=[1, 1, 1, 100],
                                      background_normal='', text=f'{list_list[2][2]}',
                                      pos_hint={'center_x': .65, 'center_y': .24}, size_hint=(.5, .03))
            self.add_widget(self.mainbutton2)
            self.mainbutton2.bind(on_release=dropdown3.open)

            dropdown3.bind(on_select=lambda instance, x: setattr(self.mainbutton2, 'text', x))
            dropdown4 = DropDown()
            for index in list_list[3]:
                btn = Button(text=f'{index}', size_hint_y=None, height=80)
                btn.bind(on_release=lambda btn: dropdown4.select(btn.text))
                dropdown4.add_widget(btn)
            self.mainbutton3 = Button(color=(0, 0, 1, 1),
                                      background_color=[1, 1, 1, 100],
                                      background_normal='', text=f'{list_list[3][2]}',
                                      pos_hint={'center_x': .65, 'center_y': .20}, size_hint=(.5, .03))

            self.add_widget(self.mainbutton3)
            self.mainbutton3.bind(on_release=dropdown4.open)

            dropdown4.bind(on_select=lambda instance, x: setattr(self.mainbutton3, 'text', x))

            if info != None:
                self.remove = 'remove'
                conn = sqlite3.connect("mydatabase.db")
                sql = "SELECT rowid, * FROM projects WHERE rowid=?"
                cursor1 = conn.cursor()
                cursor1.execute(sql, (info,))
                info = cursor1.fetchall()[0]
                self.info = info
                self.func(info)

        def func(self, info):
            self.lable1.text = info[1]
            self.lable2.text = info[2]
            self.lable3.text = info[3]
            self.lable4.text = info[6]
            self.lable5.text = info[7]
            self.checkbox1.state = info[4]
            self.checkbox2.state = info[5]
            self.mainbutton.text = info[8]
            self.mainbutton1.text = info[9]
            self.mainbutton2.text = info[10]
            self.mainbutton3.text = info[11]
            self.sell = info[12]

        def func_error(self, address, name, number, error1, error2, error3, checkbox1, checkbox2, player, error4):
            errors = 0
            if address.text == '':
                error1.text = 'информация объязательна'
                errors = 1
            else:
                error1.text = ' '
            if name.text == '':
                error2.text = 'информация объязательна'
                errors = 1
            else:
                error2.text = ' '
            if number.text == '':
                error3.text = 'информация объязательна'
                errors = 1
            else:
                error3.text = ' '
            if player.text == '':
                error4.text = 'информация объязательна'
                errors = 1
            else:
                error4.text = ' '
            if errors == 0:
                conn = sqlite3.connect("mydatabase.db")
                if self.remove == 'save':
                    params = (address.text, name.text, number.text, checkbox1.state,
                              checkbox2.state, player.text, self.lable5.text,
                              self.mainbutton.text, self.mainbutton1.text, self.mainbutton2.text,
                              self.mainbutton3.text, 'с/0/%')
                    cursor = conn.cursor()

                    # Вставляем данные в таблицу
                    cursor.execute(f"""INSERT INTO projects
                                      VALUES ( ?, ?,
                                      ?,?,?,?,?,?,?,?,?,?)""", params)
                    conn.commit()
                    conn.close()

                    conn1 = sqlite3.connect("noworkdatabase.db")
                    cursor1 = conn1.cursor()
                    sql = "SELECT rowid, * FROM works"
                    cursor1.execute(sql)
                    l = cursor1.fetchall()
                    conn1 = sqlite3.connect("mydatabase.db")
                    cursor1 = conn1.cursor()
                    sql = f"SELECT rowid, * FROM projects WHERE address = '{address.text}'"
                    cursor1.execute(sql)
                    o = cursor1.fetchall()[0][0]
                    i = len(l)
                    strk = ''
                    for tuple_work in range(i):
                        strk += str(l[tuple_work][0]) + '*' + '0' + '-'
                    conn = sqlite3.connect("roomsdatabase.db")
                    cursor = conn.cursor()
                    params = ('avtomatika', o, strk, None)
                    cursor.execute(f"""INSERT INTO projects
                                                      VALUES ( ?, ?,
                                                      ?, ?)""", params)
                    conn.commit()
                elif self.remove == 'remove':
                    params = (address.text, name.text, number.text, checkbox1.state, checkbox2.state, player.text,
                              self.lable5.text,
                              self.mainbutton.text, self.mainbutton1.text, self.mainbutton2.text, self.mainbutton3.text,
                              self.sell)
                    conn = sqlite3.connect("mydatabase.db")
                    cursor = conn.cursor()

                    sql = f"""
                    UPDATE projects
                    SET address = ?, name = ?, number=?, whatsapp = ?, telegram = ?, player = ?, H =?, wall = ?, box = ?,
                    shit = ?, sety = ?, sell = ?
                    WHERE rowid = '{self.info[0]}'
                    """

                    cursor.execute(sql, params)
                    conn.commit()
                    conn = sqlite3.connect("roomsdatabase.db")
                    sql = "SELECT * FROM projects WHERE address=?"
                    cursor1 = conn.cursor()
                    cursor1.execute(sql, (self.info[0],))
                    i = cursor1.fetchall()
                    conn1 = sqlite3.connect("mydatabase.db")
                    cursor1 = conn1.cursor()
                    sql = f"SELECT rowid, * FROM projects WHERE rowid = '{self.info[0]}'"
                    cursor1.execute(sql)
                    o = cursor1.fetchall()[0][0]
                    conn1 = sqlite3.connect("roomsdatabase.db")
                    cursor1 = conn1.cursor()
                    for f in range(len(i)):
                        sql = f"""
                                            UPDATE projects
                                            SET address = ? 
                                            WHERE address = '{self.info[0]}' AND room = '{i[f][0]}'
                                            """

                        cursor1.execute(sql, (str(o),))
                        conn1.commit()
                sm.current = 'main'
                # main.open_info(address)


    class MainApp(Screen):
        add = ObjectProperty()
        back = ObjectProperty()

        def Back_click(self, window, key, *largs):

            if key == 27:
                if self.windows == '1':
                    self.list_button()
                if self.windows == '2':
                    conn = sqlite3.connect(self.mydatabase)
                    cursor = conn.cursor()
                    sql = "SELECT rowid, * FROM projects WHERE rowid=?"
                    cursor.execute(sql, (self.button_text,))
                    s = cursor.fetchall()
                    self.func_info(s)
                # you can create a method here to cache in a list the number of screens and then pop the last visited screen.
                return True

        def __init__(self, **kw):
            super().__init__(**kw)
            self.windows = 'full'
            Window.bind(on_keyboard=self.Back_click)
            self.mydatabase = 'mydatabase.db'
            self.noworkdatabase = 'noworkdatabase.db'
            self.workdatabase = 'workdatabase.db'
            self.roomsdatabase = 'roomsdatabase.db'

            self.button_add = Button(
                text='Добавить проект',
                background_color=[0, 0, 1, 100],
                background_normal='',
                font_size=80,
                color=[1, 1, 1, 1],
                size_hint=(1, .1),
                pos_hint={'center_x': .5, 'center_y': .05})
            self.title = self.ids.title
            self.add = self.ids.add
            self.back = self.ids.back
            self.sr = Screen(size_hint=(1, .85),
                             pos_hint={'center_x': .5, 'center_y': .55})
            self.add_widget(self.button_add)
            self.add_widget(self.sr)
            self.room_new = True

        def items_add_room(self,j):
            Material().items_add_room(self,j)

        def save_work(self, name_room):
            conn = sqlite3.connect(self.roomsdatabase)
            cursor = conn.cursor()
            strk = ''
            for key in self.keys_work:
                if self.keys_work[key].text == '':
                    self.keys_work[key].text = '0'
                    return
                for y in self.keys_work[key].text:
                    p = 0
                    for i in range(10):
                        if str(i) in y:
                            p = 1
                            break
                    if p == 0:
                        self.keys_work[key].text = '0'
                        return
                strk += str(key) + '*' + self.keys_work[key].text + '-'
            if name_room == 'avtomatika':
                sql = f"""
                UPDATE projects
                SET info = '{strk}'
                WHERE address = '{self.button_text}' AND rowid = '{self.button_room}'
                """
            else:
                sql = f"""
                                UPDATE projects
                                SET info2 = '{strk}'
                                WHERE address = '{self.button_text}' AND rowid = '{self.button_room}'
                                """

            cursor.execute(sql)
            conn.commit()
            self.sr.clear_widgets()
            conn = sqlite3.connect(self.mydatabase)
            cursor = conn.cursor()
            sql = "SELECT rowid, * FROM projects WHERE rowid=?"
            cursor.execute(sql, (self.button_text,))
            s = cursor.fetchall()
            if self.room_new == True:
                self.func_info(s)
            elif self.room_new == False:
                self.room_new = True
                self.add_room()

        def remove_name_room(self, button_name):
            layout = Screen()
            button_back = Button(text='Отмена', size_hint=(.5, .35), pos_hint={'center_x': .25, 'center_y': .25})
            input = TextInput(size_hint=(.9, .35), pos_hint={'center_x': .5, 'center_y': .65})
            button_save = Button(text='Сохранить', size_hint=(.5, .35), pos_hint={'center_x': .75, 'center_y': .25})
            self.popup = Popup(title='     Изменение ',
                               content=layout, size_hint=(.6, .2))

            def ok(*args):
                conn = sqlite3.connect(self.roomsdatabase)
                cursor = conn.cursor()
                strk = ''

                sql = f"""
                                        UPDATE projects
                                        SET room = '{input.text}'
                                        WHERE address = '{self.button_text}' AND rowid = '{button_name.text}'
                                        """

                cursor.execute(sql)
                conn.commit()
                self.sr.clear_widgets()
                conn = sqlite3.connect(self.mydatabase)
                cursor = conn.cursor()
                sql = "SELECT rowid, * FROM projects WHERE rowid=?"
                cursor.execute(sql, (self.button_text,))
                s = cursor.fetchall()
                self.popup.dismiss()
                self.func_info(s)

            layout.add_widget(input)
            button_back.bind(on_press=self.popup.dismiss)
            layout.add_widget(button_back)
            button_save.bind(on_press=lambda *args: ok())
            layout.add_widget(button_save)
            self.popup.open()

        def save_room(self, k):
            conn = sqlite3.connect(self.roomsdatabase)
            cursor = conn.cursor()
            params = (self.text_room.text, self.button_text, '', '')
            fk = cursor.execute(f"""INSERT INTO projects
                                  VALUES ( ?, ?,
                                  ?, ?)""", params)

            conn.commit()
            conn = sqlite3.connect(self.roomsdatabase)
            cursor = conn.cursor()
            sql = "SELECT rowid, * FROM projects WHERE room=? AND address=?"
            cursor.execute(sql, (self.text_room.text, self.button_text,))
            info = cursor.fetchall()[0]
            conn1 = sqlite3.connect(self.workdatabase)
            cursor1 = conn1.cursor()
            sql = "SELECT rowid, * FROM projects"
            cursor1.execute(sql)
            strk = ''
            lists = cursor1.fetchall()
            for tuple_work in lists:
                strk += str(tuple_work[0]) + '*' + '0' + '-'

            sql = f"""
                    UPDATE projects
                    SET info2 = '{strk}'
                    WHERE address = '{self.button_text}' AND room = '{self.text_room.text}'
                    """

            cursor.execute(sql)
            conn.commit()
            self.popup.dismiss()
            self.sroom.clear_widgets()
            self.pos_work(info[0], info[1])

        def pos_work(self, j, name_room):
            def i():
                conn = sqlite3.connect(self.mydatabase)
                cursor = conn.cursor()
                sql = "SELECT rowid, * FROM projects WHERE rowid=?"
                cursor.execute(sql, (self.button_text,))
                self.func_info(cursor.fetchall())

            self.back.text = '<'
            self.back.on_press = None
            self.back.on_press = i
            self.button_room = j

            def func_add():
                self.room_new = False
                self.save_work(self.button_room)

            self.add.on_press = func_add
            self.sr.clear_widgets()
            self.sr.size_hint = (1, .85)
            self.sr.pos_hint = {'center_x': .5, 'center_y': .55}
            self.title.text = name_room
            self.layout = GridLayout(cols=4, spacing=10, size_hint=(1, None),
                                     pos_hint={'center_x': .5, 'center_y': .5})
            self.layout.bind(minimum_height=self.layout.setter('height'))
            root = RecycleView(size_hint=(1, .9))
            root.add_widget(self.layout)
            conn = sqlite3.connect(self.mydatabase)
            cursor = conn.cursor()
            sql = "SELECT rowid, * FROM projects WHERE rowid=?"
            cursor.execute(sql, (self.button_text,))
            s = cursor.fetchall()
            sql = "SELECT rowid, * FROM projects WHERE rowid=? AND address=?"
            conn1 = sqlite3.connect(self.roomsdatabase)
            cursor1 = conn1.cursor()
            cursor1.execute(sql, (self.button_room, self.button_text,))
            information = cursor1.fetchall()[0]
            info = information[3]
            info2 = information[4]
            work_list = []
            col_work_list = []
            keys_move = {}
            self.keys_work = {}
            conn = sqlite3.connect(self.workdatabase)
            cursor = conn.cursor()
            cursor.execute(f"SELECT rowid, * FROM projects")
            info121 = cursor.fetchall()
            conn = sqlite3.connect(self.noworkdatabase)
            cursor = conn.cursor()
            cursor.execute(f"SELECT rowid, * FROM works")
            info131 = cursor.fetchall()
            strk = ''
            if name_room != 'avtomatika' and name_room != 'items':
                for i in range(len(info121)):
                    pil = 0
                    for info_btn in info2.split('-'):
                        if info121[i][0] != '' and str(info121[i][0]) == info_btn.split("*")[0]:
                            strk += str(info121[i][0]) + '*' + info_btn.split("*")[1] + '-'
                            pil = 1
                    if info121[i][0] != '' and pil == 0:
                        strk += str(info121[i][0]) + '*' + '0' + '-'
                sql = f"""
                                                UPDATE projects
                                                SET info2 = '{strk}'
                                                WHERE address = '{self.button_text}' AND rowid = '{self.button_room}'
                                                """
            if name_room == 'avtomatika':
                for i in range(len(info131)):
                    pil = 0
                    for info_btn in info.split('-'):
                        if info131[i][0] != '' and str(info131[i][0]) == info_btn.split("*")[0]:
                            strk += str(info131[i][0]) + '*' + info_btn.split("*")[1] + '-'
                            pil = 1

                    if info131[i][0] != '' and pil == 0:
                        strk += str(info131[i][0]) + '*' + '0' + '-'
                sql = f"""
                                                UPDATE projects
                                                SET info = '{strk}'
                                                WHERE address = '{self.button_text}' AND rowid = '{self.button_room}'
                                                """

            cursor1.execute(sql)
            conn1.commit()

            pi = -1
            sql = "SELECT rowid, * FROM projects WHERE rowid=? AND address=?"
            conn1 = sqlite3.connect(self.roomsdatabase)
            cursor1 = conn1.cursor()
            cursor1.execute(sql, (self.button_room, str(self.button_text),))
            information = cursor1.fetchall()[0]
            info = information[3]
            info2 = information[4]
            conn = sqlite3.connect(self.workdatabase)
            cursor = conn.cursor()
            cursor.execute(f"SELECT rowid, * FROM projects")
            info121 = cursor.fetchall()
            conn = sqlite3.connect(self.noworkdatabase)
            cursor = conn.cursor()
            cursor.execute(f"SELECT rowid, * FROM works")
            info131 = cursor.fetchall()
            if name_room != 'avtomatika':
                for info_btn in info2.split('-'):
                    pi += 1
                    if info_btn.split("*")[0] != '':
                        if info121[pi] != []:
                            for i in range(len(info121)):
                                if str(info121[i][0]) == info_btn.split("*")[0]:
                                    info12 = info121[i]
                                    p = True
                                    break
                                else:
                                    p = False
                                #     info12 = info121[i]
                            if p == True:

                                if info12[3] == 'Квартира' and s[0][4] == 'normal' and s[0][5] == 'down':
                                    continue
                                elif info12[3] == 'Дом' and s[0][5] == 'normal' and s[0][4] == 'down':
                                    continue
                                if info12[4] != 'None':
                                    if info12[4] in s[0][8]:
                                        text = info12[1]
                                    else:
                                        continue
                                if info12[5] != 'None':
                                    if info12[5] in s[0][9]:
                                        text = info12[1]
                                    else:
                                        continue
                                else:
                                    text = info12[1]
                        self.btn = Button(text=f'{text}',
                                          size_hint_y=None, size_hint_x=.7,
                                          height=dp(40),
                                          background_normal='button.png',
                                          font_size=40,
                                          color=[0, 0, 1, 1])

                        def move(button):
                            if button.text == '+':
                                keys_move[button].text = str(int(keys_move[button].text) + 1)
                                keys_move[button].background_color = (0, 0, 1, 0.1)
                            else:
                                if keys_move[button].text != '0':
                                    keys_move[button].text = str(int(keys_move[button].text) - 1)
                                    if keys_move[button].text == '0':
                                        keys_move[button].background_color = (1, 0, 0, 0.1)

                                else:
                                    keys_move[button].background_color = (1, 0, 0, 0.1)
                            return

                        self.plus = Button(text=f'+',
                                           size_hint_y=None, size_hint_x=.15,
                                           height=dp(40),
                                           background_normal='button.png',
                                           font_size=40,
                                           color=[0, 0, 1, 1],
                                           on_press=lambda *args: move(*args))
                        self.min = Button(text=f'-',
                                          size_hint_y=None, size_hint_x=.15,
                                          height=dp(40),
                                          background_normal='button.png',
                                          font_size=40,
                                          color=[0, 0, 1, 1],
                                          on_press=lambda *args: move(*args))
                        self.col_work = TextInput(
                            text=f'{info_btn.split("*")[1]}',
                            multiline=False,
                            height=dp(30),
                            pos_hint={'center_x': .5, 'center_y': .65},
                            size_hint_y=.3,
                            size_hint_x=.1,
                            foreground_color=(0, 0, 1, 1),
                            background_color=[0, 0, 1, 0.1],
                            background_normal='',
                            hint_text_color=(0, 0, 1, 1))
                        if self.col_work.text == '0':
                            self.col_work.background_color = (1, 0, 0, 0.1)
                        keys_move[self.plus] = self.col_work
                        keys_move[self.min] = self.col_work
                        self.keys_work[info12[0]] = self.col_work
                        self.layout.add_widget(self.btn)
                        self.layout.add_widget(self.plus)
                        self.layout.add_widget(self.col_work)
                        self.layout.add_widget(self.min)
                        work_list.append(info_btn.split("*")[0])
                        col_work_list.append(int(info_btn.split("*")[1]))

            if name_room == 'avtomatika':
                for info_btn in info.split('-'):
                    pi += 1
                    if info_btn.split("*")[0] != '':
                        for i in range(len(info131)):
                            if str(info131[i][0]) == info_btn.split("*")[0]:
                                info13 = info131[i]
                                p = True
                                break
                            else:
                                p = False
                        if p == True:
                            if info13[4] != 'None':
                                if info13[4] in s[0][11]:
                                    text = info13[1]
                                else:
                                    continue
                            if info13[5] != 'None':
                                if info13[5] in s[0][10]:
                                    text = info13[1]
                                else:
                                    continue
                            else:
                                text = info13[1]
                        else:
                            continue
                        self.btn = Button(text=f'{text}',
                                          size_hint_y=None, size_hint_x=.7,
                                          height=dp(40),
                                          background_normal='button.png',
                                          font_size=40,
                                          color=[0, 0, 1, 1])

                        def move(button):
                            if button.text == '+':
                                keys_move[button].text = str(int(keys_move[button].text) + 1)
                                keys_move[button].background_color = (0, 0, 1, 0.1)
                            else:
                                if keys_move[button].text != '0':
                                    keys_move[button].text = str(int(keys_move[button].text) - 1)
                                    if keys_move[button].text == '0':
                                        keys_move[button].background_color = (1, 0, 0, 0.1)

                                else:
                                    keys_move[button].background_color = (1, 0, 0, 0.1)
                            return

                        self.plus = Button(text=f'+',
                                           size_hint_y=None, size_hint_x=.15,
                                           height=dp(40),
                                           background_normal='button.png',
                                           font_size=40,
                                           color=[0, 0, 1, 1],
                                           on_press=lambda *args: move(*args))
                        self.min = Button(text=f'-',
                                          size_hint_y=None, size_hint_x=.15,
                                          height=dp(40),
                                          background_normal='button.png',
                                          font_size=40,
                                          color=[0, 0, 1, 1],
                                          on_press=lambda *args: move(*args))
                        self.col_work = TextInput(
                            text=f'{info_btn.split("*")[1]}',
                            multiline=False,
                            height=dp(30),
                            pos_hint={'center_x': .5, 'center_y': .65},
                            size_hint_y=.3,
                            size_hint_x=.1,
                            foreground_color=(0, 0, 1, 1),
                            background_color=[0, 0, 1, 0.1],
                            background_normal='',
                            hint_text_color=(0, 0, 1, 1))
                        if self.col_work.text == '0':
                            self.col_work.background_color = (1, 0, 0, 0.1)
                        keys_move[self.plus] = self.col_work
                        keys_move[self.min] = self.col_work
                        self.keys_work[info13[0]] = self.col_work
                        self.layout.add_widget(self.btn)
                        self.layout.add_widget(self.plus)
                        self.layout.add_widget(self.col_work)
                        self.layout.add_widget(self.min)
                        work_list.append(info_btn.split("*")[0])
                        col_work_list.append(int(info_btn.split("*")[1]))
            self.button_add.on_press = lambda: self.save_work(name_room)
            self.button_add.text = 'Сохранить'
            self.sr.add_widget(root)

            self.windows = '2'

        def open_info(self, button=0):
            if button != 0:
                self.button_text = button.text.split('.')[0]
            conn = sqlite3.connect(self.mydatabase)
            cursor = conn.cursor()
            sql = "SELECT rowid, * FROM projects WHERE rowid=?"
            cursor.execute(sql, (self.button_text,))
            self.func_info(cursor.fetchall())

        def add_room(self):
            layout = Screen()
            self.text_room = TextInput(size_hint=(.8, .3), pos_hint={'center_x': .5, 'center_y': .7})
            button_back = Button(text='Отмена', size_hint=(.5, .3), pos_hint={'center_x': .25, 'center_y': .25})
            button_save = Button(text='Сохранить', size_hint=(.5, .3), pos_hint={'center_x': .75, 'center_y': .25})
            layout.add_widget(self.text_room)
            self.popup = Popup(title='          Название Комнаты',
                               content=layout, size_hint=(.7, .25), pos_hint={'center_x': .5, 'center_y': .65})
            button_back.bind(on_press=self.popup.dismiss)
            layout.add_widget(button_back)
            button_save.bind(on_press=self.save_room)
            layout.add_widget(button_save)
            self.popup.open()

        def sell(self):
            conn = sqlite3.connect(self.mydatabase)
            cursor = conn.cursor()
            sql = "SELECT rowid, * FROM projects WHERE rowid=?"
            cursor.execute(sql, (self.button_text,))
            integer = cursor.fetchall()[0][12].split('/')
            layout = Screen()
            self.text_room = TextInput(text=f'{integer[1]}', size_hint=(.7, .15),
                                       pos_hint={'center_x': .35, 'center_y': .9})
            button_back = Button(text='Отмена', size_hint=(.5, .15), pos_hint={'center_x': .25, 'center_y': .1})
            button_save = Button(text='Сохранить', size_hint=(.5, .15), pos_hint={'center_x': .75, 'center_y': .1})
            layout.add_widget(self.text_room)
            info_list = [['руб.', '%'], ['Скидка', 'Наценка']]
            y_x = .65
            for i in info_list:
                label1 = Label(text=i[0], size_hint=(.25, .15), pos_hint={'center_x': .15, 'center_y': y_x})
                label2 = Label(text=i[1], size_hint=(.25, .15), pos_hint={'center_x': .65, 'center_y': y_x})
                layout.add_widget(label2)
                layout.add_widget(label1)
                y_x -= .15
            y_x = .725

            def check_1(a, b):
                if b.active == False and a.active == False:
                    a.active = True

            def check_2(a, b):
                if b.active == True and a.active == True:
                    b.active = False
                check_1(a, b)

            kir = CheckBox(active=False, size_hint=(.1, .1), pos_hint={'center_x': .35, 'center_y': .65},
                           on_press=lambda a: check_2(kir, but))
            but = CheckBox(active=False, size_hint=(.1, .1), pos_hint={'center_x': .85, 'center_y': .65},
                           on_press=lambda a: check_2(but, kir))
            vstr = CheckBox(active=False, size_hint=(.1, .1), pos_hint={'center_x': .35, 'center_y': .5},
                            on_press=lambda a: check_2(vstr, nakl))
            nakl = CheckBox(active=False, size_hint=(.1, .1), pos_hint={'center_x': .85, 'center_y': .5},
                            on_press=lambda a: check_2(nakl, vstr))
            layout.add_widget(kir)
            layout.add_widget(but)
            layout.add_widget(vstr)
            layout.add_widget(nakl)
            if integer[0] == 'с':
                vstr.active = True
            else:
                nakl.active = True
            if integer[2] == '%':
                but.active = True
            else:
                kir.active = True

            self.popup = Popup(title='          Скидка/Наценка',
                               content=layout, size_hint=(.8, .65), pos_hint={'center_x': .5, 'center_y': .65})
            button_back.bind(on_press=self.popup.dismiss)
            layout.add_widget(button_back)
            button_save.bind(on_press=lambda a: self.func_sell(a, kir, but, vstr, nakl))
            layout.add_widget(button_save)
            self.popup.open()

        def func_sell(self, button, b1, b2, b3, b4):
            text_info = self.text_room.text
            if b1.active == True:
                text_vid = 'руб.'
            else:
                text_vid = '%'
            if b3.active == True:
                text_mod = "с"
            else:
                text_mod = "н"

            conn = sqlite3.connect(self.mydatabase)
            cursor = conn.cursor()
            for y in text_info:
                p = 0
                for i in range(10):
                    if str(i) in y:
                        p = 1
                if '.' in y:
                    p=1
                if p == 0:
                    self.text_room.text = 'Введите числа'
                    return
            if text_info == '':
                text_info = '0'

            strk = text_mod + '/' + text_info + '/' + text_vid
            sql = f"""
                                            UPDATE projects
                                            SET sell = '{strk}'
                                            WHERE rowid = '{self.button_text}'
                                            """

            cursor.execute(sql)
            conn.commit()
            self.popup.dismiss()
            conn = sqlite3.connect(self.mydatabase)
            cursor = conn.cursor()
            sql = "SELECT rowid, * FROM projects WHERE rowid=?"
            cursor.execute(sql, (self.button_text,))

            self.func_info(cursor.fetchall())

        def remove_project(self):
            sm.current = 'full'
            sm.clear_widgets(sm.children[:1])
            sm.add_widget(FullApp(info=self.button_text, name='full'))
            sm.current = 'full'

        def func_info(self, info):

            from kivy.utils import platform
            if platform == "android":
                from android.permissions import request_permissions, Permission
                try:
                    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
                except Exception:
                    pass

            self.add.text = '+'
            self.add.background_color = [0, 0, 1]
            self.add.background_normal = ''
            self.add.font = 40

            def func():
                self.list_button()

            self.back.text = '<'
            self.back.on_press = func
            self.sr.clear_widgets()
            self.sr.pos_hint = {'center_x': .5, 'center_y': .55}

            canvas_paint = RelativeLayout(size_hint=(1, .1),
                                          pos_hint={'center_x': .575, 'center_y': .625})
            with canvas_paint.canvas:

                Color(0, 0, 0, 1)
                self.rect = Line(width=2.,
                                 rectangle=(0, Window.size[1] * .06, Window.size[0] * .95, Window.size[1] * .46))
            list_text = []
            self.sr.add_widget(canvas_paint)
            for i in [info[0][11], info[0][10], info[0][9], info[0][8], info[0][7], info[0][6], info[0][3], info[0][2],
                      info[0][1]]:
                list_text.append(i)
            self.player = info[0][6]
            self.name_project = list_text[8]
            list_name_1 = ["Материал стен:","Расп коробки:","Щит:", "Сеть:" ]
            list_name_2 = ["Адрес объекта:", "Имя клиента:",
                           "Номер:","Исполнитель:","Высота потолка:"]
            x = .1
            id_list =0
            list_text_info = list(reversed(list_text))

            self.layout = GridLayout(cols=2, spacing=40, size_hint=(.5, None),
                                     pos_hint={'center_x': .36, 'center_y':1.01})
            self.layout.bind(minimum_height=self.layout.setter('height'))
            self.sr.add_widget(self.layout)
            canvas_paint = RelativeLayout(size_hint=(1, .1),
                                          pos_hint={'center_x': .575, 'center_y': .625})
            with canvas_paint.canvas:

                Color(0, 0, 0, 1)
                self.rect = Line(width=2.,
                                 rectangle=(0, Window.size[1] * .32, Window.size[0] * .55, Window.size[1] * .20))
            with canvas_paint.canvas:

                Color(0, 0, 0, 1)
                self.rect = Line(width=2.,
                                 rectangle=(Window.size[0] * .55, Window.size[1] * .32, Window.size[0] * .95, Window.size[1] * .20))
            self.sr.add_widget(canvas_paint)
            for part in [list_name_2,list_name_1]:

                for i in range(0, len(part)):
                    if len(list_text_info[id_list]) > 13:
                        list_text_info[id_list] = list_text_info[id_list][:13]
                    args_name = Label(
                        text=f"{list_text_info[id_list]}",
                        font_size=33, size_hint=(1.0, 1.0), bold=True,
                        pos_hint={'center_x': .5, 'center_y': .5*1}, halign="left", valign="middle", color=[0, 0, 0, 1])
                    args_name.bind(size=args_name.setter('text_size'))
                    names = Label(
                        text=f"{part[i]}",
                        font_size=31, size_hint=(1.0, 1.0),
                        pos_hint={'center_x': .5, 'center_y': .5*i},
                        color=[0, 0, 0, 1])
                    names.bind(size=names.setter('text_size'))
                    self.layout.add_widget(names)
                    self.layout.add_widget(args_name)
                    id_list +=1

            button_delete = Button(text='Удалить',
                                   background_color=[.65, 0, 0, 1],
                                   background_normal='',
                                   font_size=40,
                                   color=[1, 1, 1, 1],
                                   size_hint=(.45, .05),
                                   pos_hint={'center_x': .3, 'center_y': .6},
                                   on_press=lambda x: self.delete_info(info), )
            button_remove = Button(text='Изменить',
                                   background_color=[.65, 0, 0, 1],
                                   background_normal='',
                                   font_size=40,
                                   color=[1, 1, 1, 1],
                                   size_hint=(.45, .05),
                                   pos_hint={'center_x': .8, 'center_y': .6},
                                   on_press=lambda *args: self.remove_project())
            self.sr.add_widget(button_remove)

            sql = f"SELECT rowid, * FROM name_group WHERE id ='2.2'"
            conn1 = sqlite3.connect('items.db')
            cursor1 = conn1.cursor()
            cursor1.execute(sql)
            info_group_list = cursor1.fetchall()[0]
            def okey_group(button):
                text_avto = button.text
                sql = f"SELECT rowid, * FROM tip_avto WHERE adress ='{str(self.button_text)}'"
                conn1 = sqlite3.connect(self.roomsdatabase)
                cursor1 = conn1.cursor()
                cursor1.execute(sql)
                if cursor1.fetchall() == []:
                    sql = f"""
                                        INSERT INTO tip_avto (adress,info)
                                        VALUES (?, ?);
                                        """

                    conn1 = sqlite3.connect(self.roomsdatabase)
                    cursor1 = conn1.cursor()
                    cursor1.execute(sql, (str(self.button_text),text_avto,))
                    conn1.commit()
                else:
                    sql = f"""
                                                UPDATE tip_avto
                                                SET info = '{text_avto}'
                                                WHERE adress = '{str(self.button_text)}'
                                                """

                    conn1 = sqlite3.connect(self.roomsdatabase)
                    cursor1 = conn1.cursor()
                    cursor1.execute(sql, )
                    conn1.commit()
            dropdown4 = DropDown()
            for index in info_group_list[3].split(','):
                if index == '':
                    continue
                sql = f"SELECT rowid, * FROM name_group WHERE id ='{index}'"
                conn1 = sqlite3.connect('items.db')
                cursor1 = conn1.cursor()
                cursor1.execute(sql)
                info_text = cursor1.fetchall()[0][2]
                btn = Button(text=f'{index} {info_text}', size_hint_y=None, height=80,
                                 on_press=lambda a: okey_group(a))
                btn.bind(on_release=lambda btn: dropdown4.select(btn.text))
                dropdown4.add_widget(btn)
            sql = f"SELECT rowid, * FROM tip_avto WHERE adress ='{str(self.button_text)}'"
            conn1 = sqlite3.connect(self.roomsdatabase)
            cursor1 = conn1.cursor()
            cursor1.execute(sql)
            piu = cursor1.fetchall()
            if piu == []:
                text_tip = '2.2.1 Автоматика ИЭК/EKF'
                sql = f"""
                                                        INSERT INTO tip_avto (adress,info)
                                                        VALUES (?, ?);
                                                        """

                conn1 = sqlite3.connect(self.roomsdatabase)
                cursor1 = conn1.cursor()
                cursor1.execute(sql, (str(self.button_text), text_tip ,))
                conn1.commit()
            else:
                text_tip = piu[0][2]
            self.mainbutton3 = Button(background_color=[0, 0, 1, 100],
                                 background_normal='',
                                 font_size=40,
                                 color=[1, 1, 1, 1], text=f'{text_tip}',
                                      size_hint=(.45, .05),
                                      pos_hint={'center_x': .8, 'center_y': .7},)

            self.sr.add_widget(self.mainbutton3)
            self.mainbutton3.bind(on_release=dropdown4.open)

            dropdown4.bind(on_select=lambda instance, x: setattr(self.mainbutton3, 'text', x))
            button_avto = Button(text='Автоматика',
                                 background_color=[0, 0, 1, 100],
                                 background_normal='',
                                 font_size=40,
                                 color=[1, 1, 1, 1],
                                 size_hint=(.45, .05),
                                 pos_hint={'center_x': .8, 'center_y': .8},
                                 on_press=lambda *args: x(0))
            self.sr.add_widget(button_avto)
            button_avto = Button(text='Материал',
                                 background_color=[0, 0, 1, 100],
                                 background_normal='',
                                 font_size=40,
                                 color=[1, 1, 1, 1],
                                 size_hint=(.45, .05),
                                 pos_hint={'center_x': .3, 'center_y': .8},
                                 on_press=lambda *args: x(1))
            self.sr.add_widget(button_avto)

            button_sell = Button(text='Скидка/Наценка',
                                 background_color=[0, 0, 1, 100],
                                 background_normal='',
                                 font_size=40,
                                 color=[1, 1, 1, 1],
                                 size_hint=(.45, .05),
                                 pos_hint={'center_x': .3, 'center_y': .7},
                                 on_press=lambda *args: self.sell())
            self.sr.add_widget(button_sell)

            def x(i):
                if i == 0:
                    conn = sqlite3.connect(self.roomsdatabase)
                    cursor1 = conn.cursor()
                    sql = "SELECT rowid, * FROM projects WHERE room=? AND address=? "
                    cursor1.execute(sql, ('avtomatika', self.button_text,))
                    p = cursor1.fetchall()
                    if p == []:
                        conn1 = sqlite3.connect("noworkdatabase.db")
                        cursor1 = conn1.cursor()
                        sql = "SELECT rowid, * FROM works"
                        cursor1.execute(sql)
                        l = cursor1.fetchall()
                        conn1 = sqlite3.connect("mydatabase.db")
                        cursor1 = conn1.cursor()
                        sql = f"SELECT rowid, * FROM projects WHERE rowid = '{self.button_text}'"
                        cursor1.execute(sql)
                        o = cursor1.fetchall()[0][0]
                        i = len(l)
                        strk = ''
                        for tuple_work in range(i):
                            strk += str(l[tuple_work][0]) + '*' + '0' + '-'
                        conn = sqlite3.connect("roomsdatabase.db")
                        cursor = conn.cursor()
                        params = ('avtomatika', o, strk, None)
                        cursor.execute(f"""INSERT INTO projects
                                                                              VALUES ( ?, ?,
                                                                              ?, ?)""", params)
                        conn.commit()
                    conn = sqlite3.connect(self.roomsdatabase)
                    cursor1 = conn.cursor()
                    sql = "SELECT rowid, * FROM projects WHERE room=? AND address=? "
                    cursor1.execute(sql, ('avtomatika', self.button_text,))
                    p = cursor1.fetchall()[0]
                    self.pos_work(p[0], p[1])
                elif i == 1:
                    Material.items_open_room(Material, self, self.button_text)

            button_total = Button(text='Сформировать',
                                  background_color=[0, 0, 1, 100],
                                  background_normal='',
                                  font_size=40,
                                  color=[1, 1, 1, 1],
                                  size_hint=(.35, .05),
                                  pos_hint={'center_x': .825, 'center_y': .945},
                                  on_press=lambda *args: self.format_excel())
            self.sr.add_widget(button_total)
            list_mg = []
            if info[0][5] == 'down':
                list_mg.append('Внешний')
            if info[0][4] == 'down':
                list_mg.append('Внутренний')
            if info[0][5] != 'down' and info[0][4] != 'down':
                list_mg.append('Внутренний')
                list_mg.append('Внешний')

            # text = "Монтаж:"
            # for i in list_mg:
            #     text = text + '\n' + i
            # mg = Label(
            #     text=text,
            #     font_size=35, bold=True,
            #     pos_hint={'center_x': .21, 'center_y': .675},
            #     color=[0, 0, 0, 1])
            # self.sr.add_widget(mg)
            list_work = []
            col_work_list = []
            cost_list = []
            sum_list = []
            sum_all_work = 0
            sum_all_items = 0
            sum_all = 0
            sql = "SELECT rowid, * FROM projects WHERE address=?"
            conn1 = sqlite3.connect(self.roomsdatabase)
            cursor1 = conn1.cursor()
            cursor1.execute(sql, (self.button_text,))
            info = cursor1.fetchall()
            sql = "SELECT rowid, * FROM projects"
            conn1 = sqlite3.connect(self.workdatabase)
            cursor1 = conn1.cursor()
            cursor1.execute(sql)
            sql = "SELECT rowid, * FROM works"
            conn2 = sqlite3.connect(self.noworkdatabase)
            cursor2 = conn2.cursor()
            cursor2.execute(sql)
            info1 = cursor1.fetchall()
            info2 = cursor2.fetchall()
            for y in info:
                for i in [3, 4]:
                    info_room = y[i]
                    if info_room != None:
                        if y[1] == 'avtomatika':
                            for info_btn in info_room.split('-'):
                                if info_btn.split("*")[0] != '':
                                    for i in range(len(info2)):

                                        if str(info2[i][0]) == info_btn.split("*")[0]:
                                            list_work.append(info2[i][1])
                                            col_work_list.append(int(info_btn.split("*")[1]))
                        else:
                            for info_btn in info_room.split('-'):
                                if info_btn.split("*")[0] != '':
                                    for i in range(len(info1)):
                                        if str(info1[i][0]) == info_btn.split("*")[0]:
                                            list_work.append(info1[i][1])
                                            col_work_list.append(int(info_btn.split("*")[1]))
            for i in range(len(list_work)):
                sql = "SELECT rowid, * FROM projects WHERE work=?"
                conn1 = sqlite3.connect(self.workdatabase)
                cursor1 = conn1.cursor()
                cursor1.execute(sql, (list_work[i],))
                sql = "SELECT rowid, * FROM works WHERE work=?"
                conn2 = sqlite3.connect(self.noworkdatabase)
                cursor2 = conn2.cursor()
                cursor2.execute(sql, (list_work[i],))
                info1 = cursor1.fetchall()
                info2 = cursor2.fetchall()
                if info1 != []:
                    cost_list.append(int(info1[0][2]))
                    sum_list.append(int(info1[0][2]) * col_work_list[i])
                    sum_all_work += int(info1[0][2]) * col_work_list[i]
                elif info2 != []:
                    cost_list.append(int(info2[0][3]))
                    sum_list.append(int(info2[0][3]) * col_work_list[i])
                    sum_all_work += int(info2[0][3]) * col_work_list[i]
            conn = sqlite3.connect(self.mydatabase)
            cursor = conn.cursor()
            sql = "SELECT rowid, * FROM projects WHERE rowid=?"
            cursor.execute(sql, (self.button_text,))
            integer = cursor.fetchall()[0][12].split('/')
            if integer[2] in 'руб.' and integer[0] == 'с':
                sum_all_work = sum_all_work - int(integer[1])
            elif integer[2] in '%' and integer[0] == 'с':
                sum_all_work -= sum_all_work * (int(integer[1]) / 100)
            elif integer[2] in 'руб.' and integer[0] != 'с':
                sum_all_work = sum_all_work + int(integer[1])
            elif integer[2] in '%' and integer[0] != 'с':
                sum_all_work = sum_all_work / ((100 - int(integer[1])) / 100)

            sql = "SELECT rowid, * FROM material WHERE address=?"
            conn1 = sqlite3.connect(self.roomsdatabase)
            cursor1 = conn1.cursor()
            cursor1.execute(sql, (str(self.button_text),))
            information_col_material = cursor1.fetchall()
            for info_item in information_col_material:
                conn = sqlite3.connect('items.db')
                cursor = conn.cursor()
                cursor.execute(f"SELECT rowid, * FROM albums WHERE ID=?",(int(info_item[1]),))
                info_material = cursor.fetchall()[0]
                sum_all_items += float(info_material[4]) * float(info_item[3])


            sum_all = sum_all_work+sum_all_items
            self.layout = GridLayout(cols=1, spacing=30, size_hint=(.5, None),
                                     pos_hint={'center_x': .86, 'center_y': 1.04})
            self.layout.bind(minimum_height=self.layout.setter('height'))
            self.sr.add_widget(self.layout)
            self.total = Label(
                text='Стоимость раб.:' + str(round(sum_all_work)),
                font_size=30,
                pos_hint={'center_x': .8, 'center_y': .85},
                color=[0, 0, 0, 1])
            self.total_items = Label(
                text='Стоимость мат.:' + str(round(sum_all_items)),
                font_size=30,
                pos_hint={'center_x': .8, 'center_y': .9},
                color=[0, 0, 0, 1])
            self.layout.add_widget(self.total_items)
            self.total_all = Label(
                text='Итого:' + str(round(sum_all)),
                font_size=30,
                pos_hint={'center_x': .8, 'center_y': .8},
                color=[0, 0, 0, 1], bold=True)
            self.layout.add_widget(self.total)
            self.layout.add_widget(self.total_all)
            self.title.text = 'Проект'
            self.sroom = Screen(size_hint=(1, .3),
                                pos_hint={'center_x': .65, 'center_y': .45}, )
            self.sr.size_hint = (1, 1)
            self.sr.pos_hint = {'center_x': .45, 'center_y': .3}
            self.add.text = '+'
            self.add.background_color = [0, 0, 255]
            self.add.color =(1,1,1)
            # self.add.background_normal = 'plus.png'
            self.add.on_press = lambda *args: self.add_room()
            self.button_add.on_press = lambda *args: self.add_room()
            self.button_add.text = 'Добавить комнату'
            self.sr.add_widget(button_delete)
            self.list_button_rooms()
            self.add.font_size = 60
            self.sr.add_widget(self.sroom)

        def delete_info(self, info):
            layout = Screen()
            button_back = Button(text='Нет', size_hint=(.5, .35), pos_hint={'center_x': .25, 'center_y': .25})
            button_save = Button(text='Да', size_hint=(.5, .35), pos_hint={'center_x': .75, 'center_y': .25})
            self.popup = Popup(title='     Вы точно хотите удалить?',
                               content=layout, size_hint=(.7, .2))

            def ok(*args):
                conn = sqlite3.connect(self.mydatabase)
                cursor = conn.cursor()
                sql = "DELETE FROM projects WHERE rowid = ?"
                cursor.execute(sql, (self.button_text,))
                conn.commit()
                conn = sqlite3.connect(self.roomsdatabase)
                cursor = conn.cursor()
                sql = "DELETE FROM projects WHERE address = ?"
                cursor.execute(sql, (self.button_text,))
                conn.commit()
                self.layout.clear_widgets()
                self.popup.dismiss()
                self.list_button()

            button_back.bind(on_press=self.popup.dismiss)
            layout.add_widget(button_back)
            button_save.bind(on_press=lambda *args: ok())
            layout.add_widget(button_save)
            self.popup.open()

        def list_button(self):
            from kivy.utils import platform
            if platform == "android":
                from android.permissions import request_permissions, Permission
                try:
                    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
                except Exception:
                    pass
            def func():
                sm.current = 'menu'

            self.back.text = '≡'
            self.back.on_press = func
            # self.add.text = ''
            # self.add.background_color = [255, 255, 255]
            # self.add.background_normal = 'plus.png'

            self.add.font_size = 60
            self.add.on_press = lambda *args: plus()

            def plus():
                sm.current = 'full'
                sm.clear_widgets(sm.children[:1])
                sm.add_widget(FullApp(name='full'))
                sm.current = 'full'

            self.title.text = 'Мои проекты'
            self.sr.clear_widgets()
            self.sr.size_hint = (1, .80)
            self.sr.pos_hint = {'center_x': .65, 'center_y': .55}
            self.button_add.text = 'Добавить проект'
            self.button_add.on_press = lambda *args: setattr(sm, 'current', "full")
            self.sr.pos_hint = {'center_x': .55, 'center_y': .55}
            self.layout = GridLayout(cols=1, spacing=40, size_hint=(.9, None),
                                     pos_hint={'center_x': .11, 'center_y': .5})
            self.layout.bind(minimum_height=self.layout.setter('height'))
            root = RecycleView(size_hint=(1, .9))
            root.add_widget(self.layout)
            self.sr.add_widget(root)
            conn = sqlite3.connect(self.mydatabase)  # или :memory: чтобы сохранить в RAM
            cursor = conn.cursor()
            for rows in cursor.execute("SELECT rowid, * FROM projects ORDER BY address"):
                self.btn = Button(text=f'{rows[0]}.{rows[1]}',
                                  size_hint_y=None, size_hint_x=.9,
                                  height=dp(50),
                                  background_normal='button.png',
                                  font_size=50, bold=True,
                                  color=[0, 0, 1, 1],
                                  on_press=self.open_info)
                self.layout.add_widget(self.btn)

        def list_button_rooms(self):

            self.add.font = 40
            self.sroom.clear_widgets()
            self.sroom.pos_hint = {'center_x': .575, 'center_y': .45}
            self.layout = GridLayout(cols=2, spacing=40, size_hint=(.95, None),
                                     pos_hint={'center_x': .65, 'center_y': .5})
            self.layout.bind(minimum_height=self.layout.setter('height'))
            self.root = RecycleView(size_hint=(1, .9))
            self.root.add_widget(self.layout)
            self.sroom.add_widget(self.root)
            conn = sqlite3.connect(self.roomsdatabase)  # или :memory: чтобы сохранить в RAM
            cursor = conn.cursor()
            for rows in cursor.execute("SELECT rowid, * FROM projects ORDER BY room"):
                if rows[2] == self.button_text:
                    if rows[1] != 'avtomatika':
                        self.btn_room = Button(text=f'{str(rows[0]) + "." + rows[1]}',
                                               pos_hint={'center_x': .65, 'center_y': .5},
                                               size_hint_y=None, size_hint_x=.6,
                                               height=dp(70),
                                               background_normal='button.png',
                                               font_size=60,
                                               color=[0, 0, 1, 1], bold=True,
                                               on_press=lambda a: self.pos_work(a.text.split('.')[0],
                                                                                a.text.split('.')[1]))

                        self.layout.add_widget(self.btn_room)
                        grid = GridLayout(cols=1, spacing=5, size_hint_x=.05)
                        self.del_room = Button(text=f'{rows[0]}',
                                               pos_hint={'center_x': .65, 'center_y': .5},
                                               size_hint_y=None, size_hint_x=.15,
                                               height=dp(32.5),
                                               background_normal='del1.png',
                                               color=[1, 1, 1, 0],
                                               on_press=lambda p: delete_info(p))
                        grid.add_widget(self.del_room)

                        self.remove_room = Button(text=f'{rows[0]}',
                                                  pos_hint={'center_x': .65, 'center_y': .5},
                                                  size_hint_y=None, size_hint_x=.15,
                                                  height=dp(32.5),
                                                  background_normal='img_140266.png',
                                                  color=[1, 1, 1, 0],
                                                  on_press=lambda p: self.remove_name_room(p))
                        grid.add_widget(self.remove_room)
                        self.layout.add_widget(grid)
            self.windows = '1'

            def delete_info(info):
                info = info.text
                layout = Screen()
                button_back = Button(text='Нет', size_hint=(.5, .35), pos_hint={'center_x': .25, 'center_y': .25})
                button_save = Button(text='Да', size_hint=(.5, .35), pos_hint={'center_x': .75, 'center_y': .25})
                self.popup = Popup(title='     Вы точно хотите удалить?',
                                   content=layout, size_hint=(.7, .2))

                def ok(*args):
                    conn = sqlite3.connect(self.roomsdatabase)
                    cursor2 = conn.cursor()
                    sql = "DELETE FROM projects WHERE rowid = ?"
                    cursor2.execute(sql, (info.split('.')[0],))
                    conn.commit()
                    conn = sqlite3.connect(self.mydatabase)
                    cursor1 = conn.cursor()
                    sql = "SELECT rowid, * FROM projects WHERE  rowid=?"
                    cursor1.execute(sql, (self.button_text,))
                    s = cursor1.fetchall()
                    self.layout.clear_widgets()
                    self.popup.dismiss()
                    self.func_info(s)

                button_back.bind(on_press=self.popup.dismiss)
                layout.add_widget(button_back)
                button_save.bind(on_press=lambda *args: ok())
                layout.add_widget(button_save)
                self.popup.open()

        def pdf_file(self):
            data1 = sqlite3.connect(self.workdatabase)
            cur = data1.cursor()
            sql = "SELECT * FROM users"
            cur.execute(sql)
            id = cur.fetchall()[0][0]
            a = ['№']
            list_work = ['Услуги']
            col_work_list = ['Кол-во']
            cost_list = ["Цена"]
            len_list = ['Ед.']
            sum_list = ["Сумма"]
            for i in range(len(self.list_work) - 1):
                if int(self.col_work_list[i + 1]) > 0:
                    list_work.append(self.list_work[i + 1])
                    col_work_list.append(self.col_work_list[i + 1])
                    cost_list.append(self.cost_list[i + 1])
                    len_list.append(self.len_list[i + 1])
                    sum_list.append(self.sum_list[i + 1])
            for i in range(len(list_work)):
                a.append(i + 1)

            def simple_table(spacing=1.1):
                data = [['№', 'Услуги', 'Кол-во', 'Ед.', "Цена", "Сумма"]]
                conn = sqlite3.connect(self.mydatabase)
                cursor = conn.cursor()
                sql = "SELECT rowid, * FROM projects WHERE rowid=?"
                cursor.execute(sql, (self.button_text,))
                for i in range(len(list_work) - 1):
                    list_arg = [a[i + 1], list_work[i + 1], col_work_list[i + 1], len_list[i + 1], cost_list[i + 1],
                                sum_list[i + 1]]
                    data.append(list_arg)

                sell = cursor.fetchall()[0][12].split('/')

                data_group =[['№', 'Материал', 'Кол-во', 'Ед.', "Цена", "Сумма"]]
                conn = sqlite3.connect(self.roomsdatabase)
                cursor = conn.cursor()
                sql = "SELECT rowid, * FROM material WHERE address=?"
                cursor.execute(sql, (self.button_text,))
                conn0 = sqlite3.connect('items.db')
                cursor0 = conn0.cursor()
                l=1
                sum_items = 0
                for i in cursor.fetchall():
                    sql = "SELECT rowid, * FROM albums WHERE ID=?"
                    cursor0.execute(sql, (int(i[1]),))
                    text_item =cursor0.fetchall()[0]
                    list_arg = [l, text_item[2], i[3], text_item[3], text_item[4],
                                int(float(text_item[4])*int(i[3]))]
                    data_group.append(list_arg)
                    l+=1
                    sum_items += float(text_item[4])*int(i[3])


                i, y = 0, ''
                conn = sqlite3.connect(self.mydatabase)
                cursor = conn.cursor()
                sql = "SELECT rowid, * FROM projects WHERE rowid=?"
                cursor.execute(sql, (self.button_text,))
                info = cursor.fetchall()

                pdf = FPDF()
                pdf.add_page()

                pdf.add_font('Roboto', '', 'Roboto.ttf', uni=True)
                pdf.add_font('Roboto-Light', '', 'Roboto-Light.ttf', uni=True)
                pdf.add_font('Roboto-LightItalic', '', 'Roboto-LightItalic.ttf', uni=True)
                row_height = 3.5277777777777772
                pdf.set_font("Roboto", size=12)
                pdf.cell(200, 10,
                         txt=f'Сметный расчет № {f"{datetime.date.today()}"[0:4] + f"{datetime.date.today()}"[5:7] + f"{datetime.date.today()}"[8:10] + id} от {f"{datetime.date.today()}"[8:10] + "-" + f"{datetime.date.today()}"[5:7] + "-" + f"{datetime.date.today()}"[0:4] + "г."}',
                         ln=1, align="L")
                pdf.cell(200, 10, txt="", ln=1, align="L")

                pdf.set_line_width(1)
                pdf.line(10, 20, 199, 20)

                pdf.set_font("Roboto", size=8)
                pdf.cell(200, 10, txt=f"Заказчик: {info[0][2]}", ln=1, align="L")
                pdf.cell(200, 10, txt=f"Стройка (инж. система): {info[0][1]}", ln=1, align="L")

                r = -1
                pdf.set_line_width(.1)
                list_gr=[]
                for row in data_group:
                    if row[2] != '0':
                        list_gr.append(row)
                        if r <= -1:
                            y = 'Roboto'
                        else:
                            y = 'Roboto-Light'
                        pdf.set_font(f'{y}', '', 8)
                        pdf.cell(pdf.w * .04, row_height * spacing,
                                 txt=str(row[0]), border=1, align='C')
                        pdf.cell(pdf.w * .5, row_height * spacing,
                                 txt=row[1], border=1)
                        pdf.cell(pdf.w * .075, row_height * spacing,
                                 txt=str(row[2]), border=1, align="C")
                        pdf.cell(pdf.w * .04, row_height * spacing,
                                 txt=str(row[3]), border=1)
                        pdf.cell(pdf.w * .12, row_height * spacing,
                                 txt=str(row[4]), border=1, align="R")
                        pdf.cell(pdf.w * .125, row_height * spacing,
                                 txt=str(row[5]), border=1, align="R")
                        pdf.ln(row_height * spacing)
                        r += 1
                data_group = list_gr

                # pdf.set_line_width(.5)
                # pdf.rect(10, 50, 189, (row_height * spacing) * len(data_group))

                pdf.set_font("Roboto", size=10)
                pdf.cell(200, 5, txt=f"Итого материал: {int(sum_items)},00              ", ln=1, align="R")
                pdf.set_line_width(.005)

                pdf.set_line_width(.1)
                self.sum_all = 0
                for row in data:
                    if i <= 0:
                        y = 'Roboto'
                    else:
                        y = 'Roboto-Light'
                    pdf.set_font(f'{y}', '', 8)
                    pdf.cell(pdf.w * .04, row_height * spacing,
                             txt=str(row[0]), border=1, align='C')
                    pdf.cell(pdf.w * .5, row_height * spacing,
                             txt=row[1], border=1)
                    pdf.cell(pdf.w * .075, row_height * spacing,
                             txt=str(row[2]), border=1, align="C")
                    pdf.cell(pdf.w * .04, row_height * spacing,
                             txt=str(row[3]), border=1)
                    pdf.cell(pdf.w * .12, row_height * spacing,
                             txt=str(row[4]), border=1, align="R")
                    pdf.cell(pdf.w * .125, row_height * spacing,
                             txt=str(row[5]), border=1, align="R")
                    if row[5].isnumeric():
                        self.sum_all+=int(row[5])
                    pdf.ln(row_height * spacing)
                    i += 1
                # pdf.set_line_width(.5)
                # pdf.rect(10, 50 + ((row_height * spacing) * (len(data_group) + 1.25)), 189,
                #          (row_height * spacing) * len(data))
                i1 = 55
                i2 = 83
                pdf.set_font("Roboto", size=10)
                pdf.cell(200, 5, txt=f"Итого услуги: {self.sum_all},00              ", ln=1, align="R")
                if sell[1] != '0':
                    pdf.set_line_width(.005)
                    pdf.set_font("Roboto", size=10)
                    if sell[0] == 'с':
                        text = 'Скидка'
                    else:
                        text = 'Накл.расходы'
                    if sell[2] == '%' and sell[0] == 'с':
                        text_sell = self.sum_all * (float(sell[1]) / 100)
                    elif sell[2] == '%' and sell[0] != 'с':
                        text_sell = self.sum_all / ((100 - float(sell[1])) / 100) - self.sum_all
                    else:
                        text_sell = sell[1]
                    pdf.cell(200, 5, txt=f"{text}: {int(text_sell)},00 руб.             ", ln=1, align="R")
                    pdf.set_line_width(.005)
                    if sell[2] == '%' and sell[0] == 'с':
                        self.sum_all -= self.sum_all * (int(sell[1]) / 100)
                    elif sell[0] != 'с':
                        self.sum_all += int(text_sell)
                    else:
                        self.sum_all -= int(sell[1])
                    i1 += 10
                    i2 += 10
                    pdf.set_font("Roboto", size=10)
                    pdf.cell(200, 5, txt=f"Всего услуги: {round(self.sum_all)},00              ", ln=1, align="R")


                pdf.set_line_width(1)
                pdf.line(10, ((row_height * spacing) * (len(data)+len(data_group)+1.5)) + i1, 199, ((row_height * spacing) * (len(data)+len(data_group)+1.5)) + i1)

                pdf.set_font("Roboto", size=10)
                pdf.cell(200, 10, txt=f"Всего: {int(self.sum_all)+int(sum_items)},00             ", ln=1, align="R")
                pdf.set_font("Roboto-Light", size=10)
                pdf.cell(200, 10, txt=f"Всего наименований {(len(list_work) - 1)+int(r)}, на сумму {int(self.sum_all)+int(sum_items)},00 руб.",
                         ln=1,
                         align="L")

                pdf.set_font("Roboto-LightItalic", size=10)
                from num2t4ru import num2text
                male_units = ((u'рубль', u'рубля', u'рублей'), 'm')
                pdf.cell(200, 10, txt=f"({num2text(int(self.sum_all)+int(sum_items),male_units)})", ln=1, align="L")

                pdf.set_font("Roboto", size=10)
                pdf.cell(70, 10, txt="Исполнитель", align="L")
                pdf.set_font("Roboto-Light", size=10)
                pdf.cell(50, 10, txt=f"/{info[0][6]}/", align="L")
                pdf.set_line_width(.5)
                pdf.line(50, ((row_height * spacing) * (len(data)+len(data_group)+3)) + i2, 75, ((row_height * spacing) * (len(data)+len(data_group)+3)) + i2)
                sql = f"""
                                                        UPDATE users
                                                        SET userid = '{int(id) + 1}'
                                                        """
                cur.execute(sql)
                data1.commit()
                from kivy.utils import platform
                if platform == "android":
                    try:
                        pdf.output(
                            f'/storage/emulated/0/folder/{f"{datetime.date.today()}"[0:4] + f"{datetime.date.today()}"[5:7] + f"{datetime.date.today()}"[8:10] + id}.pdf')
                    except Exception:
                        pass
                pdf.output(
                    f'{f"{datetime.date.today()}"[0:4] + f"{datetime.date.today()}"[5:7] + f"{datetime.date.today()}"[8:10] + id}.pdf')

            simple_table()
            self.name_file = f'{f"{datetime.date.today()}"[0:4] + f"{datetime.date.today()}"[5:7] + f"{datetime.date.today()}"[8:10] + id}.pdf'
            return [
                f'{f"{datetime.date.today()}"[0:4] + f"{datetime.date.today()}"[5:7] + f"{datetime.date.today()}"[8:10] + id}.pdf']

        def send_mail(self, send_from, send_to, subject, message, files=[],
                      server="smtp.yandex.ru", port=465, username='', password='',
                      use_tls=True):
            msg = MIMEMultipart()
            msg['From'] = send_from
            msg['To'] = COMMASPACE.join(send_to)
            msg['Date'] = formatdate(localtime=True)
            msg['Subject'] = subject

            msg.attach(MIMEText(message))

            for path in files:
                part = MIMEBase('application', "octet-stream")
                with open(path, 'rb') as file:
                    part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition',
                                'attachment; filename="{}"'.format(Path(path).name))
                msg.attach(part)

            smtp = smtplib.SMTP(server, port)
            if use_tls:
                smtp.starttls()
            smtp.login(username, password)
            smtp.sendmail(send_from, send_to, msg.as_string())
            smtp.quit()

        def format_excel(self):
            try:
                self.add.text = ''
                self.add.background_color = [255, 255, 255]
                self.add.background_normal = 'nt-png.png'


                def i():
                    conn = sqlite3.connect(self.mydatabase)
                    cursor = conn.cursor()
                    sql = "SELECT rowid, * FROM projects WHERE rowid=?"
                    cursor.execute(sql, (self.button_text,))
                    self.func_info(cursor.fetchall())

                self.back.text = '<'
                self.back.on_press = None
                self.back.on_press = i
                list_work = []
                col_work_list = []
                cost_list = []
                len_list = []
                sum_list = []
                sum_all = 0
                sql = "SELECT * FROM projects WHERE address=?"
                conn1 = sqlite3.connect(self.roomsdatabase)
                cursor1 = conn1.cursor()
                cursor1.execute(sql, (self.button_text,))
                info = cursor1.fetchall()
                sql = "SELECT rowid, * FROM projects"
                conn1 = sqlite3.connect(self.workdatabase)
                cursor1 = conn1.cursor()
                cursor1.execute(sql)
                sql = "SELECT rowid, * FROM works"
                conn2 = sqlite3.connect(self.noworkdatabase)
                cursor2 = conn2.cursor()
                cursor2.execute(sql)
                info1 = cursor1.fetchall()
                info2 = cursor2.fetchall()
                for y in info:
                    for i in [2, 3]:
                        info_room = y[i]
                        if info_room != None:
                            if y[0] == 'avtomatika':
                                for info_btn in info_room.split('-'):
                                    if info_btn.split("*")[0] != '':
                                        for i in range(len(info2)):

                                            if str(info2[i][0]) == info_btn.split("*")[0]:
                                                list_work.append(info2[i][1])
                                                col_work_list.append(int(info_btn.split("*")[1]))
                            else:
                                for info_btn in info_room.split('-'):
                                    if info_btn.split("*")[0] != '':
                                        for i in range(len(info1)):
                                            if str(info1[i][0]) == info_btn.split("*")[0]:
                                                list_work.append(info1[i][1])
                                                col_work_list.append(int(info_btn.split("*")[1]))
                for i in range(len(list_work)):

                    sql = "SELECT * FROM projects WHERE work=?"
                    conn1 = sqlite3.connect(self.workdatabase)
                    cursor1 = conn1.cursor()
                    cursor1.execute(sql, (list_work[i],))
                    sql = "SELECT * FROM works WHERE work=?"
                    conn2 = sqlite3.connect(self.noworkdatabase)
                    cursor2 = conn2.cursor()
                    cursor2.execute(sql, (list_work[i],))
                    info1 = cursor1.fetchall()
                    info2 = cursor2.fetchall()
                    if info1 != []:
                        cost_list.append(int(info1[0][1]))
                        len_list.append(info1[0][5])
                        sum_list.append(int(info1[0][1]) * col_work_list[i])
                        sum_all += int(info1[0][1]) * col_work_list[i]
                    elif info2 != []:
                        cost_list.append(int(info2[0][2]))
                        len_list.append(info2[0][1])
                        sum_list.append(int(info2[0][2]) * col_work_list[i])
                        sum_all += int(info2[0][2]) * col_work_list[i]
                list_work = list_work[::-1]
                col_work_list = col_work_list[::-1]
                cost_list = cost_list[::-1]
                len_list = len_list[::-1]
                sum_list = sum_list[::-1]
                list_works = []
                col_work_lists = []
                len_lists = []
                cost_lists = []
                sum_lists = []
                for i in range(len(list_work) - 1, -1, -1):
                    list = []
                    col = 0
                    for a in range(len(list_work) - 1, -1, -1):
                        if list_work[i] in list_works:
                            continue
                        elif list_work[i] == list_work[a]:
                            list.append(a)
                    if list != []:
                        for a in list:
                            col += int(col_work_list[a])
                        sum = col * int(cost_list[list[0]])
                        list_works.append(list_work[list[0]])
                        col_work_lists.append(str(col))
                        len_lists.append(len_list[list[0]])
                        cost_lists.append(cost_list[list[0]])
                        sum_lists.append(str(sum))
                sql = "SELECT * FROM works"
                conn2 = sqlite3.connect(self.noworkdatabase)
                cursor2 = conn2.cursor()
                cursor2.execute(sql)
                p = cursor2.fetchall()
                list_works = list_works[len(p) - 1:] + list_works[:len(p) - 1]
                col_work_lists = col_work_lists[len(p) - 1:] + col_work_lists[:len(p) - 1]
                len_lists = len_lists[len(p) - 1:] + len_lists[:len(p) - 1]
                cost_lists = cost_lists[len(p) - 1:] + cost_lists[:len(p) - 1]
                sum_lists = sum_lists[len(p) - 1:] + sum_lists[:len(p) - 1]
                self.table(list_works, col_work_lists, len_lists, cost_lists, sum_lists, sum_all)
                self.windows = '2'

                def ok():
                    try:
                        notification.notify(message='Подождите', toast=True)
                        # self.send_mail('activelektro@gmail.com', 'aktiv-elektro@list.ru',
                        #                f'{self.name_project}', str(self.name_project),
                        #                self.pdf_file(),
                        #                username='activelektro@gmail.com', password='send2022')
                        self.pdf_file()
                        notification.notify(message='Готово', toast=True)
                        file = pathlib.Path(self.name_file)
                        file.unlink()
                    except Exception as ex:
                        if '[Errno 11001] getaddrinfo failed' in str(ex):
                            notification.notify(message='Ошибка', toast=True)
                            notification.notify(message='Отсутствует Wi-Fi', toast=True)
                        else:
                            self.send_mail('activelektro@gmail.com', 'aktiv-elektro@list.ru',
                                           f'{self.name_project}', str(self.name_project),
                                           self.pdf_file(),
                                           username='activelektro@gmail.com', password='Erik2412')

                self.add.on_press = ok
            except Exception as e:
                import traceback
                lb = Label(text=f'{traceback.format_exc()}', color=(0, 0, 0, 1))
                self.add_widget(lb)

        def func_input_data(self):

            def i():

                from kivy.utils import platform
                if platform == "android":
                    import os
                    if not os.path.isdir("/storage/emulated/0/folder"):
                        os.mkdir("/storage/emulated/0/folder")
                    import shutil

                    shutil.copyfile('mydatabase.db', '/storage/emulated/0/folder/mydatabase.db')
                    shutil.copyfile('noworkdatabase.db', '/storage/emulated/0/folder/noworkdatabase.db')
                    shutil.copyfile('workdatabase.db', '/storage/emulated/0/folder/workdatabase.db')
                    shutil.copyfile('roomsdatabase.db', '/storage/emulated/0/folder/roomsdatabase.db')
                    shutil.copyfile('items.xlsx', '/storage/emulated/0/folder/items.xlsx')

            self.popup.dismiss()
            i()
            layout = Screen()
            self.popup = Popup(title='     Готово',
                               content=layout, size_hint=(.5, .2), pos_hint={"center_x": .5, "center_y": .45})
            layout.add_widget(Button(text="Окей", size_hint=(1, .5), on_press=lambda a: self.popup.dismiss()))
            self.popup.open()

        def question(self):
            layout = Screen()
            self.popup = Popup(title='     Хотите сделать резервную копию?',
                               content=layout, size_hint=(.5, .2),
                               pos_hint={"center_x": .5, "center_y": .45})

            layout.add_widget(
                Button(text="Нет", size_hint=(.5, .5), on_press=lambda a: self.popup.dismiss(),
                       pos_hint={"center_x": .25}))
            layout.add_widget(
                Button(text="Да", size_hint=(.5, .5), on_press=lambda a: self.func_input_data(),
                       pos_hint={"center_x": .75}))
            self.popup.open()

        def table(self, list_work, col_work_list, len_list, cost_list, sum_list, sum_all):
            self.sroom.clear_widgets()
            self.sr.clear_widgets()
            self.button_add.on_press = lambda: None
            bi = Screen()
            with bi.canvas:
                Color(1, 1, 1, 1)
                l = Rectangle(pos=self.sr.pos,
                              size=(Window.size[0] * 2, Window.size[1] * .9))
            self.sr.add_widget(bi)
            self.sr.size_hint = (1, .90)
            self.sr.background = (0, 0, 1, 1)
            self.sr.background_normal = None
            self.sr.pos_hint = {'center_x': .5, 'center_y': .425}
            root = RecycleView(size_hint=(1, 1))
            self.list_work = list_work
            self.col_work_list = col_work_list
            self.len_list = len_list
            self.cost_list = cost_list
            self.sum_list = sum_list
            self.sum_all = sum_all
            self.list_work.insert(0, 'Услуги')
            self.col_work_list.insert(0, 'Кол-во')
            self.len_list.insert(0, 'Ед.')
            self.cost_list.insert(0, "Цена")
            self.sum_list.insert(0, "Сумма")
            self.layouts = GridLayout(cols=1, size_hint=(1, None),
                                      pos_hint={'center_x': .5, 'center_y': .5})
            d = 0
            for i in range(len(list_work)):
                if col_work_list[i] == 'Кол-во' or int(col_work_list[i]) <= 0:
                    pass
                else:
                    d += 1
            layout1 = RelativeLayout(height=100,
                                     size_hint_y=None, size_hint_x=Window.width)
            layout2 = RelativeLayout(height=100,
                                     size_hint_y=None, size_hint_x=Window.width)
            col_work_text = Label(text=f'Кол-во работ:{d}',
                                  color=(0, 0, 0, 1), pos_hint={'center_x': .75, 'center_y': .5},
                                  font_size=50)

            btn = Button(text=f'Материал',
                         size_hint_y=.45, size_hint_x=.5,
                         background_normal='button.png',
                         font_size=20,
                         pos_hint={'center_x': .25, 'center_y': -.5},
                         color=[0, 0, 1, 1],
                         on_press=lambda a: self.table_items())
            layout2.add_widget(btn)

            layout1.add_widget(col_work_text)
            conn = sqlite3.connect(self.mydatabase)
            cursor = conn.cursor()
            sql = "SELECT rowid, * FROM projects WHERE rowid=?"
            cursor.execute(sql, (self.button_text,))
            sell = cursor.fetchall()[0][12].split('/')
            if sell[1] != '0':
                if sell[0] == 'с':
                    text = 'Скидка'
                else:
                    text = 'Накл.расходы'
                player_text = Label(text=f'{text}:{sell[1]}{sell[2]}',
                                    color=(0, 0, 0, 1), pos_hint={'center_x': .5, 'center_y': .5},
                                    font_size=50,
                                    halign="left",
                                    valign="middle")
                player_text.bind(size=player_text.setter('text_size'))
                layout2.add_widget(player_text)

            total= Label(text=f'{self.total.text}',
                                  color=(0, 0, 0, 1), pos_hint={'center_x': .75, 'center_y': .5},
                                  font_size=50)
            layout2.add_widget(total)
            self.layouts.add_widget(layout2)
            self.layouts.add_widget(layout1)
            col = 0
            for i in range(len(self.list_work)):
                if self.col_work_list[i] == 'Кол-во' or int(self.col_work_list[i]) > 0:
                    SkillStat = CustomLayout(col=col, list_work=self.list_work[i], col_work_list=self.col_work_list[i],
                                             len_list=self.len_list[i],
                                             cost_list=self.cost_list[i], sum_list=self.sum_list[i],
                                             sum_all=self.sum_all, pos=(0, 0),
                                             height=100,
                                             size_hint_y=None, size_hint_x=Window.width)
                    self.layouts.add_widget(SkillStat)
                    col += 1

            total.pos_hint = {'center_x': .75, 'center_y': .5}
            self.layouts.bind(minimum_height=self.layouts.setter('height'))
            with root.canvas:
                Color(0, 0, 0, 1)
                i = Line(width=4, points=(Window.size[0] * .005, 0, Window.size[0] * .995, 0))
            root.add_widget(self.layouts)
            self.sr.add_widget(root)
            self.question()

        def table_items(self):
            self.sroom.clear_widgets()
            self.sr.clear_widgets()
            self.button_add.on_press = lambda: None
            bi = Screen()
            with bi.canvas:
                Color(1, 1, 1, 1)
                l = Rectangle(pos=self.sr.pos,
                              size=(Window.size[0] * 2, Window.size[1] * .9))
            self.sr.add_widget(bi)
            self.sr.size_hint = (1, .90)
            self.sr.background = (0, 0, 1, 1)
            self.sr.background_normal = None
            self.sr.pos_hint = {'center_x': .5, 'center_y': .425}
            root = RecycleView(size_hint=(1, 1))
            data_group = [['№', 'Материал', 'Кол-во', 'Ед.', "Цена", "Сумма"]]
            conn = sqlite3.connect(self.roomsdatabase)
            cursor = conn.cursor()
            sql = "SELECT rowid, * FROM material WHERE address=?"
            cursor.execute(sql, (self.button_text,))
            conn0 = sqlite3.connect('items.db')
            cursor0 = conn0.cursor()
            l = 1
            sum_items = 0
            for i in cursor.fetchall():
                sql = "SELECT rowid, * FROM albums WHERE ID=?"
                cursor0.execute(sql, (int(i[1]),))
                text_item = cursor0.fetchall()[0]
                list_arg = [l, text_item[2], i[3], text_item[3], text_item[4],
                            int(float(text_item[4]) * int(i[3]))]
                data_group.append(list_arg)
                l += 1
                sum_items += float(text_item[4]) * int(i[3])
            self.layouts = GridLayout(cols=1, size_hint=(1, None),
                                      pos_hint={'center_x': .5, 'center_y': .5})

            layout1 = RelativeLayout(height=100,
                                     size_hint_y=None, size_hint_x=Window.width)
            layout2 = RelativeLayout(height=100,
                                     size_hint_y=None, size_hint_x=Window.width)
            col_work_text = Label(text=f'Кол-во работ:{l}',
                                  color=(0, 0, 0, 1), pos_hint={'center_x': .75, 'center_y': .5},
                                  font_size=50)

            layout1.add_widget(col_work_text)

            total = Label(text=f'Стоимость мат.:{sum_items}',
                                  color=(0, 0, 0, 1), pos_hint={'center_x': .75, 'center_y': .5},
                                  font_size=50)

            layout2.add_widget(total)
            self.layouts.add_widget(layout2)
            self.layouts.add_widget(layout1)

            for info in data_group:
                SkillStat = CustomLayout(col=info[0], list_work=info[1], col_work_list=info[2],
                                         len_list=info[3],
                                         cost_list=info[4], sum_list=info[5],
                                         sum_all=self.sum_all, pos=(0, 0),
                                         height=100,
                                         size_hint_y=None, size_hint_x=Window.width)
                self.layouts.add_widget(SkillStat)
            self.total.pos_hint = {'center_x': .75, 'center_y': .5}
            self.layouts.bind(minimum_height=self.layouts.setter('height'))
            with root.canvas:
                Color(0, 0, 0, 1)
                i = Line(width=4, points=(Window.size[0] * .005, 0, Window.size[0] * .995, 0))
            root.add_widget(self.layouts)
            self.sr.add_widget(root)

        def on_enter(self, *args):
            self.list_button()


    class MenuApp(Screen):
        def __init__(self, **kw):
            super().__init__(**kw)

            def ok(r):
                sm.current = 'settings'

            button = Button(
                text='Настройки', size_hint=(1, .1),
                pos_hint={'center_x': .5, 'center_y': .55},
                background_color=[1, 1, 1, 100],
                on_press=ok,
                background_normal='button.png',
                font_size=60,
                color=[0, 0, 1, 1])
            self.add_widget(button)


    class Settings(Screen):

        def __init__(self, **kw):
            super().__init__(**kw)
            self.title = self.ids.title
            self.add = self.ids.add
            self.back1 = self.ids.back1
            self.sr = Screen(size_hint=(1, .85),
                             pos_hint={'center_x': .65, 'center_y': .55})
            self.add_widget(self.sr)
            self.back1.on_press = self.okey
            self.chouce()

        def okey(self, i=0):
            if self.back1.text != '<':
                sm.current = 'menu'
            if self.back1.text == '<':
                self.chouce()

        def items_svizka(self, selff, button, list_info_button, key_list, button_key):
            Material().items_svizka(selff, button, list_info_button, key_list, button_key)
            return

        def chouce(self, i=0):
            self.sr.size_hint = (1, .95)
            self.sr.pos_hint = {'center_x': .65, 'center_y': .55}
            self.add.text = ''
            self.back1.text = '≡'
            self.add.on_press = lambda: 1 + 1
            self.sr.clear_widgets()
            self.title.text = 'Настройки'
            self.title.font_size = 80

            self.work = Button(text=f'Редактор работ',
                               size_hint=(.9, .1),
                               pos_hint={'center_x': .35, 'center_y': .8},
                               background_normal='button.png',
                               font_size=40,
                               color=[0, 0, 1, 1],
                               on_press=lambda a: self.pos_work())

            self.avto = Button(text=f'Редактор автоматики',
                               size_hint=(.9, .1),
                               pos_hint={'center_x': .35, 'center_y': .65},
                               background_normal='button.png',
                               font_size=40,
                               color=[0, 0, 1, 1],
                               on_press=lambda a: self.pos_avto())

            self.items_button = Button(text=f'Редактор материала',
                                       size_hint=(.9, .1),
                                       pos_hint={'center_x': .35, 'center_y': .5},
                                       background_normal='button.png',
                                       font_size=40,
                                       color=[0, 0, 1, 1],
                                       on_press=lambda a: Material.open_group(a, selff=self, button_name=a.text))

            self.input_data = Button(text=f'Резервное копирование',
                                     size_hint=(.45, .05),
                                     pos_hint={'center_x': .1, 'center_y': .1},
                                     background_normal='button.png',
                                     font_size=40,
                                     color=[0, 0, 1, 1],
                                     on_press=lambda a: self.func_input_data())
            self.output_data = Button(text=f'Загрузка данных',
                                      size_hint=(.45, .05),
                                      pos_hint={'center_x': .6, 'center_y': .1},
                                      background_normal='button.png',
                                      font_size=40,
                                      color=[0, 0, 1, 1],
                                      on_press=lambda a: self.func_output_data())
            self.input_data_excel = Button(text=f'Загрузка материала',
                                           size_hint=(.45, .05),
                                           pos_hint={'center_x': .1, 'center_y': .01},
                                           background_normal='button.png',
                                           font_size=40,
                                           color=[0, 0, 1, 1],
                                           on_press=lambda a: Material().open_info_in_excel())

            self.output_data_excel = Button(text=f'Выгрузка материала',
                                            size_hint=(.45, .05),
                                            pos_hint={'center_x': .6, 'center_y': .01},
                                            background_normal='button.png',
                                            font_size=40,
                                            color=[0, 0, 1, 1],
                                            on_press=lambda a: Material().create_excel())
            for widget in [self.work,self.avto,self.items_button,self.input_data,self.output_data,self.input_data_excel,self.output_data_excel]:
                self.sr.add_widget(widget)

        def func_open_group(self, key_list, button_key):
            Material().items_open(self, button_key, key_list)

        def func_output_data(self):
            from kivy.utils import platform
            if platform == "android":
                import os
                if not os.path.isdir("/storage/emulated/0/folder"):
                    layout = Screen()
                    self.popup = Popup(title='Ошибка: Отсутствие  данных', content=layout, size_hint=(.5, .2),
                                       pos_hint={"center_x": .5, "center_y": .45})
                    layout.add_widget(Button(text="Окей", size_hint=(1, .5), on_press=lambda a: self.popup.dismiss()))
                    self.popup.open()
                else:
                    list_outfile = ['/storage/emulated/0/folder/mydatabase.db',
                                    '/storage/emulated/0/folder/noworkdatabase.db',
                                    '/storage/emulated/0/folder/workdatabase.db',
                                    '/storage/emulated/0/folder/roomsdatabase.db',
                                    '/storage/emulated/0/folder/items.db']
                    list_infile = ['mydatabase.db', 'noworkdatabase.db', 'workdatabase.db', 'roomsdatabase.db','items.db']
                    for i in range(len(list_infile)):
                            os.remove(os.path.join(list_infile[i]))
                            import shutil
                            shutil.copyfile(list_outfile[i], list_infile[i])
                    layout = Screen()
                    self.popup = Popup(title='     Готово',
                                       content=layout, size_hint=(.5, .2),
                                       pos_hint={"center_x": .5, "center_y": .45})
                    layout.add_widget(
                        Button(text="Окей", size_hint=(1, .5), on_press=lambda a: self.popup.dismiss()))
                    self.popup.open()

        def func_input_data(self):

            def i():

                from kivy.utils import platform
                if platform == "android":
                    import os
                    if not os.path.isdir("/storage/emulated/0/folder"):
                        os.mkdir("/storage/emulated/0/folder")
                    import shutil

                    shutil.copyfile('mydatabase.db', '/storage/emulated/0/folder/mydatabase.db')
                    shutil.copyfile('noworkdatabase.db', '/storage/emulated/0/folder/noworkdatabase.db')
                    shutil.copyfile('workdatabase.db', '/storage/emulated/0/folder/workdatabase.db')
                    shutil.copyfile('roomsdatabase.db', '/storage/emulated/0/folder/roomsdatabase.db')
                    shutil.copyfile('items.db', '/storage/emulated/0/folder/items.db')

            i()
            layout = Screen()
            self.popup = Popup(title='     Готово',
                               content=layout, size_hint=(.5, .2), pos_hint={"center_x": .5, "center_y": .45})
            layout.add_widget(Button(text="Окей", size_hint=(1, .5), on_press=lambda a: self.popup.dismiss()))
            self.popup.open()

        def pos_avto(self):
            self.back1.text = '<'
            self.back1.on_press = self.okey
            self.add.on_press = self.add_avto
            self.add.text = '+'
            self.sr.clear_widgets()
            self.sr.size_hint = (1, .95)
            self.sr.pos_hint = {'center_x': .5, 'center_y': .5}
            self.layout = GridLayout(cols=2, spacing=10, size_hint=(1, None),
                                     pos_hint={'center_x': .5, 'center_y': .5})
            self.layout.bind(minimum_height=self.layout.setter('height'))
            root = RecycleView(size_hint=(1, .9))
            root.add_widget(self.layout)
            sql = "SELECT * FROM works"
            conn1 = sqlite3.connect("noworkdatabase.db")
            cursor1 = conn1.cursor()
            cursor1.execute(sql)
            info = cursor1.fetchall()
            self.keys_move = {}
            i = 0
            for info_btn in info:
                text = info_btn[0]
                i += 1
                self.btn = Button(text=f'{i}.{text}',
                                  size_hint_y=None, size_hint_x=.85,
                                  height=dp(40),
                                  background_normal='button.png',
                                  font_size=40,
                                  color=[0, 0, 1, 1])
                self.layout.add_widget(self.btn)
                self.redact = Button(text=f'',
                                     size_hint_y=None, size_hint_x=.1,
                                     height=dp(40),
                                     background_normal='img_140266.png',
                                     font_size=40,
                                     color=[0, 0, 1, 1],
                                     on_press=lambda a: self.def_redact_avto(a))
                self.layout.add_widget(self.redact)
                self.keys_move.setdefault(self.redact, text)
            self.sr.add_widget(root)

        def add_avto(self):
            layout = Screen()
            conn = sqlite3.connect("noworkdatabase.db")
            cursor = conn.cursor()
            font = Window.size[0] * Window.size[1] * .000025
            self.popup = Popup(title='     Создание',
                               content=layout, size_hint=(.8, .6))
            button_back = Button(text='Отменить', size_hint=(.5, .2), pos_hint={'center_x': .25, 'center_y': .1},
                                 font_size=font)
            button_save = Button(text='Сохранить', size_hint=(.5, .2), pos_hint={'center_x': .75, 'center_y': .1},
                                 font_size=font)
            input_name = TextInput(text=f'', size_hint=(.65, .16),
                                   pos_hint={'center_x': .325, 'center_y': .85},
                                   font_size=font)
            input_cost = TextInput(text=f'{0}', size_hint=(.25, .065),
                                   pos_hint={'center_x': .85, 'center_y': .89},
                                   font_size=font)
            list_list = [['шт.', "м/п"]]
            dropdown1 = DropDown()
            for index in list_list[0]:
                btn = Button(text=f'{index}', size_hint_y=None, height=60, font_size=font)
                btn.bind(on_release=lambda btn: dropdown1.select(btn.text))
                dropdown1.add_widget(btn)
            self.mainbutton = Button(color=(0, 0, 0, 1),
                                     background_color=[1, 1, 1, 100],
                                     background_normal='', text=f'{list_list[0][0]}',
                                     pos_hint={'center_x': .85, 'center_y': .81}, size_hint=(.25, .065), font_size=font)

            layout.add_widget(self.mainbutton)
            self.mainbutton.bind(on_release=dropdown1.open)

            dropdown1.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))
            info_list = [['220', '380'], ['Встроенный', 'Накладной']]
            y_x = .65
            for i in info_list:
                label1 = Label(text=i[0], size_hint=(.25, .15), pos_hint={'center_x': .15, 'center_y': y_x},
                               font_size=font * .8)
                label2 = Label(text=i[1], size_hint=(.25, .15), pos_hint={'center_x': .65, 'center_y': y_x},
                               font_size=font * .8)
                layout.add_widget(label2)
                layout.add_widget(label1)
                y_x -= .15
            y_x = .725
            info_list = ['Сеть(необязательно)', 'Щит(необязательно)']
            for i in info_list:
                label1 = Label(text=i, size_hint=(.25, .15), pos_hint={'center_x': .5, 'center_y': y_x},
                               font_size=font * .6)
                layout.add_widget(label1)
                y_x -= .15

            def check_1(a, b):
                if b.active == False and a.active == False:
                    a.active = True

            def check_2(a, b):
                if b.active == True and a.active == True:
                    b.active = False

            kir = CheckBox(active=False, size_hint=(.1, .1), pos_hint={'center_x': .35, 'center_y': .65},
                           on_press=lambda a: check_2(kir, but))
            but = CheckBox(active=False, size_hint=(.1, .1), pos_hint={'center_x': .85, 'center_y': .65},
                           on_press=lambda a: check_2(but, kir))
            vstr = CheckBox(active=False, size_hint=(.1, .1), pos_hint={'center_x': .35, 'center_y': .5},
                            on_press=lambda a: check_2(vstr, nakl))
            nakl = CheckBox(active=False, size_hint=(.1, .1), pos_hint={'center_x': .85, 'center_y': .5},
                            on_press=lambda a: check_2(nakl, vstr))

            def ok_save(*args):
                place = []
                if kir.active == False and but.active == False:
                    place.append('None')
                elif kir.active == False and but.active == True:
                    place.append('380')
                elif kir.active == True and but.active == False:
                    place.append('220')
                if vstr.active == False and nakl.active == False:
                    place.append('None')
                elif vstr.active == False and nakl.active == True:
                    place.append('накл')
                elif vstr.active == True and nakl.active == False:
                    place.append('встр')

                sql = f"""
                                        INSERT INTO works (work,ed,cost,cet,shit)
                                        VALUES ('{input_name.text}','{self.mainbutton.text}', '{input_cost.text}', '{place[0]}', '{place[1]}');
                                        """
                cursor.execute(sql)
                conn.commit()
                self.popup.dismiss()
                self.pos_avto()

            button_back.bind(on_press=lambda *args: self.popup.dismiss())
            button_save.bind(on_press=lambda *args: ok_save())
            for widget in [button_back,button_save,input_name,input_cost,but,kir,vstr,nakl]:
                layout.add_widget(widget)
            self.popup.open()

        def def_redact_avto(self, y):
            layout = Screen()
            conn = sqlite3.connect("noworkdatabase.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM works WHERE work = '{self.keys_move[y]}'")
            info = cursor.fetchall()
            font = Window.size[0] * Window.size[1] * .000025
            self.popup = Popup(title='     Изменение',
                               content=layout, size_hint=(.8, .6))
            button_back = Button(text='Отменить', size_hint=(.34, .2), pos_hint={'center_x': .5, 'center_y': .1},
                                 font_size=font)
            button_back.bind(on_press=lambda *args: self.popup.dismiss())
            layout.add_widget(button_back)
            button_back = Button(text='Удалить', size_hint=(.34, .2), pos_hint={'center_x': .175, 'center_y': .1},
                                 font_size=font)
            button_save = Button(text='Сохранить', size_hint=(.34, .2), pos_hint={'center_x': .825, 'center_y': .1},
                                 font_size=font)
            input_name = TextInput(text=f'{self.keys_move[y]}', size_hint=(.65, .16),
                                   pos_hint={'center_x': .325, 'center_y': .85},
                                   font_size=font)
            input_cost = TextInput(text=f'{info[0][2]}', size_hint=(.25, .065),
                                   pos_hint={'center_x': .85, 'center_y': .89},
                                   font_size=font)
            list_list = [['шт.', "м/п"]]
            dropdown1 = DropDown()
            for index in list_list[0]:
                btn = Button(text=f'{index}', size_hint_y=None, height=60, font_size=font)
                btn.bind(on_release=lambda btn: dropdown1.select(btn.text))
                dropdown1.add_widget(btn)
            self.mainbutton = Button(color=(0, 0, 0, 1),
                                     background_color=[1, 1, 1, 100],
                                     background_normal='', text=f'{info[0][1]}',
                                     pos_hint={'center_x': .85, 'center_y': .81}, size_hint=(.25, .065), font_size=font)

            layout.add_widget(self.mainbutton)
            self.mainbutton.bind(on_release=dropdown1.open)

            dropdown1.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))
            info_list = [['220', '380'], ['Встроенный', 'Накладной']]
            y_x = .65
            for i in info_list:
                label1 = Label(text=i[0], size_hint=(.25, .15), pos_hint={'center_x': .15, 'center_y': y_x},
                               font_size=font * .8)
                label2 = Label(text=i[1], size_hint=(.25, .15), pos_hint={'center_x': .65, 'center_y': y_x},
                               font_size=font * .8)
                layout.add_widget(label2)
                layout.add_widget(label1)
                y_x -= .15
            y_x = .725
            info_list = ['Сеть(необязательно)', 'Щит(необязательно)']
            for i in info_list:
                label1 = Label(text=i, size_hint=(.25, .15), pos_hint={'center_x': .5, 'center_y': y_x},
                               font_size=font * .6)
                layout.add_widget(label1)
                y_x -= .15

            def check_1(a, b):
                if b.active == False and a.active == False:
                    a.active = True

            def check_2(a, b):
                if b.active == True and a.active == True:
                    b.active = False

            kir = CheckBox(active=False, size_hint=(.1, .1), pos_hint={'center_x': .35, 'center_y': .65},
                           on_press=lambda a: check_2(kir, but))
            but = CheckBox(active=False, size_hint=(.1, .1), pos_hint={'center_x': .85, 'center_y': .65},
                           on_press=lambda a: check_2(but, kir))
            vstr = CheckBox(active=False, size_hint=(.1, .1), pos_hint={'center_x': .35, 'center_y': .5},
                            on_press=lambda a: check_2(vstr, nakl))
            nakl = CheckBox(active=False, size_hint=(.1, .1), pos_hint={'center_x': .85, 'center_y': .5},
                            on_press=lambda a: check_2(nakl, vstr))

            if info[0][3] == '380':
                but.active = True
            elif info[0][3] == '220':
                kir.active = True
            if info[0][4] == 'Накл':
                nakl.active = True
            elif info[0][4] == 'Встр':
                vstr.active = True

            def ok_delete(*args):
                sql = "DELETE FROM works WHERE work = ?"
                cursor.execute(sql, (self.keys_move[y],))
                conn.commit()
                self.popup.dismiss()
                self.pos_avto()

            def ok_save(*args):
                place = []
                if kir.active == False and but.active == False:
                    place.append('None')
                elif kir.active == False and but.active == True:
                    place.append('380')
                elif kir.active == True and but.active == False:
                    place.append('220')
                if vstr.active == False and nakl.active == False:
                    place.append('None')
                elif vstr.active == False and nakl.active == True:
                    place.append('накл')
                elif vstr.active == True and nakl.active == False:
                    place.append('встр')
                sql = f"""
                                        UPDATE works
                                        SET work = '{input_name.text}', cost = '{input_cost.text}', ed = '{self.mainbutton.text}', cet = '{place[0]}', shit = '{place[1]}'
                                        WHERE work = '{self.keys_move[y]}'
                                        """
                cursor.execute(sql)
                conn.commit()
                self.popup.dismiss()
                self.pos_avto()

            button_back.bind(on_press=lambda *args: ok_delete())
            button_save.bind(on_press=lambda *args: ok_save())
            for widget in [button_back,button_save,input_name,input_cost,but,kir,vstr,nakl]:
                layout.add_widget(widget)
            self.popup.open()

        def pos_work(self):
            self.back1.text = '<'
            self.back1.on_press = self.okey
            self.add.on_press = self.add_work
            self.add.text = '+'
            self.sr.clear_widgets()
            self.sr.size_hint = (1, .95)
            self.sr.pos_hint = {'center_x': .5, 'center_y': .5}
            self.layout = GridLayout(cols=2, spacing=10, size_hint=(1, None),
                                     pos_hint={'center_x': .5, 'center_y': .5})
            self.layout.bind(minimum_height=self.layout.setter('height'))
            root = RecycleView(size_hint=(1, .9))
            root.add_widget(self.layout)
            sql = "SELECT * FROM projects"
            conn1 = sqlite3.connect("workdatabase.db")
            cursor1 = conn1.cursor()
            cursor1.execute(sql)
            info = cursor1.fetchall()
            self.keys_move = {}
            i = 0
            for info_btn in info:
                i += 1
                text = info_btn[0]
                self.btn = Button(text=f'{i}.{text}',
                                  size_hint_y=None, size_hint_x=.85,
                                  height=dp(40),
                                  background_normal='button.png',
                                  font_size=40,
                                  color=[0, 0, 1, 1])
                self.layout.add_widget(self.btn)
                self.redact = Button(text=f'',
                                     size_hint_y=None, size_hint_x=.1,
                                     height=dp(40),
                                     background_normal='img_140266.png',
                                     font_size=40,
                                     color=[0, 0, 1, 1],
                                     on_press=lambda a: self.def_redact(a))
                self.layout.add_widget(self.redact)
                self.keys_move.setdefault(self.redact, text)
            self.sr.add_widget(root)

        def add_work(self):
            layout = Screen()
            conn = sqlite3.connect("workdatabase.db")
            cursor = conn.cursor()
            font = Window.size[0] * Window.size[1] * .000025
            self.popup = Popup(title='     Создание',
                               content=layout, size_hint=(.8, .6))
            button_back = Button(text='Отменить', size_hint=(.5, .2), pos_hint={'center_x': .25, 'center_y': .1},
                                 font_size=font)
            button_save = Button(text='Сохранить', size_hint=(.5, .2), pos_hint={'center_x': .75, 'center_y': .1},
                                 font_size=font)
            input_name = TextInput(text=f'', size_hint=(.65, .16),
                                   pos_hint={'center_x': .325, 'center_y': .85},
                                   font_size=font)
            input_cost = TextInput(text=f'{0}', size_hint=(.25, .065),
                                   pos_hint={'center_x': .85, 'center_y': .89},
                                   font_size=font)
            list_list = [['шт.', "м/п"]]
            dropdown1 = DropDown()
            for index in list_list[0]:
                btn = Button(text=f'{index}', size_hint_y=None, height=60, font_size=font)
                btn.bind(on_release=lambda btn: dropdown1.select(btn.text))
                dropdown1.add_widget(btn)
            self.mainbutton = Button(color=(0, 0, 0, 1),
                                     background_color=[1, 1, 1, 100],
                                     background_normal='', text=f'{list_list[0][0]}',
                                     pos_hint={'center_x': .85, 'center_y': .81}, size_hint=(.25, .065), font_size=font)

            layout.add_widget(self.mainbutton)
            self.mainbutton.bind(on_release=dropdown1.open)

            dropdown1.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))
            info_list = [['Внешний', 'Внутренний'], ['Кирпич', 'Бетон'], ['Встроенный', 'Накладной']]
            y_x = .65
            for i in info_list:
                label1 = Label(text=i[0], size_hint=(.25, .15), pos_hint={'center_x': .15, 'center_y': y_x},
                               font_size=font * .8)
                label2 = Label(text=i[1], size_hint=(.25, .15), pos_hint={'center_x': .65, 'center_y': y_x},
                               font_size=font * .8)
                layout.add_widget(label2)
                layout.add_widget(label1)
                y_x -= .15
            y_x = .725
            info_list = ['Монтаж', 'Материал(необязательно)', 'Расп. коробки(необязательно)']
            for i in info_list:
                label1 = Label(text=i, size_hint=(.25, .15), pos_hint={'center_x': .5, 'center_y': y_x},
                               font_size=font * .6)
                layout.add_widget(label1)
                y_x -= .15

            def check_1(a, b):
                if b.active == False and a.active == False:
                    a.active = True

            def check_2(a, b):
                if b.active == True and a.active == True:
                    b.active = False

            home = CheckBox(active=True, size_hint=(.1, .1), pos_hint={'center_x': .35, 'center_y': .65},
                            on_press=lambda a: check_1(home, kvar))
            kvar = CheckBox(active=True, size_hint=(.1, .1), pos_hint={'center_x': .85, 'center_y': .65},
                            on_press=lambda a: check_1(kvar, home))
            kir = CheckBox(active=False, size_hint=(.1, .1), pos_hint={'center_x': .35, 'center_y': .5},
                           on_press=lambda a: check_2(kir, but))
            but = CheckBox(active=False, size_hint=(.1, .1), pos_hint={'center_x': .85, 'center_y': .5},
                           on_press=lambda a: check_2(but, kir))
            vstr = CheckBox(active=False, size_hint=(.1, .1), pos_hint={'center_x': .35, 'center_y': .35},
                            on_press=lambda a: check_2(vstr, nakl))
            nakl = CheckBox(active=False, size_hint=(.1, .1), pos_hint={'center_x': .85, 'center_y': .35},
                            on_press=lambda a: check_2(nakl, vstr))

            def ok_save(*args):
                place = []
                if home.active == True and kvar.active == True:
                    place.append('Дом/Квартира')
                elif home.active == False and kvar.active == True:
                    place.append('Квартира')
                elif home.active == True and kvar.active == False:
                    place.append('Дом')
                if kir.active == False and but.active == False:
                    place.append('None')
                elif kir.active == False and but.active == True:
                    place.append('Бетон')
                elif kir.active == True and but.active == False:
                    place.append('Кирпич')
                if vstr.active == False and nakl.active == False:
                    place.append('None')
                elif vstr.active == False and nakl.active == True:
                    place.append('Накл')
                elif vstr.active == True and nakl.active == False:
                    place.append('Встр')
                sql = f"""
                                        INSERT INTO projects (work, money, place, mater, korob,ed)
                                        VALUES ('{input_name.text}', '{input_cost.text}', '{place[0]}', '{place[1]}', '{place[2]}','{self.mainbutton.text}');
                                        """
                cursor.execute(sql)
                conn.commit()
                self.popup.dismiss()
                self.pos_work()

            button_back.bind(on_press=lambda *args: self.popup.dismiss())
            button_save.bind(on_press=lambda *args: ok_save())
            for widget in [button_back,button_save,input_name,input_cost,home,kvar,but,kir,vstr,nakl]:
                layout.add_widget(widget)
            self.popup.open()

        def def_redact(self, y):
            layout = Screen()
            conn = sqlite3.connect("workdatabase.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM projects WHERE work = '{self.keys_move[y]}'")
            info = cursor.fetchall()
            font = Window.size[0] * Window.size[1] * .000025
            self.popup = Popup(title='     Изменение',
                               content=layout, size_hint=(.8, .6))
            button_back = Button(text='Отменить', size_hint=(.34, .2), pos_hint={'center_x': .5, 'center_y': .1},
                                 font_size=font)
            button_back.bind(on_press=lambda *args: self.popup.dismiss())
            layout.add_widget(button_back)
            button_back = Button(text='Удалить', size_hint=(.34, .2), pos_hint={'center_x': .175, 'center_y': .1},
                                 font_size=font)
            button_save = Button(text='Сохранить', size_hint=(.34, .2), pos_hint={'center_x': .825, 'center_y': .1},
                                 font_size=font)
            input_name = TextInput(text=f'{self.keys_move[y]}', size_hint=(.65, .16),
                                   pos_hint={'center_x': .325, 'center_y': .85},
                                   font_size=font)
            input_cost = TextInput(text=f'{info[0][1]}', size_hint=(.25, .065),
                                   pos_hint={'center_x': .85, 'center_y': .89},
                                   font_size=font)
            list_list = [['шт.', "м/п"]]
            dropdown1 = DropDown()
            for index in list_list[0]:
                btn = Button(text=f'{index}', size_hint_y=None, height=60, font_size=font)
                btn.bind(on_release=lambda btn: dropdown1.select(btn.text))
                dropdown1.add_widget(btn)
            self.mainbutton = Button(color=(0, 0, 0, 1),
                                     background_color=[1, 1, 1, 100],
                                     background_normal='', text=f'{info[0][5]}',
                                     pos_hint={'center_x': .85, 'center_y': .81}, size_hint=(.25, .065), font_size=font)

            layout.add_widget(self.mainbutton)
            self.mainbutton.bind(on_release=dropdown1.open)

            dropdown1.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))
            info_list = [['Внешний', 'Внутренний'], ['Кирпич', 'Бетон'], ['Встроенный', 'Накладной']]
            y_x = .65
            for i in info_list:
                label1 = Label(text=i[0], size_hint=(.25, .15), pos_hint={'center_x': .15, 'center_y': y_x},
                               font_size=font * .8)
                label2 = Label(text=i[1], size_hint=(.25, .15), pos_hint={'center_x': .65, 'center_y': y_x},
                               font_size=font * .8)
                layout.add_widget(label2)
                layout.add_widget(label1)
                y_x -= .15
            y_x = .725
            info_list = ['Монтаж', 'Материал(необязательно)', 'Расп. коробки(необязательно)']
            for i in info_list:
                label1 = Label(text=i, size_hint=(.25, .15), pos_hint={'center_x': .5, 'center_y': y_x},
                               font_size=font * .6)
                layout.add_widget(label1)
                y_x -= .15

            def check_1(a, b):
                if b.active == False and a.active == False:
                    a.active = True

            def check_2(a, b):
                if b.active == True and a.active == True:
                    b.active = False

            home = CheckBox(active=True, size_hint=(.1, .1), pos_hint={'center_x': .35, 'center_y': .65},
                            on_press=lambda a: check_1(home, kvar))
            kvar = CheckBox(active=True, size_hint=(.1, .1), pos_hint={'center_x': .85, 'center_y': .65},
                            on_press=lambda a: check_1(kvar, home))
            kir = CheckBox(active=False, size_hint=(.1, .1), pos_hint={'center_x': .35, 'center_y': .5},
                           on_press=lambda a: check_2(kir, but))
            but = CheckBox(active=False, size_hint=(.1, .1), pos_hint={'center_x': .85, 'center_y': .5},
                           on_press=lambda a: check_2(but, kir))
            vstr = CheckBox(active=False, size_hint=(.1, .1), pos_hint={'center_x': .35, 'center_y': .35},
                            on_press=lambda a: check_2(vstr, nakl))
            nakl = CheckBox(active=False, size_hint=(.1, .1), pos_hint={'center_x': .85, 'center_y': .35},
                            on_press=lambda a: check_2(nakl, vstr))
            if info[0][2] == 'квартира':
                home.active = False
            elif info[0][2] == 'дом':
                kvar.active = False
            if info[0][3] == 'бетон':
                but.active = True
            elif info[0][3] == 'кирпич':
                kir.active = True
            if info[0][4] == 'накл':
                nakl.active = True
            elif info[0][4] == 'встр':
                vstr.active = True

            def ok_delete(*args):
                sql = "DELETE FROM projects WHERE work = ?"
                cursor.execute(sql, (self.keys_move[y],))
                conn.commit()
                self.popup.dismiss()
                self.pos_work()

            def ok_save(*args):
                place = []
                if home.active == True and kvar.active == True:
                    place.append('Дом/Квартира')
                elif home.active == False and kvar.active == True:
                    place.append('Квартира')
                elif home.active == True and kvar.active == False:
                    place.append('Дом')
                if kir.active == False and but.active == False:
                    place.append('None')
                elif kir.active == False and but.active == True:
                    place.append('бетон')
                elif kir.active == True and but.active == False:
                    place.append('кирпич')
                if vstr.active == False and nakl.active == False:
                    place.append('None')
                elif vstr.active == False and nakl.active == True:
                    place.append('накл')
                elif vstr.active == True and nakl.active == False:
                    place.append('встр')
                sql = f"""
                                        UPDATE projects
                                        SET work = '{input_name.text}', money = '{input_cost.text}', place = '{place[0]}', mater = '{place[1]}', korob = '{place[2]}', ed = '{self.mainbutton.text}'
                                        WHERE work = '{self.keys_move[y]}'
                                        """
                cursor.execute(sql)
                conn.commit()
                self.popup.dismiss()
                self.pos_work()

            button_back.bind(on_press=lambda *args: ok_delete())
            button_save.bind(on_press=lambda *args: ok_save())
            for widget in [button_back,button_save,input_name,input_cost,home,kvar,but,kir,vstr,nakl]:
                layout.add_widget(widget)
            self.popup.open()

        def update_list_group(self, button_name, key):
            Material().open_group(self, button_name=button_name)


    class Addinfo(Screen):
        pass


    main = MainApp(name='main')
    sm = ScreenManager()
    sm.add_widget(main)
    sm.add_widget(MenuApp(name='menu'))
    sm.add_widget(FullApp(name='full'))
    sm.add_widget(Addinfo(name='addinfo'))
    sm.add_widget(Zemle(name='zemle'))
    sm.add_widget(Cechenia(name='cechenia'))
    sm.add_widget(Settings(name='settings'))


    class SampleApp(App):
        def build(self):
            return (sm)


    if __name__ == "__main__":
        SampleApp().run()
except Exception as ex:

    class SampleApp(App):
        def build(self):
            t = TextInput(text=f'{traceback.format_exc()}', size_hint=(1, 1), pos_hint={'center_x': .5, 'center_y': .5})
            return t


    if __name__ == "__main__":
        app = SampleApp()
        app.run()