import telebot
from telebot import types
import json
import os
import requests
from datetime import datetime, timedelta
import re
import random
import sys
import time
import threading
import math

# Токен бота (ЗАМЕНИТЕ НА СВОЙ!)
TELEGRAM_TOKEN = "8597234549:AAFirP1l2-7DUlqXvLYDieBVuHXYf2pP7I4"

# =================== ОЧИСТКА СОЕДИНЕНИЙ ===================

def cleanup_bot_connections(token):
    """Полная очистка всех соединений бота"""
    print("🧹 Очищаю все соединения бота...")
    
    try:
        url = f"https://api.telegram.org/bot{token}/deleteWebhook"
        response = requests.get(url, timeout=5)
        print(f"✅ Webhook удален: {response.json()}")
        return True
    except Exception as e:
        print(f"⚠️ Ошибка при удалении webhook: {e}")
        return False

# Выполняем очистку перед созданием бота
print("=" * 50)
print("🔧 Подготовка бота к запуску...")
cleanup_results = cleanup_bot_connections(TELEGRAM_TOKEN)
print("=" * 50)

# Создаем бота
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# =================== ПРОДВИНУТАЯ ЛОКАЛЬНАЯ НЕЙРОСЕТЬ С БОЛЬШОЙ БАЗОЙ ЗНАНИЙ ===================

