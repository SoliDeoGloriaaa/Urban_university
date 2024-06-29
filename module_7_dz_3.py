# Использование %:
team1_num = 5
team2_num = 6
print('Количество участников первой команды: %s!' %(team1_num))
print('Итого сегодня в командах участников: %s и %s!' %(team1_num, team2_num))


# Использование .format()
print('Команда Волшебники данных решала задач: {score_2}!'.format(score_2=42))
print('Волшебники данных решили задачи за {team1_time} c!'.format(team1_time=18015.2))


# Использование f-строк
score_1, score_2 = 40, 42
print(f'Команды решили {score_1} и {score_2} задач')

challenge_result = 'победа команды Мастера кода!'
print(f'Результат битвы: {challenge_result}')

task_total, time_avg = 82, 350.4
print(f'Сегодня было решено {task_total} задач, в среднем по {time_avg} секунды на задачу!')