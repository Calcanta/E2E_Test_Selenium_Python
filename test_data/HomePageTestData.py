import openpyxl


class HomePageTestData:
    home_page_test_data = [
        {"first_name": "Cinthia", "email": "calcanta@hotmail.com", "gender": "Female"},
        {"first_name": "Carlos", "email": "carlos@hotmail.com", "gender": "Male"},
        {"first_name": "Angel", "email": "angel@hotmail.com", "gender": "Male"},
    ]

    @staticmethod
    def get_test_data(test_case_name,
                      workbook_path='C:/Users/HP/Documents/PyProjects/E2E_example/test_data/test_cases_data.xlsx',
                      sheet_name='HomePageTestsData'):
        data_book = openpyxl.load_workbook(workbook_path)
        data_sheet = data_book[sheet_name]
        test_case_data = []
        test_data_names = [cell.value for cell in data_sheet[1]]
        test_data_names = test_data_names[1:]
        for row in data_sheet.iter_rows(min_row=2, values_only=True):
            if row[0] == test_case_name:
                test_case_data = [*row]
                test_case_data = test_case_data[1:]
                break
        if test_case_data == [] or test_data_names == []:
            test_data_dict = {"first_name": "Cinthia", "email": "calcanta@hotmail.com", "gender": "Female"}
        else:
            test_data_dict = dict(zip(test_data_names, test_case_data))
        return [test_data_dict]