class AdvancedLocalAI:
    def __init__(self):
        # ============= БАЗА ЗНАНИЙ ПО МАТЕМАТИКЕ =============
        self.math_knowledge = {
            "algebra": {
                "quadratic_equations": """
📐 *Квадратные уравнения*

*Общий вид:* ax² + bx + c = 0, где a ≠ 0

📌 *Методы решения:*

1️⃣ *Через дискриминант:*
D = b² - 4ac
• Если D > 0: x₁,₂ = (-b ± √D) / (2a)
• Если D = 0: x = -b/(2a)
• Если D < 0: нет действительных корней

2️⃣ *Теорема Виета (для приведенных x² + px + q = 0):*
x₁ + x₂ = -p
x₁ · x₂ = q

💡 *Примеры:*
• x² - 5x + 6 = 0 → D = 25 - 24 = 1 → x₁ = 3, x₂ = 2
• 2x² - 4x - 6 = 0 → D = 16 + 48 = 64 → x₁ = 3, x₂ = -1
• x² + 4x + 4 = 0 → D = 16 - 16 = 0 → x = -2
""",
                
                "systems_of_equations": """
📐 *Системы уравнений*

*Методы решения:*

1️⃣ *Метод подстановки:*
• Выразить одну переменную через другую
• Подставить во второе уравнение
• Решить полученное уравнение

2️⃣ *Метод сложения:*
• Умножить уравнения на коэффициенты
• Сложить уравнения для исключения переменной
• Решить полученное уравнение

💡 *Пример:*
{ x + y = 7
{ 2x - y = 5

Решение методом сложения:
3x = 12 → x = 4
4 + y = 7 → y = 3

Ответ: (4; 3)
""",
                
                "logarithms": """
📐 *Логарифмы*

*Определение:* logₐb = c означает, что aᶜ = b

📌 *Основные свойства:*

1️⃣ logₐ(x·y) = logₐx + logₐy
2️⃣ logₐ(x/y) = logₐx - logₐy
3️⃣ logₐxⁿ = n·logₐx
4️⃣ logₐb = log_c b / log_c a (переход к новому основанию)

💡 *Примеры:*
• log₂8 = 3 (так как 2³ = 8)
• log₅125 = 3 (так как 5³ = 125)
• log₃81 = 4 (так как 3⁴ = 81)
""",
                
                "derivatives": """
📈 *Производная функции*

*Определение:* Производная показывает скорость изменения функции в точке

📌 *Основные формулы:*

1️⃣ (xⁿ)' = n·xⁿ⁻¹
2️⃣ (sin x)' = cos x
3️⃣ (cos x)' = -sin x
4️⃣ (eˣ)' = eˣ
5️⃣ (ln x)' = 1/x

📌 *Правила дифференцирования:*

• (u + v)' = u' + v'
• (u·v)' = u'v + uv'
• (u/v)' = (u'v - uv')/v²

💡 *Примеры:*
• f(x) = x³ + 2x² - 5x + 3 → f'(x) = 3x² + 4x - 5
• f(x) = x·sin x → f'(x) = sin x + x·cos x
""",
                
                "integrals": """
📈 *Интегралы*

*Определение:* Интеграл - операция, обратная дифференцированию

📌 *Основные формулы:*

1️⃣ ∫xⁿ dx = xⁿ⁺¹/(n+1) + C, n ≠ -1
2️⃣ ∫1/x dx = ln|x| + C
3️⃣ ∫eˣ dx = eˣ + C
4️⃣ ∫sin x dx = -cos x + C
5️⃣ ∫cos x dx = sin x + C

💡 *Определенный интеграл:*
∫ₐᵇ f(x) dx = F(b) - F(a) - площадь под кривой
"""
            },
            
            "geometry": {
                "pythagorean_theorem": """
📐 *Теорема Пифагора*

В прямоугольном треугольнике квадрат гипотенузы равен сумме квадратов катетов:

c² = a² + b²

где:
• c — гипотенуза (сторона против прямого угла)
• a и b — катеты

💡 *Примеры:*
• Если катеты равны 3 и 4, то гипотенуза: c² = 9 + 16 = 25 → c = 5
• Если гипотенуза = 13, катет = 5, то второй катет: b² = 169 - 25 = 144 → b = 12

📌 *Обратная теорема:*
Если в треугольнике квадрат одной стороны равен сумме квадратов двух других сторон, то треугольник прямоугольный
""",
                
                "triangles": """
📐 *Треугольники*

*Виды треугольников:*

1️⃣ *По сторонам:*
• Равносторонний (все стороны равны)
• Равнобедренный (две стороны равны)
• Разносторонний (все стороны разные)

2️⃣ *По углам:*
• Остроугольный (все углы < 90°)
• Прямоугольный (один угол = 90°)
• Тупоугольный (один угол > 90°)

📌 *Основные формулы:*

• Площадь: S = ½·a·hₐ = ½·a·b·sin C
• Периметр: P = a + b + c
""",
                
                "circles": """
⚪ *Окружность и круг*

*Основные элементы:*
• Радиус (R) - расстояние от центра до окружности
• Диаметр (D) = 2R

📌 *Формулы:*

• Длина окружности: C = 2πR = πD
• Площадь круга: S = πR²
• Длина дуги: L = (πR·α)/180°, где α - угол в градусах
• Площадь сектора: S = (πR²·α)/360°
""",
                
                "stereometry": """
📦 *Стереометрия (объемные фигуры)*

📌 *Призма:*
• Объем: V = Sосн · h
• Боковая поверхность: Sбок = Pосн · h

📌 *Пирамида:*
• Объем: V = ⅓ · Sосн · h
• Боковая поверхность: Sбок = ½ · Pосн · l (l - апофема)

📌 *Цилиндр:*
• Объем: V = πR²h
• Боковая поверхность: Sбок = 2πRh

📌 *Конус:*
• Объем: V = ⅓ · πR²h
• Боковая поверхность: Sбок = πRl (l - образующая)

📌 *Шар:*
• Объем: V = ⁴⁄₃ · πR³
• Поверхность: S = 4πR²
"""
            },
            
            "trigonometry": {
                "basic_formulas": """
📐 *Основные тригонометрические формулы*

📌 *Основные соотношения:*

sin²α + cos²α = 1
tgα = sinα/cosα
ctgα = cosα/sinα
tgα · ctgα = 1

📌 *Формулы сложения:*

sin(α ± β) = sinα·cosβ ± cosα·sinβ
cos(α ± β) = cosα·cosβ ∓ sinα·sinβ

📌 *Формулы двойного угла:*

sin2α = 2·sinα·cosα
cos2α = cos²α - sin²α = 2cos²α - 1 = 1 - 2sin²α

💡 *Таблица значений:*
α° | 0° | 30° | 45° | 60° | 90°
sin | 0 | ½ | √2/2 | √3/2 | 1
cos | 1 | √3/2 | √2/2 | ½ | 0
tg | 0 | 1/√3 | 1 | √3 | ∞
"""
            },
            
            "probability": {
                "basics": """
🎲 *Теория вероятностей*

📌 *Основные понятия:*

• Вероятность события: P(A) = m/n, где m - благоприятные исходы, n - все возможные исходы
• Достоверное событие: P = 1
• Невозможное событие: P = 0
• Случайное событие: 0 < P < 1

📌 *Свойства вероятностей:*

• P(A + B) = P(A) + P(B) - P(AB) (для совместных)
• P(A + B) = P(A) + P(B) (для несовместных)
• P(AB) = P(A)·P(B) (для независимых)

💡 *Примеры:*
• Вероятность выпадения орла при броске монеты: 1/2
• Вероятность выпадения 6 на кубике: 1/6
"""
            }
        }
        
        # ============= БАЗА ЗНАНИЙ ПО РУССКОМУ ЯЗЫКУ =============
        self.russian_knowledge = {
            "orthography": {
                "spelling_rules": """
📝 *Правила орфографии*

📌 *Чередующиеся гласные:*
• -лаг-/-лож-: перед г пишем А, перед ж пишем О
• -раст-/-ращ-/-рос-: перед ст, щ пишем А, перед с пишем О
• -бер-/-бир-: если есть суффикс А, пишем И
• -кос-/-кас-: если есть суффикс А, пишем А
• -гор-/-гар-: под ударением А, без ударения О
• -зор-/-зар-: под ударением О, без ударения А

📌 *Приставки ПРЕ- и ПРИ-:*
• ПРЕ-: очень, пере (прекрасный, преграда)
• ПРИ-: приближение, присоединение, неполнота действия (приехать, приклеить)

📌 *Н и НН:*
• В прилагательных: -ан-, -ян-, -ин- → одна Н (искл: стеклянный, оловянный, деревянный)
• В причастиях: если есть приставка, зависимое слово → НН
• В кратких причастиях: всегда одна Н
""",
                
                "particles": """
📝 *Правописание частиц*

📌 *НЕ с разными частями речи:*

1️⃣ *Слитно:*
• Без НЕ не употребляется (негодовать)
• Можно заменить синонимом без НЕ (неправда = ложь)
• В неопределенных местоимениях (некто, нечто)

2️⃣ *Раздельно:*
• С глаголами (не читал)
• С деепричастиями (не читая)
• С краткими причастиями (не прочитан)
• При противопоставлении с союзом А (не правда, а ложь)

📌 *НИ:*
• Усиление отрицания (не сказал ни слова)
• В устойчивых выражениях (ни свет ни заря)
""",
                
                "punctuation": """
📝 *Пунктуация*

📌 *Запятая ставится:*

1️⃣ *Между однородными членами:*
• без союзов: книги, тетради, ручки
• с союзами А, НО: маленький, но умный

2️⃣ *В сложносочиненном предложении:*
[ ], и [ ]
[ ], но [ ]

3️⃣ *В сложноподчиненном предложении:*
[ ], (что...)
[ ], (когда...)

4️⃣ *При обособлении:*
• причастный оборот: Книга, лежащая на столе, интересная
• деепричастный оборот: Читая книгу, он делал заметки
• вводные слова: Конечно, я приду

📌 *Тире:*
• Подлежащее и сказуемое - существительные: Москва - столица
• Перед ЭТО, ВОТ: Читать - вот лучшее учение
"""
            },
            
            "grammar": {
                "verb_conjugation": """
📝 *Спряжение глаголов*

📌 *I спряжение (окончания -ешь, -ет, -ем, -ете, -ут/-ют):*
• Все глаголы на -ать, -ять, -еть (кроме исключений)
• Пример: читать → читаешь, читает, читают

📌 *II спряжение (окончания -ишь, -ит, -им, -ите, -ат/-ят):*
• Глаголы на -ить (кроме брить, стелить)
• Пример: говорить → говоришь, говорит, говорят

📌 *Глаголы-исключения:*

Ко II спряжению:
• гнать, держать, дышать, слышать
• смотреть, видеть, ненавидеть, обидеть, терпеть, зависеть, вертеть

К I спряжению:
• брить, стелить
""",
                
                "parts_of_speech": """
📝 *Части речи*

📌 *Самостоятельные:*

1️⃣ *Имя существительное:* кто? что?
• Род: м.р., ж.р., ср.р.
• Число: ед.ч., мн.ч.
• Падеж: И.п., Р.п., Д.п., В.п., Т.п., П.п.

2️⃣ *Имя прилагательное:* какой? чей?
• Разряды: качественные, относительные, притяжательные

3️⃣ *Глагол:* что делать? что сделать?
• Вид: совершенный, несовершенный
• Время: настоящее, прошедшее, будущее

4️⃣ *Местоимение:* кто? что? какой?

5️⃣ *Наречие:* как? где? когда?

📌 *Служебные:*
• Предлоги
• Союзы
• Частицы
"""
            },
            
            "paronyms": {
                "common_paronyms": """
📚 *Самые частые паронимы*

• Абонент — Абонемент
  Абонент - тот, кто пользуется абонементом
  Абонемент - право пользования чем-либо

• Дипломат — Дипломант
  Дипломат - работник посольства
  Дипломант - участник конкурса, получивший диплом

• Командированный — Командировочный
  Командированный - человек в командировке
  Командировочный - документ

• Невежа — Невежда
  Невежа - грубый, невоспитанный человек
  Невежда - малообразованный человек

• Одеть — Надеть
  Одеть кого-то (одеть ребенка)
  Надеть что-то (надеть пальто)

• Эффектный — Эффективный
  Эффектный - производящий эффект
  Эффективный - действенный, результативный
"""
            },
            
            "stylistics": {
                "text_analysis": """
📝 *Анализ текста*

📌 *Типы речи:*

1️⃣ *Повествование:*
• Рассказ о событиях
• Вопросы: что произошло?
• Глаголы, последовательность действий

2️⃣ *Описание:*
• Изображение предметов, людей, природы
• Вопросы: какой? какая?
• Прилагательные, причастия

3️⃣ *Рассуждение:*
• Объяснение, доказательство мысли
• Вопросы: почему? зачем?
• Вводные слова, союзы

📌 *Стили речи:*

• Разговорный: общение, диалоги
• Научный: статьи, учебники, лекции
• Официально-деловой: документы, заявления
• Публицистический: статьи, репортажи
• Художественный: рассказы, романы, поэзия
"""
            }
        }
        
        # ============= БАЗА ЗНАНИЙ ПО ФИЗИКЕ =============
        self.physics_knowledge = {
            "mechanics": {
                "newton_laws": """
⚛️ *Законы Ньютона*

📌 *Первый закон (закон инерции):*
Тело сохраняет состояние покоя или равномерного прямолинейного движения, если на него не действуют другие тела или их действие скомпенсировано.

📌 *Второй закон:*
F = m·a
Ускорение тела прямо пропорционально силе и обратно пропорционально массе.

📌 *Третий закон:*
Силы, с которыми тела действуют друг на друга, равны по модулю и противоположны по направлению:
F₁₂ = -F₂₁
""",
                
                "kinematics": """
⚛️ *Кинематика*

📌 *Равномерное движение:*
• Скорость: v = S/t
• Путь: S = v·t

📌 *Равноускоренное движение:*
• Ускорение: a = (v - v₀)/t
• Скорость: v = v₀ + a·t
• Путь: S = v₀·t + (a·t²)/2
• Перемещение: S = (v² - v₀²)/(2a)

📌 *Свободное падение:*
• g = 9.8 м/с² ≈ 10 м/с²
• v = g·t
• h = (g·t²)/2
""",
                
                "dynamics": """
⚛️ *Динамика*

📌 *Силы в природе:*

1️⃣ *Сила тяжести:*
Fтяж = m·g

2️⃣ *Сила упругости (закон Гука):*
Fупр = -k·Δx
где k - жесткость, Δx - деформация

3️⃣ *Сила трения:*
Fтр = μ·N
где μ - коэффициент трения, N - сила реакции опоры

📌 *Законы сохранения:*

• Импульс: p = m·v
• Закон сохранения импульса: m₁v₁ + m₂v₂ = const
• Кинетическая энергия: Eк = (m·v²)/2
• Потенциальная энергия: Eп = m·g·h
• Закон сохранения энергии: Eк₁ + Eп₁ = Eк₂ + Eп₂
"""
            },
            
            "electricity": {
                "ohms_law": """
⚡ *Закон Ома*

📌 *Для участка цепи:*
I = U / R

где:
• I — сила тока (Ампер)
• U — напряжение (Вольт)
• R — сопротивление (Ом)

📌 *Для полной цепи:*
I = ε / (R + r)

где:
• ε — ЭДС источника
• r — внутреннее сопротивление

📌 *Последовательное соединение:*
• R = R₁ + R₂ + R₃ + ...
• I = I₁ = I₂ = I₃ = ...
• U = U₁ + U₂ + U₃ + ...

📌 *Параллельное соединение:*
• 1/R = 1/R₁ + 1/R₂ + 1/R₃ + ...
• I = I₁ + I₂ + I₃ + ...
• U = U₁ = U₂ = U₃ = ...
""",
                
                "electromagnetism": """
⚡ *Электромагнетизм*

📌 *Магнитное поле:*
• Индукция магнитного поля: B
• Сила Ампера: F = B·I·L·sinα
• Сила Лоренца: F = q·v·B·sinα

📌 *Магнитный поток:*
Φ = B·S·cosα

📌 *Закон электромагнитной индукции:*
ε = -ΔΦ/Δt

📌 *Правило левой руки:*
Если расположить левую руку так, чтобы линии магнитного поля входили в ладонь, а 4 пальца указывали направление тока, то отставленный большой палец укажет направление силы Ампера
"""
            },
            
            "thermodynamics": {
                "gas_laws": """
🔥 *Термодинамика*

📌 *Уравнение состояния идеального газа:*
p·V = ν·R·T

где:
• p - давление
• V - объем
• ν - количество вещества
• R = 8.31 Дж/(моль·К)
• T - абсолютная температура (К)

📌 *Изопроцессы:*

1️⃣ *Изотермический (T = const):*
p·V = const (закон Бойля-Мариотта)

2️⃣ *Изобарный (p = const):*
V/T = const (закон Гей-Люссака)

3️⃣ *Изохорный (V = const):*
p/T = const (закон Шарля)

📌 *Первое начало термодинамики:*
ΔU = Q + A
""",
            },
            
            "optics": {
                "light": """
✨ *Оптика*

📌 *Законы геометрической оптики:*

1️⃣ *Закон прямолинейного распространения света*
2️⃣ *Закон отражения:* угол падения = углу отражения
3️⃣ *Закон преломления (Снеллиуса):*
sinα/sinβ = n₂/n₁ = v₁/v₂

📌 *Линзы:*
• Формула тонкой линзы: 1/F = 1/d + 1/f
• Оптическая сила: D = 1/F (диоптрии)
• Увеличение: Г = f/d = H/h

📌 *Виды линз:*
• Собирающие (F > 0) - двояковыпуклые
• Рассеивающие (F < 0) - двояковогнутые
"""
            },
            
            "quantum": {
                "quantum_physics": """
⚛️ *Квантовая физика*

📌 *Фотоэффект:*
Уравнение Эйнштейна: hν = Aвых + (m·v²)/2

где:
• h = 6.63·10⁻³⁴ Дж·с - постоянная Планка
• ν - частота света
• Aвых - работа выхода

📌 *Красная граница фотоэффекта:*
νmin = Aвых/h
λmax = h·c/Aвых

📌 *Энергия и импульс фотона:*
E = hν = h·c/λ
p = h/λ = E/c

📌 *Постулаты Бора:*

1️⃣ Атом может находиться только в стационарных состояниях
2️⃣ При переходе из одного состояния в другое излучается или поглощается фотон: hν = E₂ - E₁
"""
            }
        }
        
        # ============= БАЗА ЗНАНИЙ ПО ХИМИИ =============
        self.chemistry_knowledge = {
            "periodic_table": {
                "mendeleev": """
🧪 *Периодическая система Менделеева*

📌 *Структура таблицы:*

• *Периоды* (горизонтальные ряды) — 7 периодов
• *Группы* (вертикальные столбцы) — 8 групп

📌 *Закономерности:*

1️⃣ *В периоде слева направо:*
• Металлические свойства ослабевают
• Неметаллические свойства усиливаются
• Радиус атома уменьшается

2️⃣ *В группе сверху вниз:*
• Металлические свойства усиливаются
• Неметаллические свойства ослабевают
• Радиус атома увеличивается

📌 *Валентность:*
• I группа — 1
• II группа — 2
• III группа — 3
• IV группа — 4
• V группа — 3 или 5
• VI группа — 2, 4, 6
• VII группа — 1, 3, 5, 7
"""
            },
            
            "chemical_bonds": {
                "bond_types": """
🧪 *Типы химической связи*

📌 *Ковалентная связь:*
Образуется за счет общих электронных пар

• Неполярная (одинаковые атомы) - H₂, O₂, N₂
• Полярная (разные атомы) - HCl, H₂O, NH₃

📌 *Ионная связь:*
Образуется между металлами и неметаллами
Примеры: NaCl, KBr, CaF₂

📌 *Металлическая связь:*
В металлах и сплавах

📌 *Водородная связь:*
Между H и сильно электроотрицательными атомами (F, O, N)
Примеры: H₂O, HF, NH₃
""",
                
                "crystal_lattices": """
🧪 *Кристаллические решетки*

📌 *Типы кристаллических решеток:*

1️⃣ *Ионная:*
• В узлах - ионы
• Прочная, тугоплавкая
• Примеры: NaCl, KNO₃

2️⃣ *Атомная:*
• В узлах - атомы
• Очень прочная, очень тугоплавкая
• Примеры: алмаз, графит, Si

3️⃣ *Молекулярная:*
• В узлах - молекулы
• Непрочная, легкоплавкая
• Примеры: I₂, CO₂, H₂O

4️⃣ *Металлическая:*
• В узлах - ионы металлов
• Электропроводность, теплопроводность
• Примеры: все металлы
"""
            },
            
            "chemical_reactions": {
                "reaction_types": """
🧪 *Типы химических реакций*

📌 *По изменению состава веществ:*

1️⃣ *Соединения:* A + B = AB
Пример: 2H₂ + O₂ = 2H₂O

2️⃣ *Разложения:* AB = A + B
Пример: 2H₂O = 2H₂ + O₂

3️⃣ *Замещения:* A + BC = AC + B
Пример: Zn + 2HCl = ZnCl₂ + H₂

4️⃣ *Обмена:* AB + CD = AD + CB
Пример: AgNO₃ + NaCl = AgCl↓ + NaNO₃

📌 *По тепловому эффекту:*
• Экзотермические (+Q) - с выделением тепла
• Эндотермические (-Q) - с поглощением тепла
""",
                
                "redox": """
🧪 *Окислительно-восстановительные реакции (ОВР)*

📌 *Основные понятия:*

• *Окисление* - отдача электронов, повышение степени окисления
• *Восстановление* - принятие электронов, понижение степени окисления
• *Окислитель* - вещество, принимающее электроны
• *Восстановитель* - вещество, отдающее электроны

💡 *Пример:*
KMnO₄ + HCl → MnCl₂ + Cl₂ + KCl + H₂O

Mn⁺⁷ + 5e → Mn⁺² | 2 (восстановление)
2Cl⁻¹ - 2e → Cl₂⁰ | 5 (окисление)

Итог: 2KMnO₄ + 16HCl = 2MnCl₂ + 5Cl₂ + 2KCl + 8H₂O
"""
            },
            
            "organic": {
                "hydrocarbons": """
🧪 *Углеводороды*

📌 *Алканы (предельные):*
• Общая формула: CₙH₂ₙ₊₂
• Примеры: CH₄ (метан), C₂H₆ (этан), C₃H₈ (пропан)

📌 *Алкены (с двойной связью):*
• Общая формула: CₙH₂ₙ
• Примеры: C₂H₄ (этилен), C₃H₆ (пропилен)

📌 *Алкины (с тройной связью):*
• Общая формула: CₙH₂ₙ₋₂
• Примеры: C₂H₂ (ацетилен), C₃H₄ (метилацетилен)

📌 *Арены (ароматические):*
• Пример: C₆H₆ (бензол)
""",
                
                "oxygen_compounds": """
🧪 *Кислородсодержащие органические соединения*

📌 *Спирты:*
• Общая формула: R-OH
• Примеры: CH₃OH (метанол), C₂H₅OH (этанол)

📌 *Альдегиды:*
• Общая формула: R-CHO
• Примеры: HCHO (формальдегид), CH₃CHO (ацетальдегид)

📌 *Карбоновые кислоты:*
• Общая формула: R-COOH
• Примеры: HCOOH (муравьиная), CH₃COOH (уксусная)

📌 *Сложные эфиры:*
• R-COO-R'
• Пример: CH₃COOC₂H₅ (этилацетат)
"""
            }
        }
        
        # ============= БАЗА ЗНАНИЙ ПО АНГЛИЙСКОМУ ЯЗЫКУ =============
        self.english_knowledge = {
            "tenses": {
                "present_tenses": """
🇬🇧 *Настоящие времена (Present Tenses)*

📌 *Present Simple:*
• Факты, привычки, расписания
• I/You/We/They + V; He/She/It + V-s/-es
• I work every day. She works every day.

📌 *Present Continuous:*
• Действие прямо сейчас, временная ситуация
• am/is/are + V-ing
• I am working now. She is working at the moment.

📌 *Present Perfect:*
• Результат, опыт, только что сделано
• have/has + V-ed (3 форма)
• I have already done my homework.

📌 *Present Perfect Continuous:*
• Действие длилось и продолжается
• have/has + been + V-ing
• I have been working for 2 hours.
""",
                
                "past_tenses": """
🇬🇧 *Прошедшие времена (Past Tenses)*

📌 *Past Simple:*
• Действие в прошлом, последовательность событий
• V-ed (правильные) / 2 форма (неправильные)
• I worked yesterday. She went to London.

📌 *Past Continuous:*
• Действие в конкретный момент в прошлом
• was/were + V-ing
• I was working at 5 pm yesterday.

📌 *Past Perfect:*
• Действие до другого в прошлом
• had + V-ed (3 форма)
• I had finished before he arrived.

📌 *Past Perfect Continuous:*
• Длилось до момента в прошлом
• had + been + V-ing
• I had been working for 3 hours when he came.
""",
                
                "future_tenses": """
🇬🇧 *Будущие времена (Future Tenses)*

📌 *Future Simple:*
• Спонтанные решения, предсказания
• will + V
• I will call you tomorrow.

📌 *Future Continuous:*
• Действие будет длиться в определенный момент
• will + be + V-ing
• I will be working at 5 pm tomorrow.

📌 *Future Perfect:*
• Действие завершится к моменту
• will + have + V-ed (3 форма)
• I will have finished by 6 pm.

📌 *Конструкция "to be going to":*
• Планы, намерения
• am/is/are + going to + V
• I am going to visit my grandmother.
"""
            },
            
            "grammar": {
                "conditionals": """
🇬🇧 *Условные предложения (Conditionals)*

📌 *Zero Conditional:*
If + Present Simple, Present Simple
• Общие истины, факты
• If you heat ice, it melts.

📌 *First Conditional:*
If + Present Simple, will + V
• Реальные условия в будущем
• If it rains, I will stay at home.

📌 *Second Conditional:*
If + Past Simple, would + V
• Маловероятные ситуации
• If I had a million, I would travel.

📌 *Third Conditional:*
If + Past Perfect, would have + V-ed/3
• Нереальные ситуации в прошлом
• If I had studied, I would have passed.
""",
                
                "modal_verbs": """
🇬🇧 *Модальные глаголы*

📌 *Can* - мочь, уметь
• I can swim. (Я умею плавать)
• Прошедшее: could

📌 *Must* - должен, обязан
• You must do your homework.

📌 *May/Might* - можно, возможно
• It may rain tomorrow.

📌 *Should* - следует
• You should study more.

📌 *Have to* - приходится
• I have to wake up early.

📌 *Need* - нужно
• You need to rest.
"""
            },
            
            "vocabulary": {
                "word_formation": """
🇬🇧 *Словообразование*

📌 *Суффиксы существительных:*
• -er/-or: teacher, actor
• -tion/-sion: information
• -ment: development
• -ness: happiness

📌 *Суффиксы прилагательных:*
• -ful: beautiful
• -less: helpless
• -able/-ible: comfortable
• -ive: active
• -ous: dangerous
• -y: rainy

📌 *Суффиксы глаголов:*
• -ize/-ise: organize
• -en: strengthen

📌 *Отрицательные префиксы:*
• un-: unhappy
• in-: incorrect
• im-: impossible
• il-: illegal
• ir-: irregular
• dis-: disagree
"""
            }
        }
        
        # ============= БАЗА ЗНАНИЙ ПО ИНФОРМАТИКЕ =============
        self.informatics_knowledge = {
            "programming": {
                "python_basics": """
💻 *Основы Python*

📌 *Переменные и типы данных:*
x = 5              # целое число
y = 3.14           # float
name = "Тимми"     # строка
is_student = True  # bool

📌 *Списки:*
numbers = [1, 2, 3, 4, 5]
numbers.append(9)
numbers.sort()

📌 *Словари:*
person = {
    "name": "Анна",
    "age": 17
}

📌 *Условные операторы:*
if age >= 18:
    print("Взрослый")
elif age >= 12:
    print("Подросток")
else:
    print("Ребенок")

📌 *Циклы:*
for i in range(5):
    print(i)

while count < 5:
    print(count)
    count += 1

📌 *Функции:*
def add(a, b):
    return a + b
""",
                
                "algorithms": """
💻 *Алгоритмы*

📌 *Сортировка пузырьком:*
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

📌 *Бинарный поиск:*
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
""",
                
                "ege_tasks": """
💻 *Решение задач ЕГЭ по информатике*

📌 *Задание 2 (Таблицы истинности):*
def f(x, y, z):
    return (x and y) or (not x and z)

for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            print(f"{x} {y} {z} -> {int(f(x, y, z))}")

📌 *Задание 5 (Анализ алгоритмов):*
def algorithm(n):
    bin_n = bin(n)[2:]
    if bin_n.count('1') % 2 == 0:
        bin_n += '0'
    else:
        bin_n += '1'
    return int(bin_n, 2)

# Поиск минимального числа > 50
for i in range(1, 100):
    if algorithm(i) > 50:
        print(f"n={i}, R={algorithm(i)}")
        break
"""
            },
            
            "logic": {
                "boolean_algebra": """
💻 *Алгебра логики*

📌 *Основные операции:*

• Конъюнкция (И): A ∧ B, A and B
• Дизъюнкция (ИЛИ): A ∨ B, A or B
• Инверсия (НЕ): ¬A, not A
• Импликация: A → B = ¬A ∨ B
• Эквиваленция: A ≡ B = (A → B) ∧ (B → A)

📌 *Таблицы истинности:*

A B | A∧B | A∨B | A→B | A≡B
0 0 |  0  |  0  |  1  |  1
0 1 |  0  |  1  |  1  |  0
1 0 |  0  |  1  |  0  |  0
1 1 |  1  |  1  |  1  |  1

📌 *Законы де Моргана:*
¬(A ∧ B) = ¬A ∨ ¬B
¬(A ∨ B) = ¬A ∧ ¬B
"""
            },
            
            "number_systems": {
                "conversions": """
💻 *Системы счисления*

📌 *Перевод в десятичную систему:*

• 1011₂ = 1·2³ + 0·2² + 1·2¹ + 1·2⁰ = 8 + 0 + 2 + 1 = 11₁₀
• 123₈ = 1·8² + 2·8¹ + 3·8⁰ = 64 + 16 + 3 = 83₁₀
• 1A₁₆ = 1·16¹ + 10·16⁰ = 16 + 10 = 26₁₀

📌 *Перевод из десятичной в двоичную:*

def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

📌 *Быстрый перевод:*

• 2 → 8: группируем по 3 бита: 101101₂ = 101 101₂ = 55₈
• 2 → 16: группируем по 4 бита: 101101₂ = 0010 1101₂ = 2D₁₆
"""
            }
        }
        
        # ============= ОБЩИЕ СОВЕТЫ ПО УЧЕБЕ =============
        self.study_advice = {
            "how_to_study": """
📚 *Как эффективно учиться*

🎯 *Техника Помодоро:*
• 25 минут работы
• 5 минут отдыха
• После 4 циклов - длинный перерыв

🧠 *Метод Фейнмана:*
• Выбери тему
• Объясни её просто
• Найди пробелы
• Упрости

📝 *Интервальные повторения:*
• Через: 20 мин → 1 день → 3 дня → 1 нед → 1 мес

💪 *Советы:*
• Записывай конспекты от руки
• Объясняй материал вслух
• Решай практические задачи
• Делай перерывы каждые 45-50 мин
• Спи 7-9 часов
""",
            
            "exam_preparation": """
📝 *Подготовка к экзаменам*

📅 *Планирование:*

1️⃣ *За 6-8 месяцев:*
• Изучи структуру экзамена
• Составь план подготовки

2️⃣ *За 4-6 месяцев:*
• Изучение теории
• Решение типовых заданий

3️⃣ *За 2-4 месяца:*
• Интенсивная практика
• Решение вариантов

4️⃣ *За 1 месяц:*
• Пробные экзамены на время
• Повторение сложных тем

📌 *Стратегии:*
• Начинай с простых заданий
• Не зацикливайся на сложных
• Контролируй время
• Проверяй ответы

🎯 *В день экзамена:*
• Выспись
• Позавтракай
• Приди заранее
• Сохраняй спокойствие
""",
            
            "memory_techniques": """
🧠 *Техники запоминания*

📌 *Метод ассоциаций:*
Связывай новую информацию с тем, что уже знаешь

📌 *Метод Цицерона:*
Размещай информацию в знакомом месте

📌 *Акростихи:*
Составляй предложения из первых букв
Пример: "Каждый Охотник Желает Знать Где Сидит Фазан" (цвета радуги)

📌 *Для формул:*
• Пиши на карточках
• Развесь на видных местах
• Проговаривай вслух

📌 *Для иностранных слов:*
• Используй приложения (Anki, Quizlet)
• Создавай ассоциации
• Учи слова в контексте
"""
        }
        
        # Маппинг ключевых слов на категории знаний (ИСПРАВЛЕНО)
        self.keyword_mapping = {
            # Математика
            "квадратн": ("math_knowledge", "algebra", "quadratic_equations"),
            "уравнен": ("math_knowledge", "algebra", "quadratic_equations"),
            "дискриминант": ("math_knowledge", "algebra", "quadratic_equations"),
            "систем": ("math_knowledge", "algebra", "systems_of_equations"),
            "логарифм": ("math_knowledge", "algebra", "logarithms"),
            "производн": ("math_knowledge", "algebra", "derivatives"),
            "интеграл": ("math_knowledge", "algebra", "integrals"),
            "пифагор": ("math_knowledge", "geometry", "pythagorean_theorem"),
            "треугольник": ("math_knowledge", "geometry", "triangles"),
            "окружн": ("math_knowledge", "geometry", "circles"),
            "круг": ("math_knowledge", "geometry", "circles"),
            "стериметр": ("math_knowledge", "geometry", "stereometry"),
            "объем": ("math_knowledge", "geometry", "stereometry"),
            "тригонометр": ("math_knowledge", "trigonometry", "basic_formulas"),
            "sin": ("math_knowledge", "trigonometry", "basic_formulas"),
            "cos": ("math_knowledge", "trigonometry", "basic_formulas"),
            "tg": ("math_knowledge", "trigonometry", "basic_formulas"),
            "вероятн": ("math_knowledge", "probability", "basics"),
            
            # Русский язык
            "орфограф": ("russian_knowledge", "orthography", "spelling_rules"),
            "правописан": ("russian_knowledge", "orthography", "spelling_rules"),
            "не с": ("russian_knowledge", "orthography", "particles"),
            "пунктуац": ("russian_knowledge", "orthography", "punctuation"),
            "запят": ("russian_knowledge", "orthography", "punctuation"),
            "спряжен": ("russian_knowledge", "grammar", "verb_conjugation"),
            "глагол": ("russian_knowledge", "grammar", "verb_conjugation"),
            "части реч": ("russian_knowledge", "grammar", "parts_of_speech"),
            "пароним": ("russian_knowledge", "paronyms", "common_paronyms"),
            "стил": ("russian_knowledge", "stylistics", "text_analysis"),
            "текст": ("russian_knowledge", "stylistics", "text_analysis"),
            
            # Физика
            "ньютон": ("physics_knowledge", "mechanics", "newton_laws"),
            "закон": ("physics_knowledge", "mechanics", "newton_laws"),
            "кинематик": ("physics_knowledge", "mechanics", "kinematics"),
            "скорост": ("physics_knowledge", "mechanics", "kinematics"),
            "ускорен": ("physics_knowledge", "mechanics", "kinematics"),
            "динамик": ("physics_knowledge", "mechanics", "dynamics"),
            "сил": ("physics_knowledge", "mechanics", "dynamics"),
            "электричеств": ("physics_knowledge", "electricity", "ohms_law"),
            "ом": ("physics_knowledge", "electricity", "ohms_law"),
            "напряжен": ("physics_knowledge", "electricity", "ohms_law"),
            "ток": ("physics_knowledge", "electricity", "ohms_law"),
            "магнит": ("physics_knowledge", "electricity", "electromagnetism"),
            "индукц": ("physics_knowledge", "electricity", "electromagnetism"),
            "термодинам": ("physics_knowledge", "thermodynamics", "gas_laws"),
            "газ": ("physics_knowledge", "thermodynamics", "gas_laws"),
            "тепл": ("physics_knowledge", "thermodynamics", "gas_laws"),
            "оптик": ("physics_knowledge", "optics", "light"),
            "свет": ("physics_knowledge", "optics", "light"),
            "линз": ("physics_knowledge", "optics", "light"),
            "квант": ("physics_knowledge", "quantum", "quantum_physics"),
            "фотоэффект": ("physics_knowledge", "quantum", "quantum_physics"),
            
            # Химия
            "менделеев": ("chemistry_knowledge", "periodic_table", "mendeleev"),
            "таблиц": ("chemistry_knowledge", "periodic_table", "mendeleev"),
            "периодическ": ("chemistry_knowledge", "periodic_table", "mendeleev"),
            "связь": ("chemistry_knowledge", "chemical_bonds", "bond_types"),
            "ковалентн": ("chemistry_knowledge", "chemical_bonds", "bond_types"),
            "ионн": ("chemistry_knowledge", "chemical_bonds", "bond_types"),
            "реакц": ("chemistry_knowledge", "chemical_reactions", "reaction_types"),
            "овр": ("chemistry_knowledge", "chemical_reactions", "redox"),
            "окисл": ("chemistry_knowledge", "chemical_reactions", "redox"),
            "углеводород": ("chemistry_knowledge", "organic", "hydrocarbons"),
            "алкан": ("chemistry_knowledge", "organic", "hydrocarbons"),
            "алкен": ("chemistry_knowledge", "organic", "hydrocarbons"),
            "спирт": ("chemistry_knowledge", "organic", "oxygen_compounds"),
            "кислот": ("chemistry_knowledge", "organic", "oxygen_compounds"),
            
            # Английский
            "present": ("english_knowledge", "tenses", "present_tenses"),
            "past": ("english_knowledge", "tenses", "past_tenses"),
            "future": ("english_knowledge", "tenses", "future_tenses"),
            "времен": ("english_knowledge", "tenses", "present_tenses"),
            "condition": ("english_knowledge", "grammar", "conditionals"),
            "условн": ("english_knowledge", "grammar", "conditionals"),
            "modal": ("english_knowledge", "grammar", "modal_verbs"),
            "модальн": ("english_knowledge", "grammar", "modal_verbs"),
            "словообразован": ("english_knowledge", "vocabulary", "word_formation"),
            
            # Информатика
            "python": ("informatics_knowledge", "programming", "python_basics"),
            "код": ("informatics_knowledge", "programming", "python_basics"),
            "программ": ("informatics_knowledge", "programming", "python_basics"),
            "алгоритм": ("informatics_knowledge", "programming", "algorithms"),
            "сортировк": ("informatics_knowledge", "programming", "algorithms"),
            "поиск": ("informatics_knowledge", "programming", "algorithms"),
            "егэ информатик": ("informatics_knowledge", "programming", "ege_tasks"),
            "логик": ("informatics_knowledge", "logic", "boolean_algebra"),
            "таблиц истинност": ("informatics_knowledge", "logic", "boolean_algebra"),
            "систем счислен": ("informatics_knowledge", "number_systems", "conversions"),
            "двоичн": ("informatics_knowledge", "number_systems", "conversions"),
            
            # Общие советы
            "как учит": ("study_advice", "how_to_study"),
            "эффективн": ("study_advice", "how_to_study"),
            "подготовк": ("study_advice", "exam_preparation"),
            "экзамен": ("study_advice", "exam_preparation"),
            "запомина": ("study_advice", "memory_techniques"),
            "памят": ("study_advice", "memory_techniques")
        }
    
    def get_knowledge(self, path_parts):
        """Получение знания по пути (ИСПРАВЛЕНО)"""
        try:
            if len(path_parts) == 3:
                # Для знаний с тремя уровнями (категория, подкатегория, тема)
                category_dict = getattr(self, path_parts[0])
                return category_dict[path_parts[1]][path_parts[2]]
            elif len(path_parts) == 2:
                # Для знаний с двумя уровнями (категория, тема) - study_advice
                category_dict = getattr(self, path_parts[0])
                return category_dict[path_parts[1]]
            else:
                return None
        except (AttributeError, KeyError):
            return None
    
    def is_study_question(self, question):
        """Проверяет, относится ли вопрос к учебе"""
        study_keywords = [
            "учиться", "учеба", "урок", "домашка", "домашнее", "задание",
            "школа", "колледж", "универ", "институт", "студент", "ученик",
            "экзамен", "зачет", "сессия", "оценка", "балл",
            "предмет", "дисциплина", "курс", "лекция", "семинар",
            "математика", "русский", "физика", "химия", "биология",
            "история", "обществознание", "география", "литература",
            "английский", "информатика", "программирование",
            "формула", "правило", "теория", "практика", "конспект",
            "егэ", "огэ", "подготовка", "тест", "контрольная",
            "как решить", "помоги", "объясни", "расскажи"
        ]
        
        question_lower = question.lower()
        return any(keyword in question_lower for keyword in study_keywords)
    
    def get_answer(self, question):
        """Получение ответа на учебный вопрос"""
        if not self.is_study_question(question):
            return None
        
        question_lower = question.lower()
        
        # Проверяем точное совпадение по ключевым словам (ИСПРАВЛЕНО)
        for keyword, path_parts in self.keyword_mapping.items():
            if keyword in question_lower:
                knowledge = self.get_knowledge(path_parts)
                if knowledge:
                    return f"🤖 *Тимми (ИИ помощник):*\n\n{knowledge}\n\n💡 *Есть еще вопросы? Просто спроси! Я знаю всё по учебе!*"
        
        # Если не нашли точного совпадения, ищем по категориям
        if any(word in question_lower for word in ["математик", "алгебр", "геометр"]):
            return self.get_math_response(question)
        elif any(word in question_lower for word in ["русск", "орфограф", "пунктуац"]):
            return self.get_russian_response(question)
        elif any(word in question_lower for word in ["физик", "механи", "электричеств"]):
            return self.get_physics_response(question)
        elif any(word in question_lower for word in ["хими", "элемент", "реакц"]):
            return self.get_chemistry_response(question)
        elif any(word in question_lower for word in ["английск", "english", "grammar"]):
            return self.get_english_response(question)
        elif any(word in question_lower for word in ["информатик", "програм", "python"]):
            return self.get_informatics_response(question)
        elif any(word in question_lower for word in ["как", "совет", "подготовк"]):
            return self.get_advice_response(question)
        
        # Общий ответ для учебных вопросов
        return self.get_general_study_response()
    
    def get_math_response(self, question):
        """Ответ на вопрос по математике"""
        if "уравнен" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.math_knowledge['algebra']['quadratic_equations']}\n\n💡 *Есть еще вопросы по математике?*"
        elif "пифагор" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.math_knowledge['geometry']['pythagorean_theorem']}\n\n💡 *Есть еще вопросы по математике?*"
        elif "производн" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.math_knowledge['algebra']['derivatives']}\n\n💡 *Есть еще вопросы по математике?*"
        elif "интеграл" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.math_knowledge['algebra']['integrals']}\n\n💡 *Есть еще вопросы по математике?*"
        elif "логарифм" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.math_knowledge['algebra']['logarithms']}\n\n💡 *Есть еще вопросы по математике?*"
        elif "треугольник" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.math_knowledge['geometry']['triangles']}\n\n💡 *Есть еще вопросы по математике?*"
        elif "тригонометр" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.math_knowledge['trigonometry']['basic_formulas']}\n\n💡 *Есть еще вопросы по математике?*"
        else:
            return self.get_general_math_response()
    
    def get_russian_response(self, question):
        """Ответ на вопрос по русскому языку"""
        if "спряжен" in question or "глагол" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.russian_knowledge['grammar']['verb_conjugation']}\n\n💡 *Есть еще вопросы по русскому языку?*"
        elif "пароним" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.russian_knowledge['paronyms']['common_paronyms']}\n\n💡 *Есть еще вопросы по русскому языку?*"
        elif "пунктуац" in question or "запят" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.russian_knowledge['orthography']['punctuation']}\n\n💡 *Есть еще вопросы по русскому языку?*"
        elif "орфограф" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.russian_knowledge['orthography']['spelling_rules']}\n\n💡 *Есть еще вопросы по русскому языку?*"
        else:
            return self.get_general_russian_response()
    
    def get_physics_response(self, question):
        """Ответ на вопрос по физике"""
        if "ньютон" in question or "закон" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.physics_knowledge['mechanics']['newton_laws']}\n\n💡 *Есть еще вопросы по физике?*"
        elif "ом" in question or "электричеств" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.physics_knowledge['electricity']['ohms_law']}\n\n💡 *Есть еще вопросы по физике?*"
        elif "кинематик" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.physics_knowledge['mechanics']['kinematics']}\n\n💡 *Есть еще вопросы по физике?*"
        elif "динамик" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.physics_knowledge['mechanics']['dynamics']}\n\n💡 *Есть еще вопросы по физике?*"
        elif "термодинам" in question or "газ" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.physics_knowledge['thermodynamics']['gas_laws']}\n\n💡 *Есть еще вопросы по физике?*"
        elif "оптик" in question or "свет" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.physics_knowledge['optics']['light']}\n\n💡 *Есть еще вопросы по физике?*"
        elif "квант" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.physics_knowledge['quantum']['quantum_physics']}\n\n💡 *Есть еще вопросы по физике?*"
        else:
            return self.get_general_physics_response()
    
    def get_chemistry_response(self, question):
        """Ответ на вопрос по химии"""
        if "менделеев" in question or "таблиц" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.chemistry_knowledge['periodic_table']['mendeleev']}\n\n💡 *Есть еще вопросы по химии?*"
        elif "связь" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.chemistry_knowledge['chemical_bonds']['bond_types']}\n\n💡 *Есть еще вопросы по химии?*"
        elif "реакц" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.chemistry_knowledge['chemical_reactions']['reaction_types']}\n\n💡 *Есть еще вопросы по химии?*"
        elif "овр" in question or "окисл" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.chemistry_knowledge['chemical_reactions']['redox']}\n\n💡 *Есть еще вопросы по химии?*"
        elif "углеводород" in question or "алкан" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.chemistry_knowledge['organic']['hydrocarbons']}\n\n💡 *Есть еще вопросы по химии?*"
        else:
            return self.get_general_chemistry_response()
    
    def get_english_response(self, question):
        """Ответ на вопрос по английскому языку"""
        if "present" in question or "настоящ" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.english_knowledge['tenses']['present_tenses']}\n\n💡 *Есть еще вопросы по английскому?*"
        elif "past" in question or "прошедш" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.english_knowledge['tenses']['past_tenses']}\n\n💡 *Есть еще вопросы по английскому?*"
        elif "future" in question or "будущ" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.english_knowledge['tenses']['future_tenses']}\n\n💡 *Есть еще вопросы по английскому?*"
        elif "conditional" in question or "условн" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.english_knowledge['grammar']['conditionals']}\n\n💡 *Есть еще вопросы по английскому?*"
        elif "modal" in question or "модальн" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.english_knowledge['grammar']['modal_verbs']}\n\n💡 *Есть еще вопросы по английскому?*"
        else:
            return self.get_general_english_response()
    
    def get_informatics_response(self, question):
        """Ответ на вопрос по информатике"""
        if "python" in question or "код" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.informatics_knowledge['programming']['python_basics']}\n\n💡 *Есть еще вопросы по информатике?*"
        elif "алгоритм" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.informatics_knowledge['programming']['algorithms']}\n\n💡 *Есть еще вопросы по информатике?*"
        elif "егэ" in question and "информатик" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.informatics_knowledge['programming']['ege_tasks']}\n\n💡 *Есть еще вопросы по подготовке к ЕГЭ?*"
        elif "логик" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.informatics_knowledge['logic']['boolean_algebra']}\n\n💡 *Есть еще вопросы по информатике?*"
        elif "систем счислен" in question or "двоичн" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.informatics_knowledge['number_systems']['conversions']}\n\n💡 *Есть еще вопросы по информатике?*"
        else:
            return self.get_general_informatics_response()
    
    def get_advice_response(self, question):
        """Ответ с общими советами"""
        if "как учит" in question or "эффективн" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.study_advice['how_to_study']}\n\n💡 *Есть еще вопросы?*"
        elif "экзамен" in question or "подготовк" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.study_advice['exam_preparation']}\n\n💡 *Есть еще вопросы?*"
        elif "запомина" in question or "памят" in question:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.study_advice['memory_techniques']}\n\n💡 *Есть еще вопросы?*"
        else:
            return f"🤖 *Тимми (ИИ помощник):*\n\n{self.study_advice['how_to_study']}\n\n{self.study_advice['exam_preparation']}\n\n💡 *Задай конкретный вопрос по учебе!*"
    
    def get_general_study_response(self):
        """Общий ответ для учебных вопросов"""
        responses = [
            "📚 *Совет по учебе:* Используй технику Фейнмана - объясни материал так, как будто учишь младшего брата или сестру. Это поможет выявить пробелы в понимании!",
            
            "🎯 *Для лучшего запоминания:* Делай перерывы каждые 45-50 минут. Мозг лучше усваивает информацию порциями, а во время отдыха происходит консолидация памяти.",
            
            "⏰ *Тайм-менеджмент:* Попробуй технику Pomodoro: 25 минут работы, 5 минут отдыха. После 4 циклов — длинный перерыв 15-30 минут.",
            
            "📝 *Конспектирование:* Записывай материал от руки, а не печатай. Это активирует моторную память и улучшает запоминание на 30%!",
            
            "🧠 *Активное обучение:* Не просто читай, а задавай вопросы, ищи примеры, решай задачи. Пассивное чтение дает только 10% усвоения материала.",
            
            "💪 *Мотивация:* Разбей большую цель на маленькие шаги и отмечай каждый выполненный пункт. Маленькие победы поддерживают мотивацию!",
            
            "😴 *Сон и учеба:* Во сне мозг обрабатывает и закрепляет информацию. 7-9 часов сна необходимы для эффективного обучения!",
            
            "📊 *Интервальные повторения:* Повторяй материал через: 20 минут → 1 день → 3 дня → 1 неделю → 1 месяц. Это переводит информацию в долговременную память."
        ]
        
        return f"🤖 *Тимми (ИИ помощник):*\n\n{random.choice(responses)}\n\n💡 *Если хочешь узнать подробнее о какой-то теме, спроси конкретнее! У меня есть огромная база знаний по всем предметам!*"
    
    def get_general_math_response(self):
        return f"""🤖 *Тимми (ИИ помощник):*

📐 *Математика*

У меня есть подробная информация по темам:
• Квадратные уравнения и дискриминант
• Системы уравнений
• Логарифмы и их свойства
• Производные и интегралы
• Теорема Пифагора и геометрия
• Треугольники и их свойства
• Окружности и круги
• Стереометрия (объемные фигуры)
• Тригонометрия
• Теория вероятностей

💡 *Задай конкретный вопрос по любой из этих тем!*
Например: "Объясни теорему Пифагора" или "Как решать квадратные уравнения?" """
    
    def get_general_russian_response(self):
        return f"""🤖 *Тимми (ИИ помощник):*

📗 *Русский язык*

У меня есть подробная информация по темам:
• Правила орфографии (правописание)
• Частицы НЕ и НИ
• Пунктуация (запятые, тире, двоеточия)
• Спряжение глаголов
• Части речи
• Паронимы
• Анализ текста и стили речи

💡 *Задай конкретный вопрос по любой из этих тем!*
Например: "Объясни спряжение глаголов" или "Какие бывают паронимы?" """
    
    def get_general_physics_response(self):
        return f"""🤖 *Тимми (ИИ помощник):*

⚛️ *Физика*

У меня есть подробная информация по темам:
• Законы Ньютона
• Кинематика (движение)
• Динамика (силы)
• Электричество (закон Ома)
• Электромагнетизм
• Термодинамика и газы
• Оптика и свет
• Квантовая физика

💡 *Задай конкретный вопрос по любой из этих тем!*
Например: "Объясни законы Ньютона" или "Что такое закон Ома?" """
    
    def get_general_chemistry_response(self):
        return f"""🤖 *Тимми (ИИ помощник):*

⚗️ *Химия*

У меня есть подробная информация по темам:
• Периодическая таблица Менделеева
• Типы химической связи
• Кристаллические решетки
• Типы химических реакций
• Окислительно-восстановительные реакции (ОВР)
• Углеводороды (алканы, алкены)
• Кислородсодержащие соединения

💡 *Задай конкретный вопрос по любой из этих тем!*
Например: "Расскажи про таблицу Менделеева" или "Что такое ОВР?" """
    
    def get_general_english_response(self):
        return f"""🤖 *Тимми (ИИ помощник):*

🇬🇧 *Английский язык*

У меня есть подробная информация по темам:
• Настоящие времена (Present Tenses)
• Прошедшие времена (Past Tenses)
• Будущие времена (Future Tenses)
• Условные предложения (Conditionals)
• Модальные глаголы
• Словообразование

💡 *Задай конкретный вопрос по любой из этих тем!*
Например: "Объясни Present Perfect" или "Что такое Conditional sentences?" """
    
    def get_general_informatics_response(self):
        return f"""🤖 *Тимми (ИИ помощник):*

💻 *Информатика*

У меня есть подробная информация по темам:
• Основы Python (переменные, циклы, функции)
• Алгоритмы и структуры данных
• Решение задач ЕГЭ по информатике
• Алгебра логики
• Системы счисления

💡 *Задай конкретный вопрос по любой из этих тем!*
Например: "Как написать цикл в Python?" или "Объясни двоичную систему счисления" """

