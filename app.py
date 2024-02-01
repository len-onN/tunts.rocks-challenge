import openpyxl
from math import ceil
import gspread

spreadsheet = gspread.service_account(filename="credentials.json")
working_sheet = spreadsheet.open('Engenharia de Software - Desafio Lenon Fernandes Philippi')
print(working_sheet.get_worksheet_by_id(0))

# Load the workbook
# workbook = openpyxl.load_workbook("Engenharia de Software - Desafio Lenon Fernandes Philippi.xlsx")

# Select the "engenharia_de_software" sheet
sheet = working_sheet.get_worksheet_by_id(0)

values = sheet.get_all_values()

for row in range(3, len(values)):
    enrollment = int(values[row][0])
    absences = int(values[row][2])
    p1, p2, p3 = map(int, values[row][3:6])

    if absences > 0.25 * 60:
        situation = "Reprovado por Falta"
        final_grade = 0
    else:
        average = ceil(((p1 + p2 + p3) / 3) / 10)

        if average < 5:
            situation = "Reprovado por Nota"
            final_grade = 0
        elif 5 <= average < 7:
            situation = "Exame Final"
            naf = 10 - average
            final_grade = naf
        else:
            situation = "Aprovado"
            final_grade = 0
    sheet.update_cell(row + 1, 7, situation)
    sheet.update_cell(row + 1, 8, final_grade)
