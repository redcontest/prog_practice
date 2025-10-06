from string import digits


def main():
    scores = input("Введите все баллы, выставленные за олимпиаду: ")

    while not (all(c in digits + ' ' for c in scores)
               and scores != ''
               and any(c in digits for c in scores)):
        scores = input("Введите ЦЕЛОЧИСЛЕННЫЕ значения БЕЗ"
                       "запятых и прочих знаков: ")
    scores = list(int(i) for i in scores.split())

    student_score = input("Введите ваш результат по олимпиаде: ")
    while not (all(c in digits for c in student_score)
               and student_score != ''):
        student_score = input("Введите ЦЕЛОЧИСЛЕННОЕ значение БЕЗ"
                              "запятых и прочих знаков: ")
    student_score = int(student_score)

    scores.append(student_score)
    check_winners(scores, student_score)


def check_winners(scores: list, student_score: int):
    """
    Определяет, находится ли результат участника олимпиады в тройке наибольших.
    Если находится, функция сообщает, что участник попал в тройку победителей.
    В противном случае сообщает, что участник не попал в тройку победителей.
    При этом логика функции основана на том, что если двое участников олимпиады
    набирают одинаковое количество баллов, то они стоят на одном и том же
    призовом месте.

    Args:
    scores (list): список всех выставленных баллов участникам олимпиады
    student_score (int): балл, который необходимо проверить на наличие в тройке
                         наибольших.
    """
    sorted_score = sorted(set(scores), reverse=True)[:3]

    if student_score in sorted_score:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")


if __name__ == '__main__':
    main()