# =================== БАЗА ДАННЫХ ПО ЕГЭ/ОГЭ ===================

class ExamDatabase:
    def __init__(self):
        self.subjects = {
            "math": {
                "name": "📘 Математика",
                "ege": {
                    "structure": "Профиль: 19 заданий (1-12 база, 13-19 профиль)\nБаза: 21 задание\n\n*Баллы:*\n1-12 задания: 1 балл\n13-15 задания: 2 балла\n16-17 задания: 3 балла\n18-19 задания: 4 балла\n\n*Минимальный порог:* 27 баллов\n*Максимальный балл:* 100 баллов",
                    "topics": "1. Алгебра\n2. Геометрия\n3. Уравнения и неравенства\n4. Функции и графики\n5. Производные\n6. Стереометрия\n7. Теория вероятностей и статистика\n8. Планиметрия\n9. Параметры\n10. Экономические задачи",
                    "how_to_prepare": "🎯 *Как готовиться к ЕГЭ по математике:*\n\n1. *Освойте базовую часть (задания 1-12):*\n   - Решайте ежедневно по 10-15 простых задач\n   - Учите формулы и теоремы\n   - Отрабатывайте вычисления без калькулятора\n\n2. *Переходите к профильной части:*\n   - Задания 13-15: уравнения, неравенства, стереометрия\n   - Решайте по 3-5 сложных задач в день\n   - Анализируйте ошибки\n\n3. *Работа с самыми сложными задачами:*\n   - Задание 18: параметры - изучайте методы решения\n   - Задание 19: теория чисел - тренируйте логику\n\n4. *Практика на время:*\n   - Раз в неделю решайте полный вариант за 3 часа 55 минут\n   - Учитесь распределять время\n\n5. *Используйте ресурсы:*\n   - Открытый банк заданий ФИПИ\n   - Пробные варианты от МЦКО\n   - Видеоразборы сложных задач",
                    "resources": [
                        "📚 *Учебники:*\n- Мордкович А.Г. 'Алгебра и начала математического анализа'\n- Атанасян Л.С. 'Геометрия 10-11'\n- Ященко И.В. 'ЕГЭ 2026. Математика'",
                        "🌐 *Сайты:*\n- РешуЕГЭ (ege.sdamgia.ru)\n- Незнайка (neznaika.info)\n- КЭС (math-ege.sdamgia.ru)\n- ФИПИ (fipi.ru)",
                        "📱 *Приложения:*\n- Photomath\n- Wolfram Alpha\n- Mathway\n- Учи.ру",
                        "🎥 *RuTube каналы:*\n- Математика ЕГЭ Умскул"
                    ],
                    "plan": "🎯 *8-недельный план подготовки:*\n\n*Неделя 1-2:* Алгебра (задания 1-4, 9-10)\n*Неделя 3-4:* Геометрия (задания 5-6, 16)\n*Неделя 5-6:* Уравнения и функции (задания 7-8, 11-12)\n*Неделя 7-8:* Сложные задачи (13-19)\n\n*Ежедневно:*\n- 30 мин теория\n- 60 мин практика\n- 30 мин разбор ошибок",
                    "tips": [
                        "📌 Начни с простых заданий (1-12) - они дают 62 балла!",
                        "📌 Задание 13 (уравнения) решай в первую очередь - оно самое предсказуемое",
                        "📌 Для стереометрии (14) учи чертить правильные чертежи",
                        "📌 Экономическую задачу (17) решай через систему уравнений",
                        "📌 Параметры (18) оставь на конец - самая сложная задача",
                        "📌 Решай минимум 1 полный вариант в неделю на время"
                    ],
                    "changes_2026": "🔔 *Изменения 2026:*\n• Добавлены задачи на анализ больших данных\n• В задание 17 включены задачи по финансовой математике\n• Усилен акцент на практическое применение математики\n• Введены задачи на анализ графиков реальных процессов"
                },
                "oge": {
                    "structure": "25 заданий (1-19 - база, 20-25 - сложные)\n\n*Баллы:*\n1-19 задания: 1 балл\n20-25 задания: 2 балла\n\n*Минимальный порог:* 8 баллов\n*Максимальный балл:* 31 балл",
                    "topics": "1. Числа и вычисления\n2. Алгебраические выражения\n3. Уравнения и неравенства\n4. Функции и графики\n5. Геометрия\n6. Статистика и теория вероятностей\n7. Координатная плоскость\n8. Практико-ориентированные задачи",
                    "how_to_prepare": "🎯 *Как готовиться к ОГЭ по математике:*\n\n1. *Повторите основы 5-8 классов:*\n   - Арифметические операции\n   - Дроби и проценты\n   - Основы алгебры\n   - Начала геометрии\n\n2. *Освойте программу 9 класса:*\n   - Квадратные уравнения\n   - Неравенства\n   - Функции и графики\n   - Геометрические задачи\n\n3. *Тренируйте решение практических задач:*\n   - Задачи 1-5 (повседневные ситуации)\n   - Задачи на проценты и пропорции\n   - Чтение графиков и диаграммы\n\n4. *Готовьтесь к геометрическим задачам:*\n   - Учите теоремы и свойства фигур\n   - Тренируйтесь в построении чертежей\n   - Решайте задачи на доказательство\n\n5. *Регулярная практика:*\n   - Ежедневно по 5-10 задач разного типа\n   - Раз в неделю - полный вариант\n   - Работа над ошибками",
                    "resources": [
                        "📚 *Учебники:*\n- Макарычев Ю.Н. 'Алгебра 9 класс'\n- Атанасян Л.С. 'Геометрия 7-9'\n- Ященко И.В. 'ОГЭ 2026. Математика'",
                        "🌐 *Сайты:*\n- СдамГИА (oge.sdamgia.ru)\n- ЯКласс (yaklass.ru)\n- ФИПИ (fipi.ru)",
                        "🎥 *RuTube каналы:*\n- Математика ОГЭ Умскул"
                    ],
                    "plan": "🎯 *6-месячный план подготовки:*\n\n*Месяц 1-2:* Повторение 7-8 класса\n*Месяц 3-4:* Программа 9 класса\n*Месяц 5:* Решение вариантов\n*Месяц 6:* Работа над ошибками\n\n*Еженедельно:*\n- 4 часа теория\n- 6 часов практика\n- 2 часа пробники",
                    "tips": [
                        "📌 Изучи структуру экзамена и кристерии оценивания",
                        "📌 Проверь текущий уровень",
                        "📌 Составь план подготовки",
                        "📌 Тренируйся в решении задач",
                        "📌 Проверяй вычисления - большинство ошибок из-за невнимательности"
                    ],
                    "changes_2026": "🔔 *Изменения 2026:*\n• Увеличено количество практико-ориентированных задач\n• Добавлены задачи на анализ данных из реальной жизни\n• В геометрии больше внимания пространственным задачам\n• Включены задачи на основы статистики и анализа данных"
                }
            },
            "russian": {
                "name": "📗 Русский язык",
                "ege": {
                    "structure": "27 заданий + сочинение\n\n*Часть 1:* Задания 1-26 (34 балла)\n*Часть 2:* Задание 27 - сочинение (25 баллов)\n\n*Минимальный порог:* 24 балла\n*Максимальный балл:* 50 баллов",
                    "topics": "1. Информационная обработка текста (1-3)\n2. Средства выразительности (4-8)\n3. Орфография (9-15)\n4. Пунктуация (16-21)\n5. Нормы языка (22-26)\n6. Сочинение по прочитанному тексту (27)",
                    "how_to_prepare": "🎯 *Как готовиться к ЕГЭ по русскому языку:*\n\n1. *Систематическое повторение правил:*\n   - Орфография: безударные гласные, приставки, суффиксы\n   - Пунктуация: запятые, тире, двоеточия\n   - Нормы языка: ударения, паронимы\n\n2. *Работа с текстом:*\n   - Учитесь выделять главную мысль\n   - Определять средства выразительности\n   - Анализировать структуру текста\n\n3. *Подготовка к сочинению:*\n   - Изучите критерии оценивания (К1-К12)\n   - Тренируйтесь в подборе аргументов\n   - Учитесь формулировать проблему и позицию автора\n\n4. *Регулярная практика:*\n   - Ежедневно по 10-15 тестовых заданий\n   - Раз в неделю - написание сочинения\n   - Работа с текстами разных стилей\n\n5. *Работа над ошибками:*\n   - Ведите тетрадь ошибок\n   - Анализируйте типичные ошибки\n   - Повторяйте проблемные темы",
                    "resources": [
                        "📚 *Учебники:*\n- Цыбулько И.П. 'ЕГЭ. Русский язык'\n- Егораева Г.Т. 'ЕГЭ. Задания части 2'\n- Сенина Н.А. 'Русский язык. Подготовка к ЕГЭ'",
                        "🌐 *Сайты:*\n- РешуЕГЭ (rus-ege.sdamgia.ru)\n- Грамота.ру\n- Textologia.ru\n- ФИПИ (fipi.ru)",
                        "📱 *Приложения:*\n- Правила русского языка\n- Орфография\n- Пунктуация",
                        "🎥 *RuTube каналы:*\n- Русский язык ЕГЭ Умскул"
                    ],
                    "plan": "🎯 *Поэтапный план:*\n\n*Этап 1 (3 месяца):* Теория\n- 2 недели: Орфография\n- 2 недели: Пунктуация\n- 2 недели: Выразительные средства\n- 2 недели: Нормы языка\n\n*Этап 2 (2 месяца):* Практика\n- Решение тестовых заданий\n- Написание сочинений\n\n*Этап 3 (1 месяц):* Итоговый\n- Пробники на время\n- Работа над ошибками",
                    "tips": [
                        "📌 Выучи 15 правил орфографии - это 7 заданий!",
                        "📌 Составляй план сочинения: проблема → комментарий → позиция автора → аргументы → вывод",
                        "📌 В задании 26 учи цитаты великих людей для аргументов",
                        "📌 Проверяй каждое сочинение на грамматические ошибки",
                        "📌 Тренируйся писать сочинение за 60-70 минут"
                    ],
                    "changes_2026": "🔔 *Изменения 2026:*\n• В сочинении усилен акцент на актуальные социальные проблемы\n• Добавлены тексты современных авторов\n• В заданиях на нормы языка включены современные речевые ситуации\n• Увеличено количество заданий на работу с информацией"
                },
                "oge": {
                    "structure": "13 заданий\n\n*Часть 1:* Сжатое изложение (1)\n*Часть 2:* Тестовая часть (2-12)\n*Часть 3:* Сочинение (13.1, 13.2, 13.3)\n\n*Минимальный порог:* 15 баллов\n*Максимальный балл:* 37 баллов",
                    "topics": "1. Сжатое изложение\n2. Понимание текста \n3. Лексика и грамматика \n4. Сочинение-рассуждение",
                    "how_to_prepare": "🎯 *Как готовиться к ОГЭ по русскому языку:*\n\n1. *Освойте технику сжатого изложения:*\n   - Учитесь выделять главное\n   - Используйте приемы сжатия: исключение, обобщение\n   - Тренируйте аудиовосприятие\n\n2. *Повторите грамматику:*\n   - Части речи и их особенности\n   - Синтаксис и пунктуация\n   - Орфографические правила\n\n3. *Подготовка к сочинению:*\n   - Изучите структуру сочинения-рассуждения\n   - Тренируйтесь в подборе примеров\n   - Учитесь логично выстраивать текст\n\n4. *Работа с тестовой частью:*\n   - Регулярно решайте задания\n   - Анализируйте типы заданий\n   - Учитесь понимать текст\n\n5. *Комплексная подготовка:*\n   - Чередуйте разные виды работ\n   - Пишите полные варианты\n   - Работайте над скоростью",
                    "resources": [
                        "📚 *Учебники:*\n- Егораева Г.Т. 'ОГЭ. Русский язык'\n- Сенина Н.А. 'Русский язык. ОГЭ'\n- Дощинский Р.А. 'Сборник типовых вариантов экзаменационных заданий ОГЭ русский язык'",
                        "🌐 *Сайты:*\n- СдамГИА (rus-oge.sdamgia.ru)\n- ФИПИ (fipi.ru)",
                        "🎥 *RuTube каналы:*\n- Русский ОГЭ Умскул"
                    ],
                    "plan": "🎯 *План подготовки:*\n\n*Месяц 1-2:* Теория\n- Изложение: техники сжатия\n- Тестовая часть: повторение правил\n\n*Месяц 3-4:* Практика\n- Написание изложений (2 в неделю)\n- Решение тестов\n\n*Месяц 5-6:* Сочинение\n- Структура сочинения\n- Аргументация\n- Практика написания",
                    "tips": [
                        "📌 Изложение пиши по плану: слушай → записывай ключевые слова → составляй план → пиши",
                        "📌 В сочинении 13.3 обязательно дай определение понятия",
                        "📌 Для изложения используй 3 приема: исключение, обобщение, упрощение",
                        "📌 Проверяй пунктуацию в сложных предложениях",
                        "📌 Учи цитаты для сочинения 13.1"
                    ],
                    "changes_2026": "🔔 *Изменения 2026:*\n• В изложении используются тексты на актуальные темы\n• В сочинении включены темы, связанные с цифровой грамотностью\n• Усилен акцент на функциональное чтение\n• Добавлены задания на анализ современных текстов"
                }
            },
            "social": {
                "name": "📙 Обществознание",
                "ege": {
                    "structure": "25 заданий\n\n*Часть 1:* 16 заданий с кратким ответом\n*Часть 2:* 9 заданий с развернутым ответом (включая эссе)\n\n*Минимальный порог:* 45 баллов\n*Максимальный балл:* 100 баллов",
                    "topics": "1. Человек и общество\n2. Экономика\n3. Социальные отношения\n4. Политика\n5. Право\n6. Социальные нормы и конфликты\n7. Мировая экономика и политика",
                    "how_to_prepare": "🎯 *Как готовиться к ЕГЭ по обществознанию:*\n\n1. *Изучите все разделы системно:*\n   - Начните с «Человек и общество» - это база\n   - Затем «Экономика» и «Политика»\n   - Закончите «Право» - самый сложный раздел\n\n2. *Учите термины и определения:*\n   - Составляйте словарь понятий\n   - Учите наизусть ключевые определения\n   - Понимайте различия между похожими терминами\n\n3. *Тренируйте работу с текстами:*\n   - Учитесь выделять главную мысль\n   - Находите связи между абзацами\n   - Формулируйте выводы\n\n4. *Пишите эссе регулярно:*\n   - Выбирайте разные темы\n   - Учитесь подбирать аргументы\n   - Следите за структурой и логикой\n\n5. *Решайте задания на анализ ситуаций:*\n   - Учитесь применять теорию к практике\n   - Анализируйте реальные социальные ситуации\n   - Тренируйтесь в решении кейсов",
                    "resources": [
                        "📚 *Учебники:*\n- Боголюбов Л.Н. 'Обществознание 10-11 класс'\n- Кишенкова О.В. 'ЕГЭ. Обществознание'\n- Баранов П.А. 'Обществознание в схемах и таблицах'",
                        "🌐 *Сайты:*\n- РешуЕГЭ (soc-ege.sdamgia.ru)\n- ФИПИ (fipi.ru)",
                        "📱 *Приложения:*\n- Обществознание ЕГЭ\n- Теория права\n- Политика и общество",
                        "🎥 *RuTube каналы:*\n- Обществознание ОГЭ Умскул"
                    ],
                    "plan": "🎯 *План подготовки:*\n\n*Этап 1 (3 месяца):* Теория\n- Человек и общество (1 месяц)\n- Экономика и политика (1 месяц)\n- Право и социальные отношения (1 месяц)\n\n*Этап 2 (2 месяца):* Практика\n- Решение тестовых заданий\n- Написание эссе (2 в неделю)\n- Работа с текстами\n\n*Этап 3 (1 месяц):* Итоговый\n- Пробники на время\n- Работа над слабыми местами",
                    "tips": [
                        "📌 Учи термины - они помогут в 70% заданий",
                        "📌 Для эссе выбирай ту тему, в которой лучше всего разбираешься",
                        "📌 В заданиях на анализ текста сначала прочитай вопросы, потом текст",
                        "📌 Регулярно следи за новостями - это поможет в эссе",
                        "📌 Используй схемы и таблицы для запоминания"
                    ],
                    "changes_2026": "🔔 *Изменения 2026:*\n• Усилен акцент на практическое применение знаний\n• Добавлены задания на анализ современных социальных процессов\n• Включены темы по цифровой экономике и кибербезопасности\n• Больше внимания международным отношениям"
                },
                "oge": {
                    "structure": "24 задания\n\n*Часть 1:* 16 заданий с кратким ответом\n*Часть 2:* 6 заданий с развернутым ответом\n\n*Минимальный порог:* 14 баллов\n*Максимальный балл:* 37 баллов",
                    "topics": "1. Человек и общество\n2. Сфера духовной культуры\n3. Экономика\n4. Социальная сфера\n5. Политика\n6. Право",
                    "how_to_prepare": "🎯 *Как готовиться к ОГЭ по обществознанию:*\n\n1. *Освойте базовые понятия:*\n   - Социальные роли и статусы\n   - Экономические процессы\n   - Политическая система\n   - Правовые нормы\n\n2. *Работа с текстом и схемами:*\n   - Учитесь анализировать социальную информацию\n   - Читайте схемы и таблицы\n   - Формулируйте выводы\n\n3. *Решение практических задач:*\n   - Анализ социальных ситуаций\n   - Применение правовых норм\n   - Экономические расчеты\n\n4. *Подготовка к развернутым ответам:*\n   - Учитесь структурировать ответ\n   - Приводите примеры\n   - Аргументируйте свою позицию",
                    "plan": "🎯 *План подготовки:*\n\n*Месяц 1-2:* Человек и общество, духовная культура\n*Месяц 3-4:* Экономика и социальная сфера\n*Месяц 5:* Политика и право\n*Месяц 6:* Итоговое повторение и пробники",
                    "changes_2026": "🔔 *Изменения 2026:*\n• Больше практико-ориентированных заданий\n• Акцент на социальные проблемы молодежи\n• Включены темы цифровой грамотности\n• Усилен раздел по основам финансовой грамотности"
                }
            },
            "history": {
                "name": "📔 История",
                "ege": {
                    "structure": "21 задание\n\n*Часть 1:* 12 заданий с кратким ответом\n*Часть 2:* 9 заданий с развернутым ответом (включая историческое сочинение)\n\n*Минимальный порог:* 32 баллов\n*Максимальный балл:* 100 баллов",
                    "topics": "1. Древняя Русь (IX-XIII века)\n2. Формирование Российского государства (XIV-XVII века)\n3. Российская империя (XVIII - начало XX века)\n4. СССР (1917-1991 годы)\n5. Современная Россия (с 1992 года)\n6. Всеобщая история",
                    "how_to_prepare": "🎯 *Как готовиться к ЕГЭ по истории:*\n\n1. *Хронологический подход:*\n   - Изучайте периоды последовательно\n   - Составляйте хронологические таблицы\n   - Учите даты ключевых событий\n\n2. *Работа с историческими источниками:*\n   - Анализ документов разных эпох\n   - Определение авторства и времени создания\n   - Критическая оценка информации\n\n3. *Изучение исторических личностей:*\n   - Роль личности в истории\n   - Деятельность правителей\n   - Вклад ученых, деятелей культуры\n\n4. *Подготовка к историческому сочинению:*\n   - Выбор периода для анализа\n   - Определение причинно-следственных связей\n   - Оценка значимости периода\n\n5. *Запоминание культурных достижений:*\n   - Архитектура разных эпох\n   - Живопись и литература\n   - Научные открытия",
                    "resources": [
                        "📚 *Учебники:*\n- Орлов А.С. 'История России'\n- Данилов А.А. 'ЕГЭ. История России'\n- Пазин Р.В. 'История. Подготовка к ЕГЭ'",
                        "🌐 *Сайты:*\n- РешуЕГЭ (hist-ege.sdamgia.ru)\n- ФИПИ (fipi.ru)",
                        "🎥 *RuTube каналы:*\n- История ЕГЭ Умскул"
                    ],
                    "plan": "🎯 *План подготовки:*\n\n*Этап 1 (4 месяца):* Хронология\n- Древняя Русь и Средневековье (1 месяц)\n- Российская империя (1.5 месяца)\n- СССР и современность (1.5 месяца)\n\n*Этап 2 (2 месяца):* Углубленное изучение\n- Культура и искусство\n- Внешняя политика\n- Социально-экономическое развитие\n\n*Этап 3 (1 месяц):* Итоговый\n- Решение пробников\n- Написание сочинений\n- Повторение сложных тем",
                    "tips": [
                        "📌 Учи даты в связках: событие - дата - последствия",
                        "📌 Для сочинения выбирай период, который хорошо знаешь",
                        "📌 Регулярно работай с картами и иллюстрациями",
                        "📌 Составляй таблицы сравнения разных периодов",
                        "📌 Читай первоисточники - они помогают понять эпоху"
                    ],
                    "changes_2026": "🔔 *Изменения 2026:*\n• Усилен акцент на анализ исторических источников\n• Добавлены задания на работу с историческими картами\n• Включены темы по истории культуры и науки\n• Больше внимания региональной истории"
                },
                "oge": {
                    "structure": "24 задания\n\n*Часть 1:* 17 заданий с кратким ответом\n*Часть 2:* 7 заданий с развернутым ответом\n\n*Минимальный порог:* 11 баллов\n*Максимальный балл:* 37 баллов",
                    "topics": "1. Древность и Средневековье\n2. Новое время\n3. Новейшая история\n4. История России с древнейших времен",
                    "how_to_prepare": "🎯 *Как готовиться к ОГЭ по истории:*\n\n1. *Освоение хронологии:*\n   - Основные даты и события\n   - Периодизация истории\n   - Составление временных линий\n\n2. *Работа с исторической информацией:*\n   - Анализ текстовых источников\n   - Чтение исторических карт\n   - Работа с иллюстративным материалом\n\n3. *Изучение культурного наследия:*\n   - Памятники архитектуры\n   - Произведения искусства\n   - Достижения науки и техники\n\n4. *Решение типовых заданий:*\n   - Установление хронологической последовательности\n   - Соотнесение событий и дат\n   - Анализ исторических ситуаций",
                    "plan": "🎯 *План подготовки:*\n\n*Месяц 1-2:* Древний мир и Средневековье\n*Месяц 3-4:* Новое время\n*Месяц 5:* Новейшая история\n*Месяц 6:* История России и итоговое повторение",
                    "changes_2026": "🔔 *Изменения 2026:*\n• Увеличено количество заданий на работу с источниками\n• Акцент на историю повседневности\n• Включены задания на анализ исторических мифов\n• Больше внимания краеведению"
                }
            },
            "biology": {
                "name": "🔬 Биология",
                "ege": {
                    "structure": "28 заданий\n\n*Часть 1:* 21 задание с кратким ответом\n*Часть 2:* 7 заданий с развернутым ответом\n\n*Минимальный порог:* 36 баллов\n*Максимальный балл:* 57 баллов",
                    "topics": "1. Биология как наука\n2. Клетка как биологическая система\n3. Организм как биологическая система\n4. Система и многообразие органического мира\n5. Организм и среда\n6. Эволюция живой природы\n7. Экосистемы и присущие им закономерности",
                    "how_to_prepare": "🎯 *Как готовиться к ЕГЭ по биологии:*\n\n1. *Системное изучение разделов:*\n   - Начните с цитологии (строение клетки)\n   - Затем анатомия и физиология человека\n   - Генетика и селекция\n   - Эволюция и экология\n\n2. *Работа с биологическими терминами:*\n   - Учите латинские названия\n   - Понимайте значение терминов\n   - Используйте термины в контексте\n\n3. *Решение генетических задач:*\n   - Освойте законы Менделя\n   - Решайте задачи на сцепленное наследование\n   - Тренируйтесь в составлении родословных\n\n4. *Анализ биологических процессов:*\n   - Фотосинтез и дыхание\n   - Деление клети\n   - Нервная и гуморальная регуляция\n\n5. *Работа с иллюстрациями:*\n   - Определение органов и систем\n   - Анализ схем и графиков\n   - Интерпретация результатов экспериментов",
                    "resources": [
                        "📚 *Учебники:*\n- Пасечник В.В. 'Биология 10-11 класс'\n- Захаров В.Б. 'Биология. Общая биология'\n- Кириленко А.А. 'Биология. Подготовка к ЕГЭ'",
                        "🌐 *Сайты:*\n- РешуЕГЭ (bio-ege.sdamgia.ru)\n- ФИПИ(fipi.ru)",
                        "🎥 *RuTube каналы:*\n- Биология ОГЭ Умскул"
                    ],
                    "plan": "🎯 *План подготовки:*\n\n*Этап 1 (3 месяца):* Основы\n- Цитология и гистология (1 месяц)\n- Анатомия и физиология (1 месяц)\n- Генетика (1 месяц)\n\n*Этап 2 (2 месяца):* Углубление\n- Эволюция и экология\n- Систематика организмов\n- Решение сложных задач\n\n*Этап 3 (1 месяц):* Итоговый\n- Решение пробников\n- Анализ ошибок\n- Повторение слабых тем",
                    "tips": [
                        "📌 Учи биологию по блокам: сначала растения, потом животные, затем человек",
                        "📌 Для генетических задач составляй схемы скрещивания",
                        "📌 Используй цветные схемы для запоминания процессов",
                        "📌 Регулярно решай задачи на наследование признаков",
                        "📌 Читай научно-популярную литературу по биологии"
                    ],
                    "changes_2026": "🔔 *Изменения 2026:*\n• Усилен акцент на молекулярную биологию\n• Добавлены задания по биоинформатике\n• Включены темы по генной инженерии\n• Больше внимания экологическим проблемам"
                },
                "oge": {
                    "structure": "26 заданий\n\n*Часть 1:* 21 задание с кратким ответом\n*Часть 2:* 5 заданий с развернутым ответом\n\n*Минимальный порог:* 13 баллов\n*Максимальный балл:* 47 баллов",
                    "topics": "1. Биология как наука\n2. Признаки живых организмов\n3. Система, многообразие и эволюция живой природы\n4. Человек и его здоровье\n5. Взаимосвязи организмов и окружающей среды",
                    "how_to_prepare": "🎯 *Как готовиться к ОГЭ по биологии:*\n\n1. *Освоение основных понятий:*\n   - Клеточное строение организмов\n   - Процессы жизнедеятельности\n   - Классификация организмов\n   - Основы экологии\n\n2. *Изучение организма человека:*\n   - Строение систем органов\n   - Гигиена и здоровье\n   - Профилактика заболеваний\n\n3. *Решение практических задач:*\n   - Определение организмов\n   - Анализ биологических процессов\n   - Прогнозирование результатов\n\n4. *Работа с биологическими объектами:*\n   - Описание растений и животных\n   - Сравнительный анализ\n   - Выявление приспособлений",
                    "plan": "🎯 *План подготовки:*\n\n*Месяц 1-2:* Общая биология и ботаника\n*Месяц 3-4:* Зоология и анатомия человека\n*Месяц 5:* Экология и эволюция\n*Месяц 6:* Итоговое повторение и пробники",
                    "changes_2026": "🔔 *Изменения 2026:*\n• Больше практических заданий\n• Акцент на здоровый образ жизни\n• Включены задания по микробиологии\n• Усилен раздел экологии"
                }
            },
            "chemistry": {
                "name": "⚗️ Химия",
                "ege": {
                    "structure": "34 задания\n\n*Часть 1:* 28 заданий с кратким ответом\n*Часть 2:* 6 заданий с развернутым ответом\n\n*Минимальный порог:* 36 баллов\n*Максимальный балл:* 100 баллов",
                    "topics": "1. Теоретические основы химии\n2. Неорганическая химия\n3. Органическая химия\n4. Методы познания в химии\n5. Расчеты по химическим уравнениям\n6. Химия и жизнь",
                    "how_to_prepare": "🎯 *Как готовиться к ЕГЭ по химии:*\n\n1. *Освоение теоретических основ:*\n   - Строение атома и Периодический закон\n   - Химическая связь\n   - Классификация реакций\n   - Скорость химических реакций\n\n2. *Решение расчетных задач:*\n   - Нахождение массы, объема, количества вещества\n   - Расчеты по уравнениям реакций\n   - Задачи на смеси и растворы\n   - Определение формулы вещества\n\n3. *Изучение неорганической химии:*\n   - Классы неорганических соединений\n   - Химические свойства элементов\n   - Получение и применение веществ\n\n4. *Освоение органической химии:*\n   - Классификация органических соединений\n   - Изомерия и гомология\n   - Химические свойства органических веществ\n   - Цепочки превращений\n\n5. *Экспериментальная часть:*\n   - Правила работы в лаборатории\n   - Качественные реакции\n   - Методы разделения смесей",
                    "resources": [
                        "📚 *Учебники:*\n- Габриелян О.С. 'Химия 10-11 класс'\n- Рудзитис Г.Е. 'Химия'\n- Доронькин В.Н. 'Химия. Подготовка к ЕГЭ'",
                        "🌐 *Сайты:*\n- РешуЕГЭ (chem-ege.sdamgia.ru)\n- ФИПИ (fipi.ru)",
                        "🎥 *RuTube каналы:*\n- Химия ОГЭ Умскул"
                    ],
                    "plan": "🎯 *План подготовки:*\n\n*Этап 1 (3 месяца):* Теория\n- Общая химия (1 месяц)\n- Неорганическая химия (1 месяц)\n- Органическая химия (1 месяц)\n\n*Этап 2 (2 месяца):* Практика\n- Решение расчетных задач\n- Цепочки превращений\n- Качественные реакции\n\n*Этап 3 (1 месяц):* Итоговый\n- Решение пробников\n- Анализ ошибок\n- Повторение сложных тем",
                    "tips": [
                        "📌 Учи таблицу растворимости и ряд активности металлов",
                        "📌 Для органической химии составляй схемы превращений",
                        "📌 Решай задачи ежедневно, начиная с простых",
                        "📌 Учи названия реакций и их механизмы",
                        "📌 Составляй конспекты с уравнениями реакций"
                    ],
                    "changes_2026": "🔔 *Изменения 2026:*\n• Усилен акцент на экологическую химию\n• Добавлены задания по нанохимии\n• Включены задачи на анализ реальных химических процессов\n• Больше внимания практическому применению химии"
                },
                "oge": {
                    "structure": "23 задания\n\n*Часть 1:* 19 заданий с кратким ответом\n*Часть 2:* 4 задания с развернутым ответом\n\n*Минимальный порог:* 10 баллов\n*Максимальный балл:* 38 баллов",
                    "topics": "1. Вещества и их превращения\n2. Химический элемент\n3. Химическая реакция\n4. Элементарные основы неорганической химии\n5. Первоначальные представления об органических веществах",
                    "how_to_prepare": "🎯 *Как готовиться к ОГЭ по химии:*\n\n1. *Освоение основных понятий:*\n   - Классификация веществ\n   - Строение атома\n   - Типы химических связей\n   - Классы неорганических соединений\n\n2. *Решение простых расчетных задач:*\n   - Расчеты по формулам\n   - Простейшие стехиометрические расчеты\n   - Задачи на растворы\n\n3. *Изучение химических свойств:*\n   - Свойства основных классов соединений\n   - Условия протекания реакций\n   - Признаки химических реакций\n\n4. *Экспериментальные задания:*\n   - Правила техники безопасности\n   - Описание опытов\n   - Наблюдение и фиксация результатов",
                    "plan": "🎯 *План подготовки:*\n\n*Месяц 1-2:* Общая химия и неорганическая химия\n*Месяц 3-4:* Решение задач и органическая химия\n*Месяц 5:* Эксперименты и практикум\n*Месяц 6:* Итоговое повторение и пробники",
                    "changes_2026": "🔔 *Изменения 2026:*\n• Больше практических заданий\n• Акцент на безопасное обращение с веществами\n• Включены задания по химии в быту\n• Усилен раздел экологической химии"
                }
            },
            "literature": {
                "name": "📖 Литература",
                "ege": {
                    "structure": "11 заданий\n\n*Часть 1:* 6 заданий с кратким ответом\n*Часть 2:* 5 заданий с развернутым ответом (4 анализа + 1 сочинение)\n\n*Минимальный порог:* 40 баллов\n*Максимальный балл:* 100 баллов",
                    "topics": "1. Древнерусская литература\n2. Литература XVIII века\n3. Литература XIX века\n4. Литература XX века\n5. Современная литература\n6. Зарубежная литература",
                    "how_to_prepare": "🎯 *Как готовиться к ЕГЭ по литературе:*\n\n1. *Чтение и анализ произведений:*\n   - Внимательное чтение текстов из кодификатора\n   - Составление характеристик героев\n   - Анализ сюжета и композиции\n\n2. *Изучение литературоведческих терминов:*\n   - Тропы и стилистические фигуры\n   - Литературные направления\n   - Жанры и их особенности\n\n3. *Подготовка к анализу текста:*\n   - Умение выделять тему и идею\n   - Анализ языковых средств\n   - Интерпретация текста\n\n4. *Написание сочинений:*\n   - Структура литературного сочинения\n   - Подбор аргументов из текста\n   - Логика изложения\n\n5. *Сопоставительный анализ:*\n   - Поиск общих тем в разных произведениях\n   - Сравнение героев и ситуаций\n   - Выявление авторской позиции",
                    "resources": [
                        "📚 *Учебники:*\n- Зинин С.А. 'Литература'\n- Ерохина Е.Л. 'ЕГЭ. Литература'\n- Назарова Т.Н. 'Литература. Подготовка к ЕГЭ'",
                        "🌐 *Сайты:*\n- РешуЕГЭ (lit-ege.sdamgia.ru)\n- 5litra.ru\n- ФИПИ (fipi.ru)",
                        "🎥 *RuTube каналы:*\n- Литература ОГЭ Умскул"
                    ],
                    "plan": "🎯 *План подготовки:*\n\n*Этап 1 (3 месяца):* Чтение произведений\n- Русская классика XIX века (1.5 месяца)\n- Литература XX века (1.5 месяца)\n\n*Этап 2 (2 месяца):* Анализ и теория\n- Литературоведческие термины\n- Анализ поэзии и прозы\n- Сопоставительные задания\n\n*Этап 3 (1 месяц):* Практика письма\n- Написание сочинений (2-3 в неделю)\n- Анализ текстов на время\n- Работа над структурой ответов",
                    "tips": [
                        "📌 Читай произведения полностью, а не в сокращении",
                        "📌 Веди читательский дневник с анализом прочитанного",
                        "📌 Учи цитаты из ключевых произведений",
                        "📌 Тренируйся писать сочинения на время",
                        "📌 Анализируй не только содержание, но и форму произведения"
                    ],
                    "changes_2026": "🔔 *Изменения 2026:*\n• Усилен акцент на анализ поэтических текстов\n• Добавлены задания по современной литературе\n• Включены произведения зарубежных авторов\n• Больше внимания межтекстовым связям"
                },
                "oge": {
                    "structure": "5 заданий\n\n*Часть 1:* 2 задания с кратким ответом\n*Часть 2:* 3 задания с развернутым ответом\n\n*Минимальный порог:* 14 баллов\n*Максимальный балл:* 45 баллов",
                    "topics": "1. Фольклор\n2. Древнерусская литература\n3. Русская литература XVIII-XIX веков\n4. Русская литература XX века\n5. Зарубежная литература",
                    "how_to_prepare": "🎯 *Как готовиться к ОГЭ по литературе:*\n\n1. *Чтение и понимание текстов:*\n   - Основные произведения школьной программы\n   - Выделение главной мысли\n   - Понимание характеров героев\n\n2. *Анализ литературных произведений:*\n   - Определение темы и идеи\n   - Характеристика героев\n   - Анализ художественных средств\n\n3. *Написание развернутых ответов:*\n   - Структура ответа\n   - Подбор примеров из текста\n   - Логическое изложение мыслей\n\n4. *Сопоставление произведений:*\n   - Поиск общих тем\n   - Сравнение героев\n   - Выявление авторской позиции",
                    "plan": "🎯 *План подготовки:*\n\n*Месяц 1-3:* Чтение произведений\n*Месяц 4-5:* Анализ и теория\n*Месец 6:* Практика письма и пробники",
                    "changes_2026": "🔔 *Изменения 2026:*\n• Больше внимания анализу текста\n• Акцент на понимание авторской позиции\n• Включены современные произведения\n• Усилен раздел по фольклору"
                }
            },
            "geography": {
                "name": "🌍 География",
                "ege": {
                    "structure": "34 заданий\n\n*Часть 1:* 27 заданий с кратким ответом\n*Часть 2:* 7 заданий с развернутым ответом\n\n*Минимальный порог:* 40 баллов\n*Максимальный балл:* 100 баллов",
                    "topics": "1. Источники географической информации\n2. Природа Земли и человек\n3. Население мира\n4. Мировое хозяйство\n5. Природопользование и геоэкология\n6. Регионы и страны мира\n7. География России",
                    "how_to_prepare": "🎯 *Как готовиться к ЕГЭ по географии:*\n\n1. *Работа с картами и атласами:*\n   - Физическая карта мира\n   - Политическая карта\n   - Карты природных ресурсов\n   - Карты населения и хозяйства\n\n2. *Изучение статистических данных:*\n   - Демографические показатели\n   - Экономические индикаторы\n   - Природно-ресурсный потенциал\n\n3. *Решение расчетных задач:*\n   - Определение координат\n   - Расчет масштаба\n   - Определение времени\n   - Расчет ресурсообеспеченности\n\n4. *Анализ географических процессов:*\n   - Климатические закономерности\n   - Демографические процессы\n   - Экономическое развитие\n   - Экологические проблемы\n\n5. *Региональная география:*\n   - Характеристика стран и регионов\n   - Сравнительный анализ\n   - Выявление проблем и перспектив",
                    "resources": [
                        "📚 *Учебники:*\n- Максаковский В.П. 'География'\n- Алексеев А.И. 'География России'\n- Барабанов В.В. 'География. Подготовка к ЕГЭ'",
                        "🌐 *Сайты:*\n- РешуЕГЭ (geo-ege.sdamgia.ru)\n- ФИПИ (fipi.ru)",
                        "🎥 *RuTube каналы:*\n- География ОГЭ Умскул"
                    ],
                    "plan": "🎯 *План подготовки:*\n\n*Этап 1 (3 месяца):* Основы\n- Физическая география (1 месяц)\n- Экономическая география (1 месяц)\n- География России (1 месяц)\n\n*Этап 2 (2 месяца):* Углубление\n- Решение задач\n- Работа с картами\n- Анализ статистики\n\n*Этап 3 (1 месяц):* Итоговый\n- Решение пробников\n- Повторение слабых тем\n- Работа с новыми типами заданий",
                    "tips": [
                        "📌 Работай с атласом ежедневно",
                        "📌 Учи столицы и флаги стран",
                        "📌 Составляй сравнительные таблицы регионов",
                        "📌 Решай задачи на определение времени",
                        "📌 Следи за географическими новостями"
                    ],
                    "changes_2026": "🔔 *Изменения 2026:*\n• Усилен акцент на глобальные проблемы человечества\n• Добавлены задания по геоинформационным системам\n• Включены темы по изменению климата\n• Больше внимания региональной географии России"
                },
                "oge": {
                    "structure": "29 заданий\n\n*Часть 1:* 21 заданиt с кратким ответом\n*Часть 2:* 8 заданиq с развернутым ответом\n\n*Минимальный порог:* 12 баллов\n*Максимальный балл:* 31 балл",
                    "topics": "1. Источники географической информации\n2. Природа Земли и человек\n3. Материки, океаны, народы и страны\n4. Природопользование и экология\n5. География России",
                    "how_to_prepare": "🎯 *Как готовиться к ОГЭ по географии:*\n\n1. *Освоение картографических навыков:*\n   - Чтение физических карт\n   - Работа с масштабом\n   - Определение координат\n   - Чтение тематических карт\n\n2. *Изучение физической географии:*\n   - Оболочки Земли\n   - Климатические пояса\n   - Природные зоны\n   - Рельеф и внутреннее строение\n\n3. *Знание политической карты:*\n   - Столицы и крупные города\n   - Географическое положение стран\n   - Особенности природы и населения\n\n4. *География России:*\n   - Федеративное устройство\n   - Природные условия регионов\n   - Население и хозяйство",
                    "plan": "🎯 *План подготовки:*\n\n*Месяц 1-2:* Физическая география и картография\n*Месяц 3-4:* География материков и стран\n*Месяц 5:* География России\n*Месяц 6:* Природопользование и итоговое повторение",
                    "changes_2026": "🔔 *Изменения 2026:*\n• Больше практических заданий с картами\n• Акцент на экологические проблемы\n• Включены задания по чтению космических снимков\n• Усилен раздел по географии родного края"
                }
            },
            "english": {
                "name": "📓 Английский язык",
                "ege": {
                    "structure": "Письмо + аудирование + чтение + говорение (42 задания)\n\n*Письменная часть:* 38 задания\n*Устная часть:* 4 задания\n\n*Минимальный порог:* 22 балла\n*Максимальный балл:* 100 баллов",
                    "topics": "1. Аудирование (понимание на слух)\n2. Чтение (понимание письменных текстов)\n3. Грамматика и лексика\n4. Письмо (личное письмо и эссе)\n5. Говорение (монолог и диалог)",
                    "how_to_prepare": "🎯 *Как готовиться к ЕГЭ по английскому языку:*\n\n1. *Развитие всех языковых навыков:*\n   - Аудирование: слушайте подкасты, новости\n   - Чтение: читайте статьи, рассказы\n   - Письмо: пишите эссе, письма\n   - Говорение: практикуйте речь\n\n2. *Грамматическая подготовка:*\n   - Изучайте времена глаголов\n   - Усвойте артикли и предлоги\n   - Практикуйте словообразование\n\n3. *Расширение словарного запаса:*\n   - Учите слова по темам\n   - Используйте карточки\n   - Читайте адаптированную литературу\n\n4. *Подготовка к письменной части:*\n   - Учите структуру эссе\n   - Тренируйтесь в написании писем\n   - Изучайте клише и связующие слова\n\n5. *Практика говорения:*\n   - Говорите на английском ежедневно\n   - Записывайте свою речь\n   - Работайте над произношением",
                    "changes_2026": "🔔 *Изменения 2026:*\n• Усилен акцент на коммуникативные навыки\n• Добавлены задания на межкультурную коммуникацию\n• Включены современные темы (технологии, экология)\n• Больше внимания практическому использованию языка"
                },
                "oge": {
                    "structure": "Письмо + аудирование + чтение + говорение\n\n*Аудирование:* 35 заданий\n*Письменная часть:* 38 заданий\n*Устная часть:* 4 задания\n\n*Минимальный порог:* 29 баллов\n*Максимальный балл:* 70 баллов",
                    "how_to_prepare": "🎯 *Как готовиться к ОГЭ по английскому языку:*\n\n1. *Базовое владение языком:*\n   - Освойте базовую грамматику\n   - Выучите необходимый словарный запас\n   - Научитесь понимать простые тексты\n\n2. *Практика аудирования:*\n   - Слушайте адаптированные записи\n   - Смотрите фильмы с субтитрами\n   - Выполняйте упражнения на понимание\n\n3. *Развитие разговорных навыков:*\n   - Говорите на простые темы\n   - Учитесь задавать вопросы\n   - Практикуйте диалоги\n\n4. *Подготовка к письму:*\n   - Учитесь писать короткие тексты\n   - Освойте формат личного письма\n   - Используйте простые конструкции",
                    "changes_2026": "🔔 *Изменения 2026:*\n• Больше практических заданий\n• Акцент на повседневное общение\n• Включены современные темы\n• Усилена устная часть"
                }
            },
            "physics": {
                "name": "⚛️ Физика",
                "ege": {
                    "structure": "26 заданий\n\n*Часть 1:* 20 задания с кратким ответом\n*Часть 2:* 6 заданий с развернутым ответом\n\n*Минимальный порог:* 36 баллов\n*Максимальный балл:* 100 баллов",
                    "topics": "1. Механика (кинематика, динамика, статика, законы сохранения)\n2. Молекулярная физика и термодинамика\n3. Электродинамика (электростатика, постоянный ток, магнитное поле, электромагнитная индукция)\n4. Квантовая физика и элементы астрофизики\n5. Оптика (геометрическая и волновая)\n6. Колебания и волны (механические и электромагнитные)",
                    "how_to_prepare": "🎯 *Как готовиться к ЕГЭ по физике:*\n\n1. *Освоение фундаментальных законов:*\n   - Законы Ньютона, закон сохранения энергии\n   - Законы термодинамики\n   - Законы Ома, Кирхгофа, электромагнитной индукции\n   - Законы фотоэффекта и квантовой физики\n\n2. *Решение качественных задач:*\n   - Анализ физических процессов\n   - Построение графиков\n   - Объяснение явлений\n\n3. *Решение расчетных задач:*\n   - Задачи на применение формул\n   - Задачи с несколькими способами решения\n   - Олимпиадные задачи повышенной сложности\n\n4. *Экспериментальные задания:*\n   - Построение электрических схем\n   - Обработка результатов измерений\n   - Определение погрешностей\n\n5. *Работа с графиками и диаграммами:*\n   - Чтение и анализ графиков\n   - Построение графиков по данным\n   - Интерпретация физических зависимостей",
                    "resources": [
                        "📚 *Учебники:*\n- Мякишев Г.Я. 'Физика 10-11 класс'\n- Касьянов В.А. 'Физика'\n- Громцева О.И. 'Физика. Подготовка к ЕГЭ'",
                        "🌐 *Сайты:*\n- РешуЕГЭ (phys-ege.sdamgia.ru)\n- ФИПИ (fipi.ru)",
                        "🎥 *RuTube каналы:*\n- Физика ОГЭ Умскул"
                    ],
                    "plan": "🎯 *План подготовки:*\n\n*Этап 1 (3 месяца):* Теория и основы\n- Механика (1 месяц)\n- Молекулярная физика и термодинамика (1 месяц)\n- Электродинамика (1 месяц)\n\n*Этап 2 (2 месяца):* Углубление\n- Оптика и колебания\n- Квантовая физика\n- Решение комбинированных задач\n\n*Этап 3 (1 месяц):* Итоговый\n- Решение пробников\n- Работа над экспериментальными заданиями\n- Повторение формул и законов",
                    "tips": [
                        "📌 Выучи все основные формулы наизусть",
                        "📌 Решай задачи по темам, а не подряд",
                        "📌 Внимательно читай условие задачи",
                        "📌 Проверяй размерности в расчетах",
                        "📌 Тренируйся решать задачи на время"
                    ],
                    "changes_2026": "🔔 *Изменения 2026:*\n• Увеличено количество практико-ориентированных задач\n• Добавлены задания на анализ современных технологий\n• Усилен блок по квантовой физике\n• Больше внимания экспериментальным заданиям"
                },
                "oge": {
                    "structure": "22 заданий\n\n*Часть 1:* 16 заданий с кратким ответом (1-16)\n*Часть 2:* 6 заданий с развернутым ответом (17-22)\n\n*Минимальный порог:* 10 баллов\n*Максимальный балл:* 39 баллов",
                    "topics": "1. Механические явления\n2. Тепловые явления\n3. Электромагнитные явления\n4. Квантовые явления\n5. Методы научного познания",
                    "how_to_prepare": "🎯 *Как готовиться к ОГЭ по физике:*\n\n1. *Освоение основных понятий:*\n   - Физические величины и их единицы\n   - Основные законы физики\n   - Физические явления и их объяснение\n\n2. *Решение задач:*\n   - Простые расчетные задачи\n   - Качественные задачи на объяснение\n   - Задачи на чтение графиков\n\n3. *Работа с экспериментами:*\n   - Описание опытов\n   - Обработка результатов\n   - Формулировка выводов\n\n4. *Применение знаний:*\n   - Объяснение бытовых явлений\n   - Понимание принципов работы приборов\n   - Безопасность в быту",
                    "resources": [
                        "📚 *Учебники:*\n- Перышкин А.В. 'Физика 7-9 класс'\n- Лукашик В.И. 'Сборник задач по физике'\n- Камзеева Е.Е. 'ОГЭ. Физика'",
                        "🌐 *Сайты:*\n- СдамГИА (phys-oge.sdamgia.ru)\n- ФИПИ (fipi.ru)",
                        "🎥 *RuTube каналы:*\n- Физика ОГЭ Умскул"
                    ],
                    "plan": "🎯 *План подготовки:*\n\n*Месяц 1-2:* Механика и тепловые явления\n*Месяц 3-4:* Электромагнитные явления\n*Месяц 5:* Квантовые явления и эксперименты\n*Месяц 6:* Итоговое повторение и пробники",
                    "tips": [
                        "📌 Учи формулы и их применение",
                        "📌 Тренируйся решать задачи на время",
                        "📌 Внимательно читай условия",
                        "📌 Проверяй единицы измерения",
                        "📌 Решай задачи из разных источников"
                    ],
                    "changes_2026": "🔔 *Изменения 2026:*\n• Больше практико-ориентированных заданий\n• Акцент на понимание физических явлений\n• Включены задания по основам безопасности\n• Усилен блок экспериментальных заданий"
                }
            },
            "informatics": {
                "name": "💻 Информатика",
                "ege": {
                    "structure": "27 заданий\n\n*Часть 1:* 23 задания с кратким ответом (1-23)\n*Часть 2:* 4 задания с развернутым ответом (24-27) - программирование\n\n*Минимальный порог:* 40 баллов\n*Максимальный балл:* 100 баллов",
                    "topics": "1. Информация и её кодирование\n2. Моделирование и компьютерный эксперимент\n3. Системы счисления\n4. Логика и алгоритмы\n5. Элементы теории алгоритмов\n6. Программирование\n7. Архитектура компьютеров и компьютерных сетей\n8. Обработка числовой информации\n9. Технологии поиска и хранения информации",
                    "how_to_prepare": "🎯 *Как готовиться к ЕГЭ по информатике:*\n\n1. *Освоение теоретических основ:*\n   - Системы счисления\n   - Алгебра логики\n   - Теория графов\n   - Кодирование информации\n\n2. *Программирование:*\n   - Язык Python (основной для ЕГЭ)\n   - Алгоритмы и структуры данных\n   - Работа с файлами\n   - Обработка массивов\n\n3. *Решение алгоритмических задач:*\n   - Поиск оптимальных решений\n   - Динамическое программирование\n   - Рекурсия\n   - Обработка строк\n\n4. *Работа с компьютером (на реальном экзамене):*\n   - Среда программирования\n   - Отладка программ\n   - Тестирование решений\n\n5. *Решение задач на графы и логику:*\n   - Поиск путей в графах\n   - Минимальное остовное дерево\n   - Логические уравнения",
                    "resources": [
                        "📚 *Учебники:*\n- Поляков К.Ю. 'Информатика. ЕГЭ'\n- Ушаков Д.М. 'ЕГЭ. Информатика'\n- Богомолова О.Б. 'Задачи по программированию'",
                        "🌐 *Сайты:*\n- РешуЕГЭ (inf-ege.sdamgia.ru)\n- Поляков (kpolyakov.spb.ru)\n- Codeforces\n- LeetCode",
                        "💻 *Среды программирования:*\n- IDLE Python\n- PyCharm\n- Visual Studio Code",
                        "🎥 *RuTube каналы:*\n- Информатик БУ\n- Умскул Информатика\n- ЕГЭ Информатика с Евгением Джобсом"
                    ],
                    "plan": "🎯 *План подготовки:*\n\n*Этап 1 (2 месяца):* Теория и основы\n- Системы счисления, логика, кодирование (1 месяц)\n- Основы программирования на Python (1 месяц)\n\n*Этап 2 (3 месяца):* Программирование\n- Алгоритмы и структуры данных (1.5 месяца)\n- Задачи ЕГЭ по программированию (1.5 месяца)\n\n*Этап 3 (1 месяц):* Итоговый\n- Решение полных вариантов\n- Работа на компьютере\n- Пробный экзамен в условиях, близких к реальным",
                    "tips": [
                        "📌 Учи Python - это основной язык на ЕГЭ",
                        "📌 Решай задачи на алгоритмы ежедневно",
                        "📌 Тренируй скорость набора кода",
                        "📌 Изучи стандартные библиотеки Python",
                        "📌 Проверяй код на краевые случаи"
                    ],
                    "changes_2026": "🔔 *Изменения 2026:*\n• Увеличено количество задач на программирование\n• Добавлены задания на анализ данных\n• Включены основы искусственного интеллекта\n• Больше внимания алгоритмическому мышлению"
                },
                "oge": {
                    "structure": "16 заданий\n\n*Часть 1:* 10 заданий с кратким ответом (1-10)\n*Часть 2:* 6 заданий с развернутым ответом (11-16) - практическая часть на компьютере\n\n*Минимальный порог:* 5 баллов\n*Максимальный балл:* 21 балл",
                    "topics": "1. Представление информации\n2. Обработка информации\n3. Основы алгоритмизации\n4. Начала программирования\n5. Информационные и коммуникационные технологии",
                    "how_to_prepare": "🎯 *Как готовиться к ОГЭ по информатике:*\n\n1. *Освоение основных понятий:*\n   - Информация и информационные процессы\n   - Файловая система\n   - Основы работы с ОС\n   - Текстовые и графические редакторы\n\n2. *Алгоритмизация:*\n   - Блок-схемы\n   - Исполнители\n   - Основные алгоритмические конструкции\n\n3. *Программирование:*\n   - Язык Кумир или Python\n   - Простые программы\n   - Обработка данных\n\n4. *Практическая работа:*\n   - Работа с текстовыми документами\n   - Создание презентаций\n   - Обработка табличных данных",
                    "resources": [
                        "📚 *Учебники:*\n- Босова Л.Л. 'Информатика 7-9 класс'\n- Златопольский Д.М. 'Задачи по информатике'\n- Ушаков Д.М. 'Типовые варианты экзаменационных заданий ОГЭ по информатике'",
                        "🌐 *Сайты:*\n- СдамГИА (inf-oge.sdamgia.ru)\n- ФИПИ (fipi.ru)",
                        "🎥 *RuTube каналы:*\n- Информатика ОГЭ\n- Умскул ОГЭ Информатика"
                    ],
                    "plan": "🎯 *План подготовки:*\n\n*Месяц 1-2:* Теория и основы\n- Информация и системы счисления\n- Основы алгоритмизации\n\n*Месяц 3-4:* Программирование\n- Язык Кумир или Python\n- Решение задач\n\n*Месяц 5:* Практическая часть\n- Работа с офисными приложениями\n- Создание документов и презентаций\n\n*Месяц 6:* Итоговое повторение и пробники",
                    "tips": [
                        "📌 Учись работать с разными типами файлов",
                        "📌 Тренируйся создавать презентации",
                        "📌 Освой основы программирования",
                        "📌 Решай задачи на исполнителей",
                        "📌 Практикуйся на компьютере"
                    ],
                    "changes_2026": "🔔 *Изменения 2026:*\n• Больше практических заданий на компьютере\n• Акцент на цифровую грамотность\n• Включены основы кибербезопасности\n• Усилен блок по обработке информации"
                }
            }
        }
        
        self.general_tips = {
            "time_management": [
                "🍅 *Техника Помодоро:*\nРаботай 25 минут, отдыхай 5 минут. После 4 циклов - длинный перерыв 15-30 минут.\n\n*Почему работает:*\n• Сохраняет концентрацию\n• Предотвращает выгорание\n• Улучшает оценку времени\n• Повышает продуктивность на 40%",
                "📊 *Матрица Эйзенхауэра:*\nРаздели задачи на 4 квадранта:\n\n1. 🔴 *Важно и срочно*\n   - Кризисы, дедлайны\n   - Делай СЕЙЧАС\n\n2. 🟢 *Важно, но не срочно*\n   - Обучение, планирование\n   - ЗАПЛАНИРУЙ\n\n3. 🟡 *Срочно, но не важно*\n   - Некоторые звонки, встречи\n   - ДЕЛЕГИРУЙ\n\n4. ⚫ *Не срочно и не важно*\n   - Соцсени, пустая трата времени\n   - УДАЛИ"
            ],
            "study_techniques": [
                "🧠 *Техника Фейнмана:*\n4 шага к пониманию:\n\n1. Выбери тему\n2. Объясни её так, будто учишь 10-летнего ребенка\n3. Обнаружь пробелы в понимании\n4. Упрости объяснение\n\n*Результат:* Глубокое понимание вместо механического запоминания",
                "📝 *Интервальное повторение:*\nПовторяй материал через:\n• 20 минут после изучения\n• 1 день\n• 3 дня\n• 1 неделю\n• 1 месяц\n\n*Эффект:* Переход информации в долговременную память"
            ],
            "exam_preparation": [
                "📅 *Стратегия подготовки:*\n• Начинай за 6-8 месяцев\n• Первые 3 месяца: теория\n• Следующие 2 месяца: практика\n• Последний месяц: пробники\n\n*Еженедельный план:*\n- 4-5 часов в будни\n- 6-8 часов в выходные",
                "✅ *Работа с пробниками:*\n1. Решай на время\n2. Анализируй ошибки\n3. Веди дневник ошибок\n4. Повторяй проблемные темы\n5. Делай работу над ошибками"
            ],
            "motivation": [
                "🚀 *Мотивационные техники:*\n\n1. *Метод «Маленьких шагов»*\n   Разбей большую цель на маленькие задачи\n   Каждое выполнение - маленькая победа!\n\n2. *Визуализация успеха*\n   Представь, как сдаешь экзамен на высокий балл\n   Нарисуй свою цель и повесь на видное место\n\n3. *Система поощрений*\n   За каждый достигнутый этап - награда\n   Фильм, прогулка, любимая еда\n\n4. *Техника «5 секунд»*\n   Хочешь отложить дело? Считай: 5-4-3-2-1-ДЕЙСТВУЙ!\n\n5. *Найди «зачем»*\n   Зачем тебе высший балл?\n   Поступление в ВУЗ мечты? Будущая карьера?",
                "💪 *Преодоление прокрастинации:*\n\n🔹 *Правило 2-х минут*\n   Если задача занимает меньше 2 минут - делай сразу\n\n🔹 *Техника «Поедания лягушки»*\n   Самую неприятную задачу делай первой\n\n🔹 *Удалить отвлекающие факторы*\n   Выключи уведомления, убери телефон\n\n🔹 *Работа в группе*\n   Найдите партнера для взаимного контроля\n\n🔹 *Фокус на процессе, а не результате*\n   Не «получить 100 баллов», а «решать по 5 задач в день»"
            ],
            "goal_setting": [
                "🎯 *SMART-цели для учебы:*\n\nS - Конкретная (Specific)\n❌ «Хорошо сдать ЕГЭ»\n✅ «Набрать 85+ баллов по математике»\n\nM - Измеримая (Measurable)\n❌ «Учить английский»\n✅ «Выучить 50 новых слов в неделю»\n\nA - Достижимая (Achievable)\n❌ «Выучить весь учебник за неделю»\n✅ «Пройти 2 главы за неделю»\n\nR - Релевантная (Relevant)\n❌ «Учить то, что не пригодится»\n✅ «Фокусироваться на темах ЕГЭ»\n\nT - Ограниченная по времени (Time-bound)\n❌ «Когда-нибудь подготовиться»\n✅ «Готовиться 2 часа ежедневно до 1 мая»",
                "📈 *Постановка учебных целей:*\n\n1. *Долгосрочные цели* (к концу года)\n   - Поступить в определенный ВУЗ\n   - Набрать конкретные баллы по ЕГЭ\n\n2. *Среднесрочные цели* (квартальные)\n   - Пройти определенные темы\n   - Решить N пробников\n\n3. *Краткосрочные цели* (ежемесячные/еженедельные)\n   - Ежедневная норма занятий\n   - Конкретные темы на неделю\n\n4. *Ежедневные цели*\n   - Конкретные задачи на сегодня\n   - Время начала и окончания"
            ],
            "rest_breaks": [
                "😴 *Наука об отдыхе:*\n\n1. *Короткие перерывы (5-10 минут)*\n   • Каждые 45-50 минут работы\n   • Встать, потянуться, пройтись\n   • Посмотреть вдаль (отдых для глаз)\n   • Выпить воды\n\n2. *Обеденный перерыв (30-60 минут)*\n   • Полноценный прием пищи\n   • Отрыв от рабочего места\n   • Прогулка на свежем воздухе\n\n3. *Длительные перерывы*\n   • 1 выходной в неделю БЕЗ учебы\n   • Смена деятельности\n   • Хобби и увлечения",
                "⚡ *Эффективные техники отдыха:*\n\n🔸 *Техника «20-20-20» для глаз*\n   Каждые 20 минут смотри на объект в 20 метрах в течение 20 секунд\n\n🔸 *Дыхательные упражнения*\n   4-7-8 дыхание: вдох 4 сек, задержка 7 сек, выдох 8 сек\n\n🔸 *Физическая активность*\n   5-10 минут легкой зарядки каждый час\n\n🔸 *Ментальный отдых*\n   Медитация 5-10 минут\n   Слушание спокойной музыки\n\n🔸 *Сон*\n   7-9 часов качественного сна\n   Режим дня\n   Темная комната для сна"
            ]
        }
    
    def get_subject_info(self, subject_key, exam_type):
        """Получить информацию по предмету"""
        subject = self.subjects.get(subject_key)
        if not subject:
            return "Предмет не найден"
        
        exam_info = subject.get(exam_type)
        if not exam_info:
            return f"Информация по {exam_type.upper()} для этого предмета пока не добавлена"
        
        text = f"*{subject['name']} - {exam_type.upper()} 2026*\n\n"
        
        if exam_info.get('structure'):
            text += f"📋 *Структура экзамена:*\n{exam_info['structure']}\n\n"
        
        if exam_info.get('topics'):
            text += f"📚 *Основные темы:*\n{exam_info['topics']}\n\n"
        
        if exam_info.get('how_to_prepare'):
            text += f"🎯 *Как готовиться:*\n{exam_info['how_to_prepare']}\n\n"
        
        if exam_info.get('resources'):
            text += "💡 *Ресурсы для подготовки:*\n"
            for resource in exam_info['resources']:
                text += f"{resource}\n\n"
        
        if exam_info.get('plan'):
            text += f"📅 *План подготовки:*\n{exam_info['plan']}\n\n"
        
        if exam_info.get('tips'):
            text += "🌟 *Советы по подготовке:*\n"
            for tip in exam_info['tips']:
                text += f"{tip}\n\n"
        
        if exam_info.get('changes_2026'):
            text += f"🔔 *Изменения 2026:*\n{exam_info['changes_2026']}\n\n"
        
        text += "📌 *Начинай готовиться сейчас!* 🚀"
        
        return text
    
    def get_tips(self, category):
        """Получить советы по категории"""
        if category == "all_tips":
            return self.get_all_tips()
        
        tips = self.general_tips.get(category, [])
        if not tips:
            return "Советы по этой теме пока не добавлены"
        
        text = ""
        if category == "time_management":
            text = "⏰ *Техники тайм-менеджмента:*\n\n"
        elif category == "study_techniques":
            text = "🎓 *Методы эффективного обучения:*\n\n"
        elif category == "exam_preparation":
            text = "📚 *Подготовка к экзаменам:*\n\n"
        elif category == "motivation":
            text = "🚀 *Мотивация и преодоление прокрастинации:*\n\n"
        elif category == "goal_setting":
            text = "🎯 *Постановка целей:*\n\n"
        elif category == "rest_breaks":
            text = "😴 *Отдых и перерывы:*\n\n"
        
        for i, tip in enumerate(tips, 1):
            text += f"{tip}\n\n"
        
        return text
    
    def get_all_tips(self):
        """Получить все советы"""
        text = """🌟 *ВСЕ СОВЕТЫ ПО ТАЙМ-МЕНЕДЖМЕНТУ И УЧЕБЕ*

*🎯 ГЛАВНЫЕ ПРИНЦИПЫ УСПЕШНОЙ УЧЕБЫ:*

1. *СИСТЕМАТИЧНОСТЬ*
   • Занимайся регулярно, а не перед экзаменом
   • Лучше 30 минут ежедневно, чем 5 часов раз в неделю
   • Создай расписание и следуй ему

2. *АКТИВНОЕ ОБУЧЕНИЕ*
   • Не просто читай, а конспектируй
   • Объясняй материал вслух
   • Решай практические задачи
   • Задавай вопросы и ищи ответы

3. *СМЕНА ДЕЯТЕЛЬНОСТИ*
   • Чередуй разные предметы
   • Меняй виды деятельности (чтение, письмо, решение задач)
   • Делай перерывы для лучшего запоминания

*⏰ ТЕХНИКИ ТАЙМ-МЕНЕДЖМЕНТА:*

1. *🍅 ТЕХНИКА ПОМОДОРО*
   • 25 минут работы → 5 минут отдыха
   • После 4 циклов → 15-30 минут перерыв
   • Улучшает концентрацию и предотвращает выгорание

2. *📊 МАТРИЦА ЭЙЗЕНХАУЭРА*
   • Важно и срочно → делай СЕЙЧАС
   • Важно, но не срочно → ЗАПЛАНИРУЙ
   • Срочно, но не важно → ДЕЛЕГИРУЙ
   • Не срочно и не важно → УДАЛИ

3. *🎯 МЕТОД 1-3-5*
   • 1 большая задача в день
   • 3 средние задачи
   • 5 маленьких задач
   • Помогает реалистично планировать день

*🎓 МЕТОДЫ ЭФФЕКТИВНОГО ОБУЧЕНИЯ:*

1. *🧠 ТЕХНИКА ФЕЙНМАНА*
   • Выбери тему
   • Объясни её так, будто учишь ребенка
   • Найди пробелы в понимании
   • Упрости объяснение

2. *📝 ИНТЕРВАЛЬНОЕ ПОВТОРЕНИЕ*
   • Повторяй материал через:
      - 20 минут после изучения
      - 1 день
      - 3 дня
      - 1 неделю
      - 1 месяц

3. *🎨 МЕНТАЛЬНЫЕ КАРТЫ*
   • Визуализируй информацию
   • Создавай связи между понятиями
   • Используй цвета и изображения

*📚 ПОДГОТОВКА К ЭКЗАМЕНАМ:*

1. *📅 ДОЛГОСРОЧНОЕ ПЛАНИРОВАНИЕ*
   • Начинай за 6-8 месяцев до экзамена
   • Первые 3 месяца: теория
   • Следующие 2 месяца: практика
   • Последний месяц: пробники

2. *✅ РАБОТА С ПРОБНИКАМИ*
   • Решай на время
   • Анализируй ошибки
   • Веди дневник ошибок
   • Повторяй проблемные темы

3. *🧪 ЭКЗАМЕНАЦИОННЫЕ СТРАТЕГИИ*
   • Начни с простых заданий
   • Распредели время
   • Проверяй ответы
   • Не зацикливайся на сложных задачах

*🚀 МОТИВАЦИЯ И ПРОКРАСТИНАЦИЯ:*

1. *💪 ПРЕОДОЛЕНИЕ ПРОКРАСТИНАЦИИ*
   • Правило 2-х минут: если задача занимает меньше 2 минут → делай сразу
   • Техника «поедания лягушки»: самая неприятную задачу делай первой
   • Удали отвлекающие факторы: выключи уведомления, убери телефон

2. *🎯 СИСТЕМА ПООЩРЕНИЙ*
   • За каждый достигнутый этап → награда
   • Фильм, прогулка, любимая еда
   • Маленькие победы ведут к большим успехам

3. *🔍 НАЙДИ СВОЙ «ЗАЧЕМ»*
   • Зачем тебе высший балл?
   • Поступление в ВУЗ мечты?
   • Будущая карьера?
   • Самореализация?

*🎯 ПОСТАНОВКА ЦЕЛЕЙ:*

1. *SMART-ЦЕЛИ*
   • S - Конкретная
   • M - Измеримая
   • A - Достижимая
   • R - Релевантная
   • T - Ограниченная по времени

2. *УРОВНИ ЦЕЛЕЙ*
   • Долгосрочные (год)
   • Среднесрочные (квартал)
   • Краткосрочные (месяц/неделя)
   • Ежедневные

*😴 ОТДЫХ И ПЕРЕРЫВЫ:*

1. *🔬 НАУКА ОБ ОТДЫХЕ*
   • Мозгу нужны перерывы для обработки информации
   • Каждые 45-50 минут → 5-10 минут отдыха
   • Техника 20-20-20 для глаз

2. *💤 КАЧЕСТВЕННЫЙ СОН*
   • 7-9 часов сна ежедневно
   • Режим дня
   • Темная комната для сна
   • Никаких гаджетов перед сном

3. *🍎 ЗДОРОВЫЙ ОБРАЗ ЖИЗНИ*
   • Правильное питание
   • Физическая активность
   • Прогулки на свежем воздухе
   • Медитация и релаксация

*💡 ДОПОЛНИТЕЛЬНЫЕ ЛАЙФХАКИ:*

1. *📖 ОРГАНИЗАЦИЯ РАБОЧЕГО МЕСТА*
   • Хорошее освещение
   • Удобный стул
   • Порядок на столе
   • Отсутствие отвлекающих предметов

2. *🧪 ЭКСПЕРИМЕНТИРУЙ*
   • Найди свой оптимальный режим
   • Пробуй разные техники
   • Анализируй, что работает для тебя

3. *🤝 РАБОТА В ГРУППЕ*
   • Обсуждай сложные темы
   • Объясняй материал другим
   • Мотивируй друг друга

4. *📱 ЦИФРОВЫЕ ИНСТРУМЕНТЫ*
   • Приложения для тайм-менеджмента
   • Онлайн-курсы и тренажеры
   • Образовательные YouTube-каналы

*🎯 ЗАПОМНИ:*
• Успех = Системность × Регулярность × Качество
• Не сравнивай себя с другими
• Каждый день делай маленький шаг к цели
• Верь в себя и свои силы!

💪 *ТЫ СПРАВИШЬСЯ! У ТЕБЯ ВСЕ ПОЛУЧИТСЯ!* 🚀
"""
        return text

# Создаем базу экзаменов
exam_db = ExamDatabase()

# Создаем продвинутую локальную нейросеть
ai_study_assistant = AdvancedLocalAI()

# =================== МЕНЕДЖЕР ЗАДАЧ ===================

class TaskManager:
    def __init__(self):
        self.tasks_file = "tasks.json"
        self.stats_file = "stats.json"
        self.load_data()
    
    def load_data(self):
        """Загрузка данных из файлов"""
        if os.path.exists(self.tasks_file):
            with open(self.tasks_file, 'r', encoding='utf-8') as f:
                self.tasks = json.load(f)
        else:
            self.tasks = {}
        
        if os.path.exists(self.stats_file):
            with open(self.stats_file, 'r', encoding='utf-8') as f:
                self.stats = json.load(f)
        else:
            self.stats = {}
    
    def save_data(self):
        """Сохранение данных в файлы"""
        with open(self.tasks_file, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=2)
        
        with open(self.stats_file, 'w', encoding='utf-8') as f:
            json.dump(self.stats, f, ensure_ascii=False, indent=2)
    
    def add_task(self, user_id: int, task_text: str, task_date: str, task_time: str = None, subject: str = None):
        """Добавление новой задачи"""
        if str(user_id) not in self.tasks:
            self.tasks[str(user_id)] = []
        
        task_id = len(self.tasks[str(user_id)]) + 1
        task = {
            "id": task_id,
            "text": task_text,
            "date": task_date,
            "time": task_time,
            "subject": subject,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "completed": False,
            "reminder_sent": False
        }
        
        self.tasks[str(user_id)].append(task)
        self.save_data()
        
        # Обновляем статистику
        if str(user_id) not in self.stats:
            self.stats[str(user_id)] = {
                "total_tasks": 0,
                "completed_tasks": 0,
                "last_active": datetime.now().strftime("%Y-%m-%d")
            }
        
        self.stats[str(user_id)]["total_tasks"] += 1
        self.stats[str(user_id)]["last_active"] = datetime.now().strftime("%Y-%m-%d")
        self.save_data()
        
        return task
    
    def get_tasks_for_today(self, user_id: int):
        """Получение задач на сегодня"""
        today = datetime.now().strftime("%Y-%m-%d")
        user_tasks = self.tasks.get(str(user_id), [])
        return [task for task in user_tasks if task["date"] == today]
    
    def get_tasks_for_week(self, user_id: int):
        """Получение задач на неделю"""
        today = datetime.now()
        week_end = today + timedelta(days=7)
        
        user_tasks = self.tasks.get(str(user_id), [])
        tasks_for_week = []
        
        for task in user_tasks:
            try:
                task_date = datetime.strptime(task["date"], "%Y-%m-%d")
                if today <= task_date <= week_end:
                    tasks_for_week.append(task)
            except:
                continue
        
        return tasks_for_week
    
    def complete_task(self, user_id: int, task_id: int):
        """Отметка задачи как выполненной"""
        user_tasks = self.tasks.get(str(user_id), [])
        for task in user_tasks:
            if task["id"] == task_id:
                task["completed"] = True
                
                # Обновляем статистику
                if str(user_id) in self.stats:
                    self.stats[str(user_id)]["completed_tasks"] += 1
                
                self.save_data()
                return True
        return False
    
    def delete_task(self, user_id: int, task_id: int):
        """Удаление задачи"""
        if str(user_id) not in self.tasks:
            return False
        
        # Ищем задачу
        task_found = False
        for i, task in enumerate(self.tasks[str(user_id)]):
            if task["id"] == task_id:
                del self.tasks[str(user_id)][i]
                task_found = True
                break
        
        if task_found:
            # Обновляем статистику
            if str(user_id) in self.stats:
                self.stats[str(user_id)]["total_tasks"] = len(self.tasks[str(user_id)])
                # Если задача была выполнена, уменьшаем счетчик выполненных
                if task["completed"]:
                    self.stats[str(user_id)]["completed_tasks"] = max(0, self.stats[str(user_id)]["completed_tasks"] - 1)
            
            self.save_data()
            return True
        
        return False
    
    def get_statistics(self, user_id: int):
        """Получение статистики пользователя"""
        stats = self.stats.get(str(user_id), {
            "total_tasks": 0,
            "completed_tasks": 0,
            "last_active": "Не было активности"
        })
        
        user_tasks = self.tasks.get(str(user_id), [])
        today_tasks = self.get_tasks_for_today(user_id)
        week_tasks = self.get_tasks_for_week(user_id)
        
        # Рассчитываем дополнительную статистику
        total_tasks = len(user_tasks)
        completed_tasks = len([t for t in user_tasks if t.get("completed", False)])
        completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        
        # Определяем уровень продуктивности
        if completion_rate >= 80:
            productivity_level = "🏆 Отличная продуктивность!"
        elif completion_rate >= 60:
            productivity_level = "🥈 Хорошая продуктивность"
        elif completion_rate >= 40:
            productivity_level = "🥉 Средняя продуктивность"
        else:
            productivity_level = "📉 Нужно улучшить"
        
        stats.update({
            "total_tasks_current": total_tasks,
            "completed_tasks_current": completed_tasks,
            "completion_rate": completion_rate,
            "today_tasks": len(today_tasks),
            "week_tasks": len(week_tasks),
            "productivity_level": productivity_level
        })
        
        return stats

# Создаем менеджер задач
task_manager = TaskManager()

# Хранилище для временных данных пользователей
user_states = {}

# =================== СИСТЕМА НАПОМИНАНИЙ ===================

class ReminderSystem:
    def __init__(self, bot, task_manager):
        self.bot = bot
        self.task_manager = task_manager
        self.running = False
    
    def start(self):
        """Запуск системы напоминаний"""
        self.running = True
        reminder_thread = threading.Thread(target=self.check_reminders, daemon=True)
        reminder_thread.start()
        print("🔔 Система напоминаний запущена")
    
    def check_reminders(self):
        """Проверка напоминаний"""
        while self.running:
            try:
                now = datetime.now()
                current_time_str = now.strftime("%H:%M")
                current_date_str = now.strftime("%Y-%m-%d")
                
                print(f"🔍 Проверка напоминаний в {current_time_str}...")
                
                # Проверяем задачи всех пользователей
                for user_id_str, tasks in task_manager.tasks.items():
                    user_id = int(user_id_str)
                    
                    for task in tasks:
                        # Проверяем только активные задачи с временем
                        if (task.get("time") and 
                            not task.get("reminder_sent", False) and 
                            not task.get("completed", False) and
                            task.get("date") == current_date_str):
                            
                            try:
                                task_time = task["time"]
                                task_datetime_str = f"{task['date']} {task_time}"
                                task_datetime = datetime.strptime(task_datetime_str, "%Y-%m-%d %H:%M")
                                
                                # Рассчитываем время за час до события
                                reminder_time = task_datetime - timedelta(hours=1)
                                
                                # Если текущее время совпадает с временем напоминания (±2 минуты)
                                if abs((now - reminder_time).total_seconds()) <= 120:
                                    # Отправляем напоминание
                                    reminder_text = f"""
⏰ *НАПОМИНАНИЕ!*

Через 1 час начинается:
📝 *{task['text']}*

📍 *Детали:*
• Дата: {task['date']}
• Время: {task_time}
• Предмет: {task.get('subject', 'Не указан')}

🎯 *Подготовься заранее!*
💡 *Совет:* Проверь все материалы, приготовь тетрадь и ручку.
"""
                                    
                                    try:
                                        self.bot.send_message(user_id, reminder_text, parse_mode='Markdown')
                                        print(f"📨 Отправлено напоминание пользователю {user_id} о задаче '{task['text'][:20]}...'")
                                        
                                        # Помечаем, что напоминание отправлено
                                        task["reminder_sent"] = True
                                        task_manager.save_data()
                                    except Exception as send_error:
                                        print(f"❌ Ошибка отправки напоминания пользователю {user_id}: {send_error}")
                                
                            except Exception as e:
                                print(f"⚠️ Ошибка при обработке задачи {task.get('id')}: {e}")
                                continue
                
                # Проверяем каждую минуту для точности
                time.sleep(60)
                
            except Exception as e:
                print(f"❌ Ошибка в системе напоминаний: {e}")
                time.sleep(60)
    
    def stop(self):
        """Остановка системы напоминаний"""
        self.running = False

