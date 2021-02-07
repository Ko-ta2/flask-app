import datetime

def context_processor():
    def get_menus():
        return [
            ("index.graph", "グラフ"),
            ("index.form", "フォーム"),
            ("index.collection", "コレクション")
        ]

    def get_current_year():
        return datetime.datetime.now().year

    def get_table_header():
        return ["headcell1","headcell2","headcell3","headcell4","headcell5"]

    def get_table_data():
        return [{
            "headcell1": "bodycell1",
            "headcell2": "bodycell2",
            "headcell3": "bodycell3",
            "headcell4": "bodycell4",
            "headcell5": "bodycell5"
        }]

    context_processor = {
        "get_menus": get_menus,
        "get_current_year": get_current_year,
        "get_table_header": get_table_header,
        "get_table_data": get_table_data
    }

    return context_processor
