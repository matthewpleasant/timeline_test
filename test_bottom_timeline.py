import csv #imports the csv file

file = open('GUNS 2012 - Timeline2.csv') #change name of exported file each time, if needed
csv_file = csv.reader(file) #creates CSV object that's parsed

time_line = open(r'timeline_test_.txt', 'a') #opens a file and appends information inside

def panel_three():
    number = 67 #or is it 68?
    for row in csv_file:
        panel0 = """
        <div id="answer%s" class="show">
            <div class="image">
            <span class="dropt">
            <img src="images/%s" alt="%s (victim)">
            <span style="width:500px;">%s (victim)</span>
            </span>
            """ % (str(number), row[1], row[0], row[0])
        time_line.write(panel0)
        if row[2] != 'None':
            panel1 = """
            <span class="dropt">
            <img src="images/%s" alt="%s (victim)">
            <span style="width:500px;">%s (victim)</span>
            </span>""" % (row[3], row[2], row[2])
            time_line.write(panel1)
        if row[4] != 'None':
            panel2 = """
            <span class="dropt">
            <img src="images/%s" alt="%s (suspect)">
            <span style="width:500px;">%s (suspect)</span>
            </span>""" % (row[5], row[4], row[4])
            time_line.write(panel2)
        if row[6] != 'None':
            panel3 = """
            <span class="dropt">
            <img src="images/%s" alt="%s (suspect)">
            <span style="width:500px;">%s (suspect)</span>
            </span>""" % (row[7], row[6], row[6])
            time_line.write(panel3)
        if row[9] != 'None':
            panel5 = """
            <span class="dropt">
            <img src="images/%s" alt="gun recovered">
            <span style="width:500px;">gun recovered</span>
            </span>""" % (row[9])
            time_line.write(panel5)
        if row[8] != 'None':
            panel6 = """
            <span class="dropt">
            <img src="images/%s" alt="crime scene">
            <span style="width:500px;">Crime Scene</span>
            </span>""" % (row[8])
            time_line.write(panel6)
        panel8 = """
            </div>
            <!-- Victim infobox pictures ends here -->
            <!-- Victim infobox text starts here -->
            <div class="text">
            <p><b>%s</b>%s</p>
            </div><!-- end of text -->
            </div><!-- end of answer -->
            <!-- Victim infobox ends here -->\n\n\n\n\n\n
            """ % (row[11], row[10])
        time_line.write(panel8)
        number += 1

panel_three()