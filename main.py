import tabula

df = tabula.read_pdf("Calendar.pdf", stream=True)
tabula.convert_into("Calendar.pdf", "Calendar.csv", output_format="csv", pages="all")

"""
TODO Parse the csv file to extract
Event ::= StartDate - EndDate
      |   Date
"""
def get_events(event_file):
    with open(event_file, "r") as f:
        for line in f:
            pass



"""TODO Generate a Calendar file with the event and dates"""
