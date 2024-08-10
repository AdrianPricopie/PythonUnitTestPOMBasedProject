class DataTest:
    correct_email = 'Test123z@yahoo.com'
    short_pass = 'Testc'
    wrong_pass = 'Testcdsad2@'
    correct_pass = 'Test123'
    wrong_format_email = 'Test123zyahoo.com'
    wrong_email = 'Grigore@yahoo.com'
    items_pressent_in_login_dashboard = ['Cumparaturile mele', 'Vanzarile mele', 'Garantiile mele', 'Asigurarile mele',
                                         'Retur',
                                         'Setari cont', 'Logout']

    product_name = 'iPhone 13'
    short_product_name = 'ipho'
    inexisting_product = 'fdsafdasfd'
    expected_result_message_for_inexisting_prod = 'Rezultate pentru fdsafdasfd 0 produse'
    expected_result_message_for_numeric_input = 'Rezultate pentru 123456 0 produse'
    interval_cautare = (200, 3320)
    auto_suggest_keyword = 'iphone'
    special_product_name = "lap@top"
    expected_result_search = ['MacBook', 'Laptop']
    numeric_product_name = "123456"

    ### NEW

    ValidColor = 'Albastru'
    ExpectedResultColor = 'Blue'