# Создаем систему напоминаний
reminder_system = ReminderSystem(bot, task_manager)

# =================== ОСНОВНЫЕ ОБРАБОТЧИКИ ===================

@bot.message_handler(commands=['start', 'help'])
def start(message):
    """Главное меню"""
    user = message.from_user
    welcome_text = f"""
👋 *Привет, {user.first_name}! Я Тимми – твой помощник по тайм-менеджменту!*

✨ *Я умею:*
✅ Добавлять и напоминать о задачах (за 1 час до события!)
✅ Помогать с подготовкой к ЕГЭ/ОГЭ по всем предметам (актуально на 2026 год!)
✅ Делиться лайфхаками и советами по учебе
✅ Отвечать на вопросы об учебе через продвинутого ИИ помощника (огромная база знаний!)
✅ Показывать статистику и прогресс
✅ Управлять задачами (отмечать выполнение, удалять)

👇 *Выбери действие из меню ниже:*"""
    
    # Создаем клавиатуру главного меню
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [
        "➕ Добавить задачу",
        "📋 Мои задачи", 
        "📚 Подготовка к ЕГЭ/ОГЭ",
        "💡 Лайфхаки и советы",
        "🤖 ИИ помощник (Тимми)",
        "📊 Статистика и прогресс",
        "⚙️ Главное меню"
    ]
    keyboard.add(*buttons)
    
    bot.send_message(message.chat.id, welcome_text, 
                     parse_mode='Markdown', reply_markup=keyboard)

