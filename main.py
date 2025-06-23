from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
import random 
import os

Window.clearcolor = (0.5, 0.5, 0.5, 1)  

class ClosablePopup(Popup):
    def __init__(self, title, message, **kwargs):
        super(ClosablePopup, self).__init__(**kwargs)
        self.title = title
        self.size_hint = (0.8, 0.4)
        
        content = BoxLayout(orientation='vertical')
        
        btn_close = Button(text='×', size_hint=(1, 0.2), font_size=24)
        btn_close.bind(on_press=self.dismiss)
        
        content.add_widget(Label(text=message, font_size=18))
        content.add_widget(btn_close)
        
        self.content = content

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        
        main_layout = BoxLayout(orientation='vertical')
        
        top_panel = BoxLayout(size_hint=(1, 0.1))
        btn_download = Button(text='Скачать index.html')
        btn_download.bind(on_press=self.download_html)
        top_panel.add_widget(btn_download)
        main_layout.add_widget(top_panel)
        
        content_row = BoxLayout(orientation='horizontal')
        
        options_panel = BoxLayout(orientation='vertical', size_hint=(0.2, 1))
        
        btn_settings = Button(text='Настройки')
        btn_settings.bind(on_press=self.show_settings)
        
        btn_data = Button(text='Данные')
        btn_data.bind(on_press=self.show_data)
        
        btn_creator = Button(text='Кто создал?')
        btn_creator.bind(on_press=self.show_creator)
        
        options_panel.add_widget(Label(text='Меню:'))
        options_panel.add_widget(btn_settings)
        options_panel.add_widget(btn_data)
        options_panel.add_widget(btn_creator)
        
        content_area = BoxLayout(orientation='vertical')
        
        self.changing_label = Label(text='Сосал?', font_size=40)
        content_area.add_widget(self.changing_label)
        
        btn_layout = BoxLayout(size_hint=(1, 0.2))
        
        btn_yes = Button(text='Да')
        btn_yes.bind(on_press=self.yes_pressed)
        
        btn_no = Button(text='Нет')
        btn_no.bind(on_press=self.no_pressed)
        
        btn_layout.add_widget(btn_yes)
        btn_layout.add_widget(btn_no)
        
        content_area.add_widget(btn_layout)
        
        content_row.add_widget(options_panel)
        content_row.add_widget(content_area)
        
        main_layout.add_widget(content_row)
        self.add_widget(main_layout)
        
        self.text_options = ['Сосал?', 'Натурал?']
        self.current_text = 0
        
        
        self.random_answers = [
            "ты натурал!",
            "ты не натурал!",
            "Определенно натурал!",
            "Ты сосал!",
            "Сосал! Попался!",
            "Ладно", 
            "100% не нутурал!",
            "Натуральный выбор!",
            "Не-натуральный ответ!",
            "Ты сделали натуральный выбор!",
            "Это был не натуральный ответ!",
            "Ты нутарул!",
            "Не-нутурул!"
        ]
        
        Clock.schedule_interval(self.change_text, 0.05)
    
    def get_random_answer(self):
        return random.choice(self.random_answers)
    
    def download_html(self, instance):
        html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prikol</title>
      <link rel="icon" type="image/png" href="favicon.png">
    <style>
        body {
            background-color: grey;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            width: 300px;
            padding: 30px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
            color: white;
            text-align: center;
            transition: all 0.3s ease;
        }
        .container:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
        }
        .title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
            min-height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .buttons {
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
        }
        button {
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        button:hover {
            transform: scale(1.05);
        }
        .yes-btn {
            background-color: #4CAF50;
            color: white;
        }
        .no-btn {
            background-color: #f44336;
            color: white;
        }
        .ok-btn {
            background-color: #2196F3;
            color: white;
            display: none; 
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="title" id="question">Маму любишь?</div>
        <div class="buttons">
            <button class="no-btn" id="noBtn">Нет</button>
            <button class="yes-btn" id="yesBtn">Да</button>
            <button class="ok-btn" id="okBtn">Понял</button>
        </div>
    </div>

    <script>
        const question = document.getElementById("question");
        const noBtn = document.getElementById("noBtn");
        const yesBtn = document.getElementById("yesBtn");
        const okBtn = document.getElementById("okBtn");

       
        yesBtn.addEventListener("click", function() {
            question.textContent = "Сосал?";
        });

        noBtn.addEventListener("click", function() {
            question.textContent = "А ну ладно";
            okBtn.style.display = "block"; 
            noBtn.style.display = "none";   
            yesBtn.style.display = "none";  
        });

       
        okBtn.addEventListener("click", function() {
            question.textContent = "Маму любишь?";
            okBtn.style.display = "none";  
            noBtn.style.display = "block";  
            yesBtn.style.display = "block"; 
        });
    </script>
</body>
</html>
        """
        try:
            with open("index.html", "w", encoding="utf-8") as f:
                f.write(html_content)
            popup = ClosablePopup(title='Успех', 
                                message='Файл index.html успешно сохранён!')
        except Exception as e:
            popup = ClosablePopup(title='Ошибка', 
                                message=f'Не удалось сохранить файл: {str(e)}')
        popup.open()
    
    def change_text(self, dt):
        self.current_text = (self.current_text + 1) % len(self.text_options)
        self.changing_label.text = self.text_options[self.current_text]
    
    def yes_pressed(self, instance):
       
        answer = self.get_random_answer()
        popup = ClosablePopup(title='Результат', message=answer)
        popup.open()
    
    def no_pressed(self, instance):
        
        answer = self.get_random_answer()
        popup = ClosablePopup(title='Результат', message=answer)
        popup.open()
    
    def show_settings(self, instance):
        popup = ClosablePopup(title='Настройки',
                            message='Настройки не будэ')
        popup.open()
    
    def show_data(self, instance):
        popup = ClosablePopup(title='Данные',
                            message='Укка помой попу, или кырбыам. - Укка: Ол бу буолан бут')
        popup.open()
    
    def show_creator(self, instance):
        popup = ClosablePopup(title='Создатель',
                            message='Приложение создано Жорой')
        popup.open()

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm

print('РАБОТАЕТ, ЙОУ!')

if __name__ == '__main__':
    MyApp().run()