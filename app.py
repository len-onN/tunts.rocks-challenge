from math import ceil
import gspread


def get_average(p1, p2, p3):
    return ceil(((p1 + p2 + p3) / 3) / 10)


def calculate_final_grade(average):
    if average < 5:
        return 0
    elif 5 <= average < 7:
        return 10 - average
    else:
        return 0


def determine_situation(absences, average):
    if absences > 0.25 * 60:
        return "Reprovado por Falta", 0
    elif average < 5:
        return "Reprovado por Nota", 0
    elif 5 <= average < 7:
        return "Exame Final", calculate_final_grade(average)
    else:
        return "Aprovado", 0


def main():
    spreadsheet = gspread.service_account(filename="credentials.json")
    working_sheet = spreadsheet.open('Engenharia de Software - Desafio Lenon Fernandes Philippi')
    sheet = working_sheet.get_worksheet_by_id(0)

    values = sheet.get_all_values()

    for row in range(3, len(values)):
        absences = int(values[row][2])
        p1, p2, p3 = map(int, values[row][3:6])

        average = get_average(p1, p2, p3)

        situation, final_grade = determine_situation(absences, average)

        sheet.update_cell(row + 1, 7, situation)
        sheet.update_cell(row + 1, 8, final_grade)


if __name__ == "__main__":
    main()
