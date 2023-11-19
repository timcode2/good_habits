from datetime import timedelta

from rest_framework.exceptions import ValidationError

from spa.tasks import check_habits


class ExecutionTimeValidator:
    """Проверка длительности поля execution_time"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        models_dict = dict(value)  # словарь из полей модели
        check_habits()
        execution_time = models_dict.get(self.field)  # значение времени выполнения
        if execution_time > timedelta(seconds=120):
            raise ValidationError('Время выполнения привычки не должно превышать 120 секунд')


class RelatedHabitValidation:
    """Проверка наличия у связанной привычки признака is_pleasant"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        award = dict(value).get('award')  # Наличие вознаграждения у привычки
        related_habit = dict(value).get('related_habit')  # Наличие связанной привычки

        # Если указано и вознаграждение и связанная привычка
        if award and related_habit:
            raise ValidationError('Невозможно одновременно указать связанную привычку и вознаграждение')

        # Если указана связанная привычка проверяем ее на наличие признака is_pleasant=True
        if related_habit:
            if not related_habit.is_pleasant:

                raise ValidationError(
                    'В связанные привычки может попасть привычка с признаком приятной (is_pleasant=True)')


class IsPleasantValidator:
    """У приятной привычки не может быть вознаграждения или связанной привычки"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        is_pleasant = dict(value).get(self.field)  # проверяем значение is_pleasant
        # если привычка приятная (is_pleasant=True)
        if is_pleasant:
            award = dict(value).get('award')  # наличие вознаграждения
            related_habit = dict(value).get('related_habit')  # наличие связанной привычки
            if award or related_habit:
                raise ValidationError(
                    'У приятной привычки (is_pleasant=True) не может быть вознаграждения или связанной привычки')


class PeriodicityValidator:
    """Нельзя выполнять привычку реже, чем 1 раз в 7 дней"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        periodicity = dict(value).get('periodicity')

        if periodicity > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')