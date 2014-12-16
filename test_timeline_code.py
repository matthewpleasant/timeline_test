import csv #imports the csv file

file = open('GUNS 2012 - Timeline1.csv') #change name of exported file each time, if needed
csv_file = csv.reader(file) #creates CSV object that's parsed

time_line = open(r'timeline_test_.txt', 'a') #opens a file and appends information inside

number = 68

for row in csv_file:
    panel1 = """
    <!-- panel -->
    <div class="panel">
    <div class="panel_content">
        <h2><p>%s</p></h2>        
            <a href="#answer%s" onclick="return showAnswer('answer%s');"><img class="thumb" src="images/%s" alt="%s (victim)"></a>
            """ % (row[0], str(number), str(number), row[1], row[0])
    time_line.write(panel1)
    if row[2] != "None":
         panel2 = """<a href="#answer%s" onclick="return showAnswer('answer%s');"><img class="thumb" src="images/%s" alt="%s (victim)"></a>
         """ % (str(number), str(number), row[2], row[0])
         time_line.write(panel2)
    panel3 = """<h2><p>%s</p></h2>
            <div class="label">%s</div>
            <div class="clear_both"></div>
        </div>
    </div>
    <!--panel-->\n
    """ % (row[3], row[4])
    time_line.write(panel3)
    number += 1
    
file.close()

time_line.close()