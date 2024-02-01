from math import ceil
import gspread

spreadsheet = gspread.service_account(filename="credentials.json")
working_sheet = spreadsheet.open('Engenharia de Software - Desafio Lenon Fernandes Philippi')
print(working_sheet.get_worksheet_by_id(0))

# Load the workbook
# workbook = openpyxl.load_workbook("Engenharia de Software - Desafio Lenon Fernandes Philippi.xlsx")

# Select the "engenharia_de_software" sheet
sheet = working_sheet.get_worksheet_by_id(0)

# Select the values
values = sheet.get_all_values()

# Iterate values, starting in 3rd row
for row in range(3, len(values)):

    # Get value from "Faltas" column
    absences = int(values[row][2])

    # Get values from "P1", "P2", "P3" columns
    p1, p2, p3 = map(int, values[row][3:6])

    # Checks for "Reprovado por Falta" situation
    if absences > 0.25 * 60:

        """
        Stores "Situação" value for actual row if it 
        checks ok for "Reprovado por Falta"
        """
        situation = "Reprovado por Falta"

        """
        Stores "Nota para Aprovação Final" value for actual
        row if it checks ok for "Reprovado por Falta"
        """
        final_grade = 0

    # If there's no excessive absences, then average is analyzed
    else:
        # Average calculation
        average = ceil(((p1 + p2 + p3) / 3) / 10)

        # Checks for "Reprovado por Nota" situation
        if average < 5:
            """
            Stores "Situação" value for actual row if it
            checks ok for "Reprovado por Nota"
            """
            situation = "Reprovado por Nota"
        
            """
            Stores "Nota para Aprovação Final" value
            for actual row if it checks ok for
            "Reprovado por Nota"
            """
            final_grade = 0

        # Checks for "Exame Final" situation
        elif 5 <= average < 7:
            """
            Stores "Situação" value for actual row
            if it checks of for "Exame Final"
            """
            situation = "Exame Final"

            # "Nota para Aprovação Final" value calculation
            naf = 10 - average

            """
            Stores "Nota para Aprovação Final" value for
            actual row if it checks ok for "Exame Final"
            """
            final_grade = naf

        # Checks for "Aprovado"
        else:
            """
            Stores "Situação" value for actual row
            if it checks of for "Aprovado"
            """
            situation = "Aprovado"

            """
            Stores "Nota para Aprovação Final" value for
            actual row if it checks ok for "Aprovado"
            """
            final_grade = 0

    """
    Updates sheet with situation ("Situação")
    and final grade ("Nota para Aprovação Final") values
    """
    sheet.update_cell(row + 1, 7, situation)
    sheet.update_cell(row + 1, 8, final_grade)
