from csv import writer
from csv import reader
 
# Open the input_file in read mode and output_file in write mode
sumMin = 0
sumMax = 0 
firstMin = 0
firstMax = 0
index = 0
with open('final-data.csv', 'r') as read_obj, \
        open('month-values.csv', 'w', newline='') as write_obj:
    # Create a csv.reader object from the input file object
    csv_reader = reader(read_obj)
    # Create a csv.writer object from the output file object
    csv_writer = writer(write_obj)
    # Read each row of the input csv file as list
    for row in csv_reader:
        # Append the default text in the row / list
        if (index == 0):
            new_row = row

        else:
            sumMin += int(row[2]) - firstMax
            sumMax += int(row[1]) - firstMin
            new_row = (row[0], sumMax, sumMin)
            # print(row[1])

        index += 1
        # Add the updated row / list to the output file
        csv_writer.writerow(new_row)