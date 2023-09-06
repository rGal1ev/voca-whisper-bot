from aiogram_dialog.widgets.text import Jinja

start_window_template: Jinja = Jinja("""
𝗩𝗼𝗰𝗮𝗪𝗵𝗶𝘀𝗽𝗲𝗿
Твой личный ассистент
<code>
1. Получи слово
2. Объясни слово на английском
3. Улучшай английский</code>
""")

welcome_window_template: Jinja = Jinja("""
{% if is_neuro_not_processing %}
{% if cancel_state_opened -%}
<b>Вы уверены</b>, что хотите покинуть игру?

<i>Текущий прогресс игры не сохраниться</i>
{% else %}

<b>Объясни слово</b>:  <code>{{ word }}</code>
<b>Твои очки</b>: <code>{{ successfully_attempts }}</code>

<b>Хорошо подумай</b>, опиши это слово как можно подробнее, 
и пришли нам ответ в виде сообщения:
{%- endif %}

{% else %}
Нейросеть <b>пытается разгадать</b> ваше объяснение
{% endif %}
""")

unsuccessful_guessed_word_window_template: Jinja = Jinja("""
<b>Ответ нейросети</b>:
<code>{{ neuro_word }}</code>
""")

end_of_game_window_template: Jinja = Jinja("""
🔥 <b>Спасибо за игру</b>
Надеемся вас встретить снова!

{% if successfully_attempts != 0 %}
<b>Отгаданных слов</b>: <code>{{ successfully_attempts }}</code>
{% endif %}
""")

error_neuro_window_template: Jinja = Jinja("""
<b>Если ошибка повторится</b>, попробуйте сыграть в игру чуть позже
""")
