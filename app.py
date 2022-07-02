from flask import Flask, render_template, request, redirect, url_for
# from base import BaseUnit
from classes import unit_classes
from equipment import Equipment, EquipmentData

app = Flask(__name__)

# heroes = {
#     "player": BaseUnit,
#     "enemy": BaseUnit
# }

arena = ...  # TODO инициализируем класс арены


@app.route("/")
def menu_page():
    return render_template("index.html")


@app.route("/fight/")
def start_fight():
    # TODO выполняем функцию start_game экземпляра класса арена и передаем ему необходимые аргументы
    # TODO рендерим экран боя (шаблон fight.html)
    pass


@app.route("/fight/hit")
def hit():
    # TODO кнопка нанесения удара
    # TODO обновляем экран боя (нанесение удара) (шаблон fight.html)
    # TODO если игра идет - вызываем метод player.hit() экземпляра класса арены
    # TODO если игра не идет - пропускаем срабатывание метода (простот рендерим шаблон с текущими данными)
    pass


@app.route("/fight/use-skill")
def use_skill():
    # TODO кнопка использования скилла
    # TODO логика пркатикчески идентична предыдущему эндпоинту
    pass


@app.route("/fight/pass-turn")
def pass_turn():
    # TODO кнопка пропус хода
    # TODO логика пркатикчески идентична предыдущему эндпоинту
    # TODO однако вызываем здесь функцию следующий ход (arena.next_turn())
    pass


@app.route("/fight/end-fight")
def end_fight():
    # TODO кнопка завершить игру - переход в главное меню
    return render_template("index.html", heroes=heroes)


@app.route("/choose-hero/", methods=['post', 'get'])
def choose_hero():
    if request.method == "GET":
        return render_template(
            "hero_choosing.html",
            header="Выберите героя",
            classes=unit_classes.values(),
            weapons=Equipment().get_weapons_names(),
            armors=Equipment().get_armors_names(),
            next_button="Выбрать врага"
        )
    return redirect(url_for("choose_enemy"))


@app.route("/choose-enemy/", methods=['post', 'get'])
def choose_enemy():
    if request.method == "GET":
        return render_template(
            "hero_choosing.html",
            header="Выберите врага",
            classes=unit_classes.values(),
            weapons=Equipment().get_weapons_names(),
            armors=Equipment().get_armors_names(),
            next_button="Начать битву"
        )


if __name__ == "__main__":
    app.run()
