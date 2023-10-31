#generation of excel
import xlsxwriter as xs
import datetime

def generate_output_excel(raw_output):

    today_date = datetime.date.today()
    workbook = xs.Workbook(f"Excel_{today_date}.xlsx")
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0

    for year, seasons in raw_output.items():
        for season, courses in seasons.items():
            worksheet.write(row, col, f"{year} {season}")
            worksheet.write_column(row + 1, col, courses)
            col += 1
        row = 0
    workbook.close()
