import openpyxl
from math import ceil

# Load the workbook
workbook = openpyxl.load_workbook("Engenharia de Software - Desafio Lenon Fernandes Philippi.xlsx")

# Select the "engenharia_de_software" sheet
sheet = workbook["engenharia_de_software"]

# Iterate through each row starting from the 4th row
for row in range(4, sheet.max_row + 1):
    # Step 1: Check for "Reprovado por Falta"
    faltas = sheet.cell(row=row, column=3).value
    if faltas > ceil(0.25 * 60):  # 25% of 60 classes
        sheet.cell(row=row, column=7, value="Reprovado por Falta")  # Situação
        sheet.cell(row=row, column=8, value=0)  # Nota para Aprovação Final
    else:
        # Step 2: Calculate the average of P1, P2, and P3
        p1 = sheet.cell(row=row, column=4).value  # P1
        p2 = sheet.cell(row=row, column=5).value  # P2
        p3 = sheet.cell(row=row, column=6).value  # P3
        media = ceil(((p1 + p2 + p3) / 3) / 10)

        # Check for "Reprovado por Nota"
        if media < 5:
            sheet.cell(row=row, column=7, value="Reprovado por Nota")  # Set the "Situação" column
            sheet.cell(row=row, column=8, value=0)  # Nota para Aprovação Final
        elif 5 <= media < 7:
            # Check for "Exame Final"
            sheet.cell(row=row, column=7, value="Exame Final")  # Set the "Situação" column
            sheet.cell(row=row, column=8, value=(10 - media))  # Set the Nota para Aprovação Final column
        else:
            # Aprovado
            sheet.cell(row=row, column=7, value="Aprovado")  # Set the "Situação" column
            sheet.cell(row=row, column=8, value=0)  # Set the Nota para Aprovação Final column

# Save the changes
workbook.save("Engenharia de Software - Desafio Lenon Fernandes Philippi.xlsx")
