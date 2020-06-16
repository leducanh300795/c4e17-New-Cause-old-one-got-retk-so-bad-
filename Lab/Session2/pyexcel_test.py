import pyexcel

data = [
    {
        "Name": "Huyen",
        "Age": 23
    },
    {
        "Name": "Don",
        "Age": 25
    },
    {
        "Name": "Quang",
        "Age": 22
    },
]

pyexcel.save_as(records=data, dest_file_name="test.xlsx")