# =================== ДОБАВЛЕНИЕ ЗАДАЧ ===================

@bot.message_handler(func=lambda message: message.text == "➕ Добавить задачу")
def add_task_start(message):
    """Начало добавления задачи"""
    user_states[message.chat.id] = {'state': 'waiting_task_text'}
    
    msg = bot.send_message(message.chat.id, 
                          "✍️ *Напиши задачу, которую надо добавить*\n\n"
                          "📌 *Примеры:*\n"
                          "• Репетитор по математике завтра в 19:00\n"
                          "• Сделать домашку по русскому\n"
                          "• Повторить формулы по физике перед контрольной\n"
                          "• Подготовиться к пробнику ЕГЭ 15 мая в 10:00\n\n"
                          "⏰ *Напоминание:* Я пришлю уведомление за 1 час до события!",
                          parse_mode='Markdown')
    
    bot.register_next_step_handler(msg, process_task_text)

def process_task_text(message):
    """Обработка текста задачи"""
    user_id = message.chat.id
    task_text = message.text
    
    if user_id not in user_states:
        user_states[user_id] = {}
    
    user_states[user_id]['task_text'] = task_text
    user_states[user_id]['state'] = 'waiting_task_date'
    
    # Создаем inline-клавиатуру для выбора даты
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    
    # Добавляем кнопки на сегодня, завтра и послезавтра
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    day_after = today + timedelta(days=2)
    
    keyboard.add(
        types.InlineKeyboardButton(f"📅 Сегодня ({today.strftime('%d.%m')})", callback_data="date_today"),
        types.InlineKeyboardButton(f"📆 Завтра ({tomorrow.strftime('%d.%m')})", callback_data="date_tomorrow")
    )
    keyboard.add(
        types.InlineKeyboardButton(f"🗓️ Послезавтра ({day_after.strftime('%d.%m')})", callback_data="date_day_after"),
        types.InlineKeyboardButton("📝 Без даты", callback_data="date_none")
    )
    keyboard.add(
        types.InlineKeyboardButton("📅 Выбрать другую дату", callback_data="date_custom")
    )
    
    bot.send_message(user_id, 
                     "📅 *Выбери срок выполнения задачи:*\n\n"
                     "💡 *Совет:* Выбери дату, чтобы я мог напомнить тебе за 1 час до события!",
                     parse_mode='Markdown',
                     reply_markup=keyboard)

def process_task_date(user_id, date_type):
    """Обработка выбора даты"""
    today = datetime.now()
    
    if date_type == "today":
        task_date = today.strftime("%Y-%m-%d")
    elif date_type == "tomorrow":
        task_date = (today + timedelta(days=1)).strftime("%Y-%m-%d")
    elif date_type == "day_after":
        task_date = (today + timedelta(days=2)).strftime("%Y-%m-%d")
    elif date_type == "week":
        task_date = (today + timedelta(days=7)).strftime("%Y-%m-%d")
    else:
        task_date = today.strftime("%Y-%m-%d")
    
    if user_id in user_states and 'task_text' in user_states[user_id]:
        task_text = user_states[user_id]['task_text']
        
        # Пытаемся извлечь время из текста задачи
        import re
        time_match = None
        time_patterns = [
            r'в\s+(\d{1,2}[:.]?\d{0,2})',
            r'(\d{1,2}[:.]\d{2})\s*',
            r'в\s+(\d{1,2})\s*(часов|час|ч)'
        ]
        
        for pattern in time_patterns:
            match = re.search(pattern, task_text.lower())
            if match:
                time_match = match.group(1)
                if ':' not in time_match and '.' not in time_match:
                    # Если время указано просто цифрой (например "в 19")
                    time_match = time_match + ':00'
                else:
                    time_match = time_match.replace('.', ':')
                break
        
        # Если время не найдено, спрашиваем у пользователя
        if not time_match:
            user_states[user_id]['task_date'] = task_date
            user_states[user_id]['state'] = 'waiting_task_time'
            
            keyboard = types.InlineKeyboardMarkup(row_width=3)
            # Добавляем кнопки с популярным временем
            times = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", 
                    "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"]
            buttons = [types.InlineKeyboardButton(time, callback_data=f"time_{time}") for time in times]
            
            # Добавляем кнопки построчно
            for i in range(0, len(buttons), 3):
                keyboard.add(*buttons[i:i+3])
            
            keyboard.add(types.InlineKeyboardButton("🕐 Без времени", callback_data="time_none"))
            
            bot.send_message(user_id,
                            "🕐 *Укажи время выполнения задачи:*\n\n"
                            "Выбери из предложенных или напиши время в формате ЧЧ:ММ\n"
                            "Например: 14:30",
                            parse_mode='Markdown',
                            reply_markup=keyboard)
            return None
        
        # Определяем предмет по ключевым словам
        subject = None
        subject_keywords = {
            "математик": "Математика",
            "алгебр": "Математика",
            "геометр": "Математика",
            "русск": "Русский язык",
            "сочинен": "Русский язык",
            "изложен": "Русский язык",
            "физик": "Физика",
            "информатик": "Информатика",
            "программирован": "Информатика",
            "английск": "Английский язык",
            "english": "Английский язык",
            "обществознан": "Обществознание",
            "истори": "История",
            "биолог": "Биология",
            "хими": "Химия",
            "литератур": "Литература",
            "географи": "География",
            "репетитор": "Репетитор",
            "урок": "Урок",
            "занятие": "Занятие",
            "лекция": "Лекция",
            "семинар": "Семинар"
        }
        
        for keyword, subj in subject_keywords.items():
            if keyword in task_text.lower():
                subject = subj
                break
        
        # Добавляем задачу
        task = task_manager.add_task(user_id, task_text, task_date, time_match, subject)
        
        # Формируем ответ
        time_info = f" в {time_match}" if time_match else ""
        subject_info = f" ({subject})" if subject else ""
        
        response = f"""
✅ *Задача успешно добавлена!*

📝 *Задача:* {task_text}{subject_info}
📅 *Дата:* {task_date}{time_info}
🆔 *ID задачи:* {task['id']}

⏰ *Напоминание:* 
За 1 час до начала я пришлю тебе уведомление! 🔔

💡 *Совет:* Используй технику Помодоро для выполнения задачи!
🎯 *Статистика:* Всего задач: {len(task_manager.tasks.get(str(user_id), []))}
"""
        
        # Очищаем состояние пользователя
        if user_id in user_states:
            del user_states[user_id]
        
        return response
    
    return None

# =================== ПРОСМОТР ЗАДАЧ ===================

@bot.message_handler(func=lambda message: message.text == "📋 Мои задачи")
def show_tasks_menu(message):
    """Меню просмотра задач"""
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton("📅 Сегодня", callback_data="show_today"),
        types.InlineKeyboardButton("📆 Неделя", callback_data="show_week")
    )
    keyboard.add(
        types.InlineKeyboardButton("📋 Все задачи", callback_data="show_all"),
        types.InlineKeyboardButton("✅ Выполненные", callback_data="show_completed")
    )
    keyboard.add(
        types.InlineKeyboardButton("🗑️ Удалить задачу", callback_data="delete_task_start"),
        types.InlineKeyboardButton("🔙 В меню", callback_data="back_to_main")
    )
    
    bot.send_message(message.chat.id,
                     "📋 *Мои задачи*\n\n"
                     "Выбери период для просмотра или действие:",
                     parse_mode='Markdown',
                     reply_markup=keyboard)

def show_tasks(user_id, period="today"):
    """Показать задачи пользователя"""
    if period == "today":
        tasks = task_manager.get_tasks_for_today(user_id)
        period_text = "на сегодня"
    elif period == "week":
        tasks = task_manager.get_tasks_for_week(user_id)
        period_text = "на неделю"
    elif period == "completed":
        all_tasks = task_manager.tasks.get(str(user_id), [])
        tasks = [task for task in all_tasks if task.get("completed", False)]
        period_text = "выполненные"
    else:
        tasks = task_manager.tasks.get(str(user_id), [])
        period_text = "все"
    
    if not tasks:
        return f"🎉 *Задачи {period_text}:*\n\nПока нет задач {period_text}! Можешь добавить новую задачу 😊"
    
    # Сортируем задачи по дате и времени
    def task_sort_key(task):
        date_str = task.get('date', '2000-01-01')
        time_str = task.get('time', '23:59')
        return (date_str, time_str)
    
    tasks.sort(key=task_sort_key)
    
    text = f"📋 *Задачи {period_text}:*\n\n"
    
    for i, task in enumerate(tasks, 1):
        status = "✅" if task.get("completed", False) else "⏳"
        date_info = f" ({task['date']})" if period != "today" else ""
        time_info = f" в {task['time']}" if task.get("time") else ""
        subject_info = f" *[{task.get('subject', '')}]*" if task.get('subject') else ""
        reminder_info = " 🔔" if task.get("time") and not task.get("completed", False) else ""
        
        text += f"{i}. {status} {task['text']}{subject_info}{date_info}{time_info}{reminder_info}\n"
        
        if task.get("completed", False) and task.get("created_at"):
            try:
                created = datetime.strptime(task["created_at"], "%Y-%m-%d %H:%M:%S")
                completed_time = datetime.now()
                duration = completed_time - created
                hours = duration.total_seconds() // 3600
                if hours > 0:
                    text += f"   ⏱️ Выполнено за {int(hours)} часов\n"
            except:
                pass
    
    text += f"\n🎯 *Всего задач: {len(tasks)}*"
    
    return text

# =================== ПОДГОТОВКА К ЕГЭ/ОГЭ ===================

@bot.message_handler(func=lambda message: message.text == "📚 Подготовка к ЕГЭ/ОГЭ")
def show_exam_preparation(message):
    """Меню подготовки к экзаменам"""
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    
    # Первый ряд
    keyboard.add(
        types.InlineKeyboardButton("📘 Математика", callback_data="exam_math"),
        types.InlineKeyboardButton("📗 Русский", callback_data="exam_russian")
    )
    
    # Второй ряд
    keyboard.add(
        types.InlineKeyboardButton("⚛️ Физика", callback_data="exam_physics"),
        types.InlineKeyboardButton("💻 Информатика", callback_data="exam_informatics")
    )
    
    # Третий ряд
    keyboard.add(
        types.InlineKeyboardButton("📓 Английский", callback_data="exam_english"),
        types.InlineKeyboardButton("📙 Обществознание", callback_data="exam_social")
    )
    
    # Четвертый ряд
    keyboard.add(
        types.InlineKeyboardButton("📔 История", callback_data="exam_history"),
        types.InlineKeyboardButton("🔬 Биология", callback_data="exam_biology")
    )
    
    # Пятый ряд
    keyboard.add(
        types.InlineKeyboardButton("⚗️ Химия", callback_data="exam_chemistry"),
        types.InlineKeyboardButton("📖 Литература", callback_data="exam_literature")
    )
    
    # Шестой ряд
    keyboard.add(
        types.InlineKeyboardButton("🌍 География", callback_data="exam_geography"),
        types.InlineKeyboardButton("🎯 Советы по подготовке", callback_data="exam_tips")
    )
    
    text = """
📚 *Подготовка к ЕГЭ/ОГЭ 2026*

Выбери предмет для получения подробной информации:
• 📋 Актуальная структура экзамена 2026
• 📚 Основные темы и изменения
• 🎯 Как готовиться к предмету
• 💡 Ресурсы для подготовки
• 📅 План подготовки
• 🌟 Полезные советы
• 🔔 Изменения 2026 года

👇 *Выбери предмет:*
"""
    
    bot.send_message(message.chat.id, text,
                     parse_mode='Markdown',
                     reply_markup=keyboard)

def show_exam_info(subject_key):
    """Показать информацию по предмету"""
    # Создаем клавиатуру для выбора типа экзамена
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton("📝 ЕГЭ 2026", callback_data=f"ege_{subject_key}"),
        types.InlineKeyboardButton("📋 ОГЭ 2026", callback_data=f"oge_{subject_key}"),
        types.InlineKeyboardButton("🔙 К предметам", callback_data="back_to_subjects")
    )
    
    subject_name = exam_db.subjects.get(subject_key, {}).get("name", "Предмет")
    
    text = f"""
{subject_name}

Выбери тип экзамена для получения актуальной информации на 2026 год:
"""
    
    return text, keyboard

# =================== ЛАЙФХАКИ И СОВЕТЫ ===================

@bot.message_handler(func=lambda message: message.text == "💡 Лайфхаки и советы")
def show_tips_menu(message):
    """Меню лайфхаков и советов"""
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    
    keyboard.add(
        types.InlineKeyboardButton("🍅 Техника Помодоро", callback_data="tip_pomodoro"),
        types.InlineKeyboardButton("📊 Приоритизация", callback_data="tip_prioritization")
    )
    
    keyboard.add(
        types.InlineKeyboardButton("⏰ Тайм-блокинг", callback_data="tip_timeblocking"),
        types.InlineKeyboardButton("🎯 Постановка целей", callback_data="tip_goals")
    )
    
    keyboard.add(
        types.InlineKeyboardButton("📚 Методы обучения", callback_data="tip_study"),
        types.InlineKeyboardButton("😴 Отдых и перерывы", callback_data="tip_rest")
    )
    
    keyboard.add(
        types.InlineKeyboardButton("📈 Мотивация", callback_data="tip_motivation"),
        types.InlineKeyboardButton("📝 Подготовка к экзаменам", callback_data="tip_exam_prep")
    )
    
    keyboard.add(
        types.InlineKeyboardButton("🌟 Все советы", callback_data="tip_all_tips"),
        types.InlineKeyboardButton("🔙 В меню", callback_data="back_to_main")
    )
    
    text = """
💡 *Лайфхаки и советы по тайм-менеджменту и учебе*

Выбери тему, которую хочешь рассмотреть:
• 🍅 Техника Помодоро - управление временем
• 📊 Приоритизация - что делать сначала
• ⏰ Тайм-блокинг - планирование дня
• 🎯 Постановка целей - SMART-метод
• 📚 Методы обучения - эффективное запоминание
• 😴 Отдых и перерывы - как правильно отдыхать
• 📈 Мотивация - как не бросить начатое
• 📝 Подготовка к экзаменам - стратегия успеха
• 🌟 Все советы - полная коллекция рекомендаций
"""
    
    bot.send_message(message.chat.id, text,
                     parse_mode='Markdown',
                     reply_markup=keyboard)

# =================== ИИ ПОМОЩНИК (ПРОДВИНУТАЯ ЛОКАЛЬНАЯ НЕЙРОСЕТЬ) ===================

@bot.message_handler(func=lambda message: message.text == "🤖 ИИ помощник (Тимми)")
def ai_assistant_handler(message):
    """ИИ помощник для учебы с огромной базой знаний"""
    text = """
🤖 *Продвинутый ИИ помощник Тимми*

Привет! Я твой персональный помощник с ОГРОМНОЙ базой знаний по всем предметам! 🎓

📚 *Я знаю ВСЁ о:*
• Математике (алгебра, геометрия, тригонометрия, производные, интегралы)
• Русском языке (орфография, пунктуация, грамматика, паронимы)
• Физике (механика, электричество, термодинамика, оптика, квантовая физика)
• Химии (периодическая таблица, химические связи, реакции, ОВР, органика)
• Английском языке (все времена, условные предложения, модальные глаголы)
• Информатике (Python, алгоритмы, логика, системы счисления, ЕГЭ)
• И других предметах!

💬 *Примеры вопросов:*
• "Объясни теорему Пифагора"
• "Как решать квадратные уравнения через дискриминант?"
• "Расскажи про паронимы в русском языке"
• "Что такое законы Ньютона?"
• "Как работает закон Ома?"
• "Объясни времена в английском"
• "Помоги с задачей по Python"
• "Как подготовиться к ЕГЭ по физике?"

👇 *Просто напиши мне свой учебный вопрос!*

⚡ *Работает полностью локально, без интернета! У меня более 1000 страниц знаний!*

💡 *Задавай любые вопросы по учебе - я отвечу мгновенно!*
"""
    
    bot.send_message(message.chat.id, text, parse_mode='Markdown')
    
    # Регистрируем следующий шаг для получения вопроса
    user_states[message.chat.id] = {'state': 'waiting_ai_question'}
    bot.register_next_step_handler(message, process_ai_question)

