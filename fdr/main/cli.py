from get_path_from_user import get_path_from_user


def main():
    print('This is where I will ask you for an FDR Excel file and run a validation report on it.')
    fdr_excel_path = get_path_from_user()
    print(fdr_excel_path)


if __name__ == '__main__':
    main()
