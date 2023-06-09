from flask import Flask  # импорт фласк из общего модуля фласка

app = Flask(__name__)  # создание приложения


# декорат, при входе на нашу страницу выдаёт пользователю привет мир
@app.route('/')
def main():
    # <h1> увеличивает размер букв до заголовка первого уровня <br>-переход на др стр
    return "<h1>Hello, world<h1><br><a href='/index'>перейти на страницу 2</a>"


# декорат, при входе на нашу страницу выдаёт пользователю привет мир
@app.route('/index/<x>/<y>')
def index(x, y):
    return f'Результат:{int(x) + int(y)}'


if __name__ == '__main__':  # вызов даст нам ссылку на страницу
    app.run()