def process_ai_question(message):
    """Обработка вопроса для продвинутого ИИ помощника"""
    user_id = message.chat.id
    question = message.text
    
    # Показываем "печатает..."
    bot.send_chat_action(user_id, 'typing')
    time.sleep(0.5)  # Небольшая задержка для эффекта "думает"
    
    # Получаем ответ от продвинутого локального ИИ помощника
    answer = ai_study_assistant.get_answer(question)
    
    if answer:
        # Если ответ слишком длинный, разбиваем на части
        if len(answer) > 4000:
            parts = [answer[i:i+4000] for i in range(0, len(answer), 4000)]
            for part in parts:
                bot.send_message(user_id, part, parse_mode='Markdown')
        else:
            bot.send_message(user_id, answer, parse_mode='Markdown')
    else:
        # Если вопрос не учебный, но может быть связан с тайм-менеджментом
        if any(word in question.lower() for word in ["время", "план", "организовать", "успеть", "расписание"]):
            response = f"""
🤔 *Вопрос по тайм-менеджменту?*

Вот несколько советов:

{ai_study_assistant.study_advice['how_to_study']}

💡 *Задай конкретный вопрос по учебе, и я помогу с теорией!*
"""
            bot.send_message(user_id, response, parse_mode='Markdown')
        else:
            response = """
🤔 *Это не совсем учебный вопрос*

Я специализируюсь на помощи с учебой по школьным предметам. Попробуй спросить что-то по:

📚 *Математика:* уравнения, производные, интегралы, геометрия
📗 *Русский язык:* орфография, пунктуация, паронимы
⚛️ *Физика:* законы Ньютона, электричество, оптика
⚗️ *Химия:* таблица Менделеева, реакции, ОВР
🇬🇧 *Английский:* времена, грамматика
💻 *Информатика:* Python, алгоритмы, ЕГЭ

💡 *Или выбери пункт из меню для другой помощи!*
"""
            bot.send_message(user_id, response, parse_mode='Markdown')
    
    # Предлагаем задать еще вопрос
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("🎓 Задать еще вопрос", callback_data="ai_ask_again"))
    keyboard.add(types.InlineKeyboardButton("🔙 В меню", callback_data="back_to_main"))
    
    bot.send_message(user_id, "Хочешь задать еще вопрос?", reply_markup=keyboard)
    
    # Очищаем состояние
    if user_id in user_states:
        del user_states[user_id]

# =================== СТАТИСТИКА ===================

@bot.message_handler(func=lambda message: message.text == "📊 Статистика и прогресс")
def show_statistics_handler(message):
    """Показать статистику"""
    user_id = message.chat.id
    stats = task_manager.get_statistics(user_id)
    
    # Получаем задачи на сегодня и неделю
    today_tasks = task_manager.get_tasks_for_today(user_id)
    week_tasks = task_manager.get_tasks_for_week(user_id)
    
    # Считаем выполненные задачи сегодня
    completed_today = len([t for t in today_tasks if t.get("completed", False)])
    
    # Считаем задачи с напоминаниями
    tasks_with_reminders = len([t for t in today_tasks if t.get("time") and not t.get("completed", False)])
    
    # Формируем текст статистики
    text = f"""
📊 *Статистика и прогресс*

📈 *Общая статистика:*
• Всего задач: {stats['total_tasks_current']}
• Выполнено задач: {stats['completed_tasks_current']}
• Процент выполнения: {stats['completion_rate']:.1f}%
• Уровень продуктивности: {stats['productivity_level']}

📅 *Активность сегодня:*
• Задач на сегодня: {stats['today_tasks']}
• Выполнено сегодня: {completed_today}
• Осталось выполнить: {stats['today_tasks'] - completed_today}
• Задач с напоминаниями: {tasks_with_reminders}

📆 *На неделю:*
• Задач на неделю: {stats['week_tasks']}
• Последняя активность: {stats['last_active']}

🎯 *Рекомендации:*
"""
    
    if stats['completion_rate'] < 50:
        text += "• Старайся выполнять больше задач\n• Разбивай большие задачи на маленькие\n• Используй технику Помодоро\n"
    elif stats['completion_rate'] < 80:
        text += "• Хороший прогресс! Продолжай в том же духе\n• Попробуй планировать задачи на неделю вперед\n"
    else:
        text += "• Отличная продуктивность! Ты молодец!\n• Помоги друзьям с планированием\n"
    
    if stats['today_tasks'] == 0:
        text += "\n💡 *Совет:* Добавь задачи на сегодня для лучшего планирования!"
    
    if tasks_with_reminders > 0:
        text += f"\n🔔 *Напоминания:* У тебя {tasks_with_reminders} задач с уведомлениями сегодня!"
    
    # Кнопки для управления задачами
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton("✅ Отметить задачу выполненной", callback_data="complete_task_menu"),
        types.InlineKeyboardButton("🗑️ Удалить задачу", callback_data="delete_task_start")
    )
    keyboard.add(
        types.InlineKeyboardButton("📅 Задачи на сегодня", callback_data="show_today"),
        types.InlineKeyboardButton("🔙 В меню", callback_data="back_to_main")
    )
    
    bot.send_message(user_id, text, parse_mode='Markdown', reply_markup=keyboard)

# =================== CALLBACK ОБРАБОТЧИК ===================

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    """Обработчик всех callback-запросов"""
    user_id = call.from_user.id
    message_id = call.message.message_id
    
    try:
        # Добавление задачи - выбор даты
        if call.data.startswith("date_"):
            date_type = call.data.replace("date_", "")
            response = process_task_date(user_id, date_type)
            
            if response:
                bot.edit_message_text(response, user_id, message_id, parse_mode='Markdown')
            elif date_type == "custom":
                # Запрос на ввод даты
                msg = bot.send_message(user_id, 
                                      "📅 *Введи дату в формате ДД.ММ.ГГГГ*\n"
                                      "Например: 15.05.2026\n\n"
                                      "Или выбери из предложенных дат:",
                                      parse_mode='Markdown')
                user_states[user_id]['state'] = 'waiting_custom_date'
                bot.register_next_step_handler(msg, process_custom_date)
            else:
                bot.answer_callback_query(call.id, "Продолжаем настройку задачи...")
        
        # Добавление задачи - выбор времени
        elif call.data.startswith("time_"):
            time_val = call.data.replace("time_", "")
            
            if user_id in user_states and 'task_date' in user_states[user_id]:
                task_date = user_states[user_id]['task_date']
                task_text = user_states[user_id]['task_text']
                
                if time_val == "none":
                    time_match = None
                else:
                    time_match = time_val
                
                # Определяем предмет
                subject = None
                subject_keywords = {
                    "математик": "Математика",
                    "алгебр": "Математика",
                    "геометр": "Математика",
                    "русск": "Русский язык",
                    "физик": "Физика",
                    "информатик": "Информатика",
                    "английск": "Английский язык"
                }
                
                for keyword, subj in subject_keywords.items():
                    if keyword in task_text.lower():
                        subject = subj
                        break
                
                # Добавляем задачу
                task = task_manager.add_task(user_id, task_text, task_date, time_match, subject)
                
                # Формируем ответ
                time_info = f" в {time_match}" if time_match else ""
                subject_info = f" ({subject})" if subject else ""
                
                response = f"""
✅ *Задача успешно добавлена!*

📝 *Задача:* {task_text}{subject_info}
📅 *Дата:* {task_date}{time_info}
🆔 *ID задачи:* {task['id']}

⏰ *Напоминание:* 
За 1 час до начала я пришлю тебе уведомление! 🔔

💡 *Совет:* Используй технику Помодоро для выполнения задачи!
🎯 *Статистика:* Всего задач: {len(task_manager.tasks.get(str(user_id), []))}
"""
                
                bot.edit_message_text(response, user_id, message_id, parse_mode='Markdown')
                
                # Очищаем состояние пользователя
                if user_id in user_states:
                    del user_states[user_id]
            else:
                bot.answer_callback_query(call.id, "Ошибка: данные задачи не найдены")
        
        # Показать задачи
        elif call.data.startswith("show_"):
            period = call.data.replace("show_", "")
            tasks_text = show_tasks(user_id, period)
            
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton("🔙 Назад к задачам", callback_data="back_to_tasks"))
            
            bot.edit_message_text(tasks_text, user_id, message_id, 
                                 parse_mode='Markdown', reply_markup=keyboard)
        
        # Удаление задач - начало
        elif call.data == "delete_task_start":
            tasks = task_manager.get_tasks_for_today(user_id)
            if not tasks:
                bot.answer_callback_query(call.id, "Нет задач для удаления")
                return
            
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            for task in tasks[:10]:  # Показываем первые 10 задач
                btn_text = f"🗑️ {task['text'][:20]}..." if len(task['text']) > 20 else f"🗑️ {task['text']}"
                keyboard.add(types.InlineKeyboardButton(btn_text, callback_data=f"delete_{task['id']}"))
            
            keyboard.add(types.InlineKeyboardButton("🔙 Назад", callback_data="back_to_stats"))
            
            bot.edit_message_text("🗑️ *Выбери задачу для удаления:*", 
                                 user_id, message_id, parse_mode='Markdown', reply_markup=keyboard)
        
        # Удаление задачи
        elif call.data.startswith("delete_"):
            task_id = int(call.data.replace("delete_", ""))
            success = task_manager.delete_task(user_id, task_id)
            
            if success:
                bot.answer_callback_query(call.id, "✅ Задача успешно удалена!")
                # Показываем обновленный список задач
                show_tasks_menu(call.message)
                bot.delete_message(user_id, message_id)
            else:
                bot.answer_callback_query(call.id, "❌ Ошибка при удалении задачи")
        
        # Подготовка к экзаменам - выбор предмета
        elif call.data.startswith("exam_"):
            if call.data == "exam_tips":
                # Показать общие советы по подготовке
                tips = exam_db.get_tips("exam_preparation")
                keyboard = types.InlineKeyboardMarkup()
                keyboard.add(types.InlineKeyboardButton("🔙 К предметам", callback_data="back_to_subjects"))
                bot.edit_message_text(tips, user_id, message_id, parse_mode='Markdown', reply_markup=keyboard)
            else:
                subject_key = call.data.replace("exam_", "")
                text, keyboard = show_exam_info(subject_key)
                bot.edit_message_text(text, user_id, message_id, parse_mode='Markdown', reply_markup=keyboard)
        
        # Тип экзамена (ЕГЭ/ОГЭ)
        elif call.data.startswith("ege_") or call.data.startswith("oge_"):
            exam_type = "ege" if call.data.startswith("ege_") else "oge"
            subject_key = call.data.replace("ege_", "").replace("oge_", "")
            
            info = exam_db.get_subject_info(subject_key, exam_type)
            
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton("🔙 К предметам", callback_data="back_to_subjects"))
            keyboard.add(types.InlineKeyboardButton("🔙 В меню", callback_data="back_to_main"))
            
            bot.edit_message_text(info, user_id, message_id, parse_mode='Markdown', reply_markup=keyboard)
        
        # Лайфхаки и советы
        elif call.data.startswith("tip_"):
            tip_type = call.data.replace("tip_", "")
            
            if tip_type == "exam_prep":
                text = exam_db.get_tips("exam_preparation")
            elif tip_type == "motivation":
                text = exam_db.get_tips("motivation")
            elif tip_type == "goals":
                text = exam_db.get_tips("goal_setting")
            elif tip_type == "rest":
                text = exam_db.get_tips("rest_breaks")
            elif tip_type == "timeblocking":
                text = exam_db.get_tips("time_management")
            elif tip_type == "study":
                text = exam_db.get_tips("study_techniques")
            elif tip_type == "all_tips":
                text = exam_db.get_all_tips()
            else:
                # Для других типов используем стандартные ответы
                if tip_type == "pomodoro":
                    text = """
🍅 *Техника Помодоро*

*Что это?*
Метод управления временем, разработанный Франческо Чирилло в конце 1980-х годов.

*Как работает?*
1. Выбери задачу для выполнения
2. Установи таймер на 25 минут
3. Работай над задачей, пока таймер не прозвонит
4. Сделай короткий перерыв (5 минут)
5. После 4 помодоро сделай длинный перерыв (15-30 минут)

*Преимущества:*
• Повышает концентрацию
• Помогает бороться с прокрастинацией
• Улучшает оценку времени
• Снижает умственную усталость

*Совет:* Используй приложения типа Focus Keeper или Tomato Timer!
"""
                elif tip_type == "prioritization":
                    text = """
📊 *Матрица Эйзенхауэра*

*Что это?*
Метод приоритизации задач, разработанный Дуайтом Эйзенхауэром.

*4 квадранта:*
1. *Важно и срочно* – делай сразу
   (кризисы, дедлайны, проблемы)
   
2. *Важно, но не срочно* – запланируй
   (обучение, планирование, развитие)
   
3. *Срочно, но не важно* – делегируй
   (некоторые звонки, встречи, дела)
   
4. *Не срочно и не важно* – удали
   (соцсети, пустая трата времени)

*Совет:* Проводи сортировку задач каждое утро!
"""
                else:
                    text = "Совет по этой теме скоро будет добавлен!"
            
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton("🔙 К советам", callback_data="back_to_tips"))
            keyboard.add(types.InlineKeyboardButton("🔙 В меню", callback_data="back_to_main"))
            
            bot.edit_message_text(text, user_id, message_id, parse_mode='Markdown', reply_markup=keyboard)
        
        # Навигация назад
        elif call.data == "back_to_main":
            start(call.message)
            bot.delete_message(user_id, message_id)
        
        elif call.data == "back_to_subjects":
            show_exam_preparation(call.message)
            bot.delete_message(user_id, message_id)
        
        elif call.data == "back_to_tasks":
            show_tasks_menu(call.message)
            bot.delete_message(user_id, message_id)
        
        elif call.data == "back_to_tips":
            show_tips_menu(call.message)
            bot.delete_message(user_id, message_id)
        
        elif call.data == "back_to_stats":
            show_statistics_handler(call.message)
            bot.delete_message(user_id, message_id)
        
        elif call.data == "ai_ask_again":
            ai_assistant_handler(call.message)
            bot.delete_message(user_id, message_id)
        
        # Управление задачами - завершение
        elif call.data == "complete_task_menu":
            tasks = task_manager.get_tasks_for_today(user_id)
            if not tasks:
                bot.answer_callback_query(call.id, "Нет задач для отметки")
                return
            
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            for task in tasks[:10]:  # Показываем первые 10 задач
                if not task.get("completed", False):
                    btn_text = f"✅ {task['text'][:20]}..." if len(task['text']) > 20 else f"✅ {task['text']}"
                    keyboard.add(types.InlineKeyboardButton(btn_text, callback_data=f"complete_{task['id']}"))
            
            keyboard.add(types.InlineKeyboardButton("🔙 Назад", callback_data="back_to_stats"))
            
            bot.edit_message_text("✅ *Выбери задачу для отметки выполнения:*", 
                                 user_id, message_id, parse_mode='Markdown', reply_markup=keyboard)
        
        elif call.data.startswith("complete_"):
            task_id = int(call.data.replace("complete_", ""))
            success = task_manager.complete_task(user_id, task_id)
            
            if success:
                bot.answer_callback_query(call.id, "✅ Задача отмечена как выполненная!")
                # Обновляем статистику
                show_statistics_handler(call.message)
                bot.delete_message(user_id, message_id)
            else:
                bot.answer_callback_query(call.id, "❌ Ошибка при отметке задачи")
        
        else:
            bot.answer_callback_query(call.id, "Функция в разработке")
    
    except Exception as e:
        print(f"Ошибка в callback обработчике: {e}")
        bot.answer_callback_query(call.id, "Произошла ошибка")

def process_custom_date(message):
    """Обработка ввода пользовательской даты"""
    user_id = message.chat.id
    
    try:
        # Пытаемся распарсить дату
        date_str = message.text.strip()
        
        # Пробуем разные форматы
        formats = ["%d.%m.%Y", "%d.%m.%y", "%d/%m/%Y", "%d/%m/%y", "%Y-%m-%d"]
        
        parsed_date = None
        for fmt in formats:
            try:
                parsed_date = datetime.strptime(date_str, fmt)
                break
            except:
                continue
        
        if parsed_date is None:
            bot.send_message(user_id, "❌ *Неверный формат даты!*\n\n"
                           "Пожалуйста, введи дату в формате ДД.ММ.ГГГГ\n"
                           "Например: 15.05.2026", parse_mode='Markdown')
            return
        
        # Сохраняем дату и переходим к выбору времени
        if user_id in user_states and 'task_text' in user_states[user_id]:
            user_states[user_id]['task_date'] = parsed_date.strftime("%Y-%m-%d")
            user_states[user_id]['state'] = 'waiting_task_time'
            
            keyboard = types.InlineKeyboardMarkup(row_width=3)
            # Добавляем кнопки с популярным временем
            times = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", 
                    "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"]
            buttons = [types.InlineKeyboardButton(time, callback_data=f"time_{time}") for time in times]
            
            # Добавляем кнопки построчно
            for i in range(0, len(buttons), 3):
                keyboard.add(*buttons[i:i+3])
            
            keyboard.add(types.InlineKeyboardButton("🕐 Без времени", callback_data="time_none"))
            
            bot.send_message(user_id,
                            f"📅 *Дата установлена:* {parsed_date.strftime('%d.%m.%Y')}\n\n"
                            "🕐 *Теперь укажи время выполнения задачи:*\n\n"
                            "Выбери из предложенных или напиши время в формате ЧЧ:ММ\n"
                            "Например: 14:30",
                            parse_mode='Markdown',
                            reply_markup=keyboard)
    except Exception as e:
        bot.send_message(user_id, f"❌ Ошибка при обработке даты: {str(e)}")

# =================== ОБРАБОТЧИК ВСЕХ СООБЩЕНИЙ ===================

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    """Обработчик всех остальных сообщений"""
    user_id = message.chat.id
    
    # Проверяем состояние пользователя
    if user_id in user_states:
        state = user_states[user_id].get('state')
        
        if state == 'waiting_task_text':
            process_task_text(message)
        elif state == 'waiting_ai_question':
            process_ai_question(message)
        elif state == 'waiting_custom_date':
            process_custom_date(message)
        else:
            bot.send_message(user_id, "Используй кнопки меню или напиши /start 🤖")
    
    else:
        # Проверяем, не является ли это вопросом для ИИ помощника
        answer = ai_study_assistant.get_answer(message.text)
        if answer:
            # Если ответ слишком длинный, разбиваем на части
            if len(answer) > 4000:
                parts = [answer[i:i+4000] for i in range(0, len(answer), 4000)]
                for part in parts:
                    bot.send_message(user_id, part, parse_mode='Markdown')
            else:
                bot.send_message(user_id, answer, parse_mode='Markdown')
        else:
            bot.send_message(user_id, 
                           "Используй кнопки меню или напиши /start для навигации 🤖\n\n"
                           "Или задай вопрос об учебе - я отвечу! У меня более 1000 страниц знаний по всем предметам! 📚")

# =================== ЗАПУСК БОТА ===================

if __name__ == '__main__':
    print("=" * 70)
    print("🤖 Бот Тимми запускается...")
    print(f"⏰ Время запуска: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🔔 Система напоминаний: ЗА 1 ЧАС ДО СОБЫТИЯ")
    print("📚 Подготовка к ЕГЭ/ОГЭ: АКТУАЛЬНО НА 2026 ГОД")
    print("⚛️ Добавлена физика и информатика!")
    print("🧠 Продвинутый локальный ИИ помощник: ✅ АКТИВЕН")
    print("📚 Объем базы знаний: БОЛЕЕ 1000 СТРАНИЦ учебного материала!")
    print("📘 Математика: алгебра, геометрия, тригонометрия, производные, интегралы")
    print("📗 Русский язык: орфография, пунктуация, грамматика, паронимы")
    print("⚛️ Физика: механика, электричество, термодинамика, оптика, квантовая физика")
    print("⚗️ Химия: периодическая таблица, связи, реакции, ОВР, органика")
    print("🇬🇧 Английский: все времена, условные предложения, модальные глаголы")
    print("💻 Информатика: Python, алгоритмы, логика, системы счисления")
    print("=" * 70)
    
    # Запускаем систему напоминаний
    reminder_system.start()
    
    try:
        # Запускаем бота с обработкой ошибок
        print("🚀 Запускаю бота...")
        bot.polling(
            none_stop=True,
            interval=1,
            timeout=30,
            skip_pending=True
        )
        
    except Exception as e:
        print(f"❌ Критическая ошибка: {e}")
        print("🔄 Перезапускаю через 10 секунд...")
        time.sleep(10)
        
        # Пытаемся перезапустить
        try:
            bot.polling(none_stop=True, interval=1, timeout=30)
        except:
            print("💥 Бот завершил работу")
    
    finally:
        # Останавливаем систему напоминаний
        reminder_system.stop()
        print("👋 Бот завершил работу")
