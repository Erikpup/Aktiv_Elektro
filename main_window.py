from kivy.uix.label import Label
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.textinput import TextInput
import sqlite3

class MainWindows(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.list_widget = ListWidget()
        self.dict_projects_id = {}
        self.toolbar = MDToolbar(
            title='Проекты',
            elevation=10)
        self.update_list_objects()

    def update_list_objects(self):
        self.clear_widgets()
        self.add_widget(self.toolbar)
        self.search_input = My_TextInput( hint_text='Поиск', multiline=False, size_hint=(1, 0.1))
        self.search_input.bind(text=self.search_object)
        self.add_widget(self.search_input)
        self.add_widget(self.list_widget)
        self.list_widget.widgets.clear_widgets()
        self.toolbar.left_action_items = [['menu', lambda x: print('x'), "Меню"]]
        self.toolbar.right_action_items = [['plus', lambda x: self.add_object_screen(), "Добавить проект"]]
        conn = sqlite3.connect('test.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM objects")
        list_objects = cur.fetchall()
        conn.close()
        for obj in list_objects:
            button = GridLayout(cols=1, spacing=10, size_hint_y=None)
            button.add_widget(Button(text=obj[1], on_press=self.open_object))
            self.dict_projects_id[button.children[0]] = obj[0]
            self.list_widget.widgets.add_widget(button)


    def add_object_screen(self):
        self.dict_info_add_object = {'TextField': {}, 'CheckBox': {}}
        self.clear_widgets([self.search_input])
        self.list_widget.widgets.clear_widgets()
        self.toolbar.right_action_items = []
        self.toolbar.left_action_items = []
        list_objects = ['Адрес объекта', 'Имя клиента', 'Номер телефона', 'Исполнитель', 'Высота потолка']
        for obj in list_objects:
            block = GridLayout(cols=1, size_hint_y=None, height=40)
            input_field = MDTextField(hint_text=obj)
            block.add_widget(input_field)
            self.dict_info_add_object['TextField'][obj] = input_field
            self.list_widget.widgets.add_widget(block)

        list_objects = [['Монтаж', 'Внутренний', 'Внешний'],
                        ['Материал стен', 'Бетон', 'Кирпич'],
                        ['Расп коробки', 'Накладные', 'Встроенные'],
                        ['Щит', 'Накладные', 'Встроенные'],
                        ['Сеть', '220V', '380V'], ]
        for obj in list_objects:
            self.list_widget.widgets.add_widget(Label(text=obj[0], color=(0, 0, 0, 1)))
            block = GridLayout(cols=2, size_hint_y=None)
            block.add_widget(Label(text=obj[1], color=(0, 0, 0, 1)))
            block.add_widget(Label(text=obj[2], color=(0, 0, 0, 1)))
            check_1 = MDCheckbox()
            check_2 = MDCheckbox()
            self.dict_info_add_object['CheckBox'][obj[0] + obj[1]] = check_1
            self.dict_info_add_object['CheckBox'][obj[0] + obj[2]] = check_2
            block.add_widget(check_1)
            block.add_widget(check_2)
            self.list_widget.widgets.add_widget(block)
        block = GridLayout(cols=2, spacing=1, size_hint_y=None)
        block.add_widget(Button(text='Сохранить', on_press=lambda x: self.save_add_object()))
        block.add_widget(Button(text='Отмена', on_press=lambda x: self.update_list_objects()))
        self.list_widget.widgets.add_widget(block)

    def save_add_object(self):
        conn = sqlite3.connect('test.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM objects")
        list_objects = cur.fetchall()
        list_objects_info = [list_objects[-1][0] + 1]
        for obj in self.dict_info_add_object['TextField'].keys():
            list_objects_info.append(self.dict_info_add_object['TextField'][obj].text)
        for obj in self.dict_info_add_object['CheckBox'].keys():
            if self.dict_info_add_object['CheckBox'][obj].state == 'down':
                list_objects_info.append(1)
            else:
                list_objects_info.append(0)
        cur.execute("INSERT INTO objects VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", list_objects_info)
        conn.commit()
        conn.close()
        self.update_list_objects()

    def search_object(self,ind,text):
        self.list_widget.widgets.clear_widgets()
        conn = sqlite3.connect('test.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM objects")
        list_objects = cur.fetchall()
        conn.close()
        for obj in list_objects:
            if text.lower() in obj[1].lower():
                button = GridLayout(cols=1, spacing=10, size_hint_y=None)
                button.add_widget(Button(text=obj[1]))
                self.dict_projects_id[button.children[0]] = obj[0]
                self.list_widget.widgets.add_widget(button)
    def open_object(self, id_obj):
        self.clear_widgets()
        self.add_widget(self.toolbar)
        self.toolbar.left_action_items = [['arrow-left', lambda x: self.update_list_objects()]]
        self.toolbar.right_action_items = [['plus', lambda x: self.add_object_screen()]]
        conn = sqlite3.connect('test.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM objects WHERE object_id = ?", (self.dict_projects_id[id_obj],))
        list_objects = cur.fetchall()
        conn.close()
        self.block_1 = GridLayout(cols=1, spacing=10)
        self.block_1.add_widget(InfoProjectWindow(cols=2, spacing=2,list_objects=list_objects))
        self.block_1.add_widget(ListButtonsProjects(cols=2, spacing=2,size_hint=(1, 0.1)))
        self.block = GridLayout(cols=1, spacing=10)
        self.block.add_widget(self.block_1)
        self.add_widget(self.block)

class My_TextInput(TextInput):
    pass

class ListWidget(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.widgets = GridLayout(cols=1, spacing=20, size_hint_y=None)
        self.widgets.bind(minimum_height=self.widgets.setter('height'))
        self.add_widget(self.widgets)

class InfoProjectWindow(GridLayout):
    def __init__(self,list_objects, **kwargs):
        super().__init__(**kwargs)
        self.list_objects = list(list_objects[0])
        list_objects = ['','Адрес объекта', 'Имя клиента', 'Номер телефона', 'Исполнитель', 'Высота потолка']
        for i in range(1,6):
            self.add_widget(Label(text=list_objects[i], color=(0, 0, 0, 1)))
            self.add_widget(Label(text=str(self.list_objects.pop(1)), color=(0, 0, 0, 1)))
        list_objects = [['Монтаж', 'Внутренний', 'Внешний'],
                        ['Материал стен', 'Бетон', 'Кирпич'],
                        ['Расп коробки', 'Накладные', 'Встроенные'],
                        ['Щит', 'Накладные', 'Встроенные'],
                        ['Сеть', '220V', '380V']]
        for i in range(len(list_objects)):
            self.add_widget(Label(text=list_objects[i][0], color=(0, 0, 0, 1)))
            text_info = ''
            for n in range(2):
                if self.list_objects.pop(1) == 1:
                    text_info += list_objects[i][n+1]+' '
            self.add_widget(Label(text=text_info, color=(0, 0, 0, 1)))

class ListButtonsProjects(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        list_buttons = ['Материал', 'Автоматика', 'Скидка/Наценка', 'Автоматика']
        for i in range(len(list_buttons)):
            self.add_widget(Button(text=list_buttons[i]))


