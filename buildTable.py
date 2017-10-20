import subprocess
from json2html import json2html
import json
from collections import OrderedDict
cmd = """export PATH=$HOME/.local/bin:/afs/cern.ch/cms/lumi/brilconda-1.0.3/bin:$PATH"""
process = subprocess.check_output(cmd, shell=True)

cmd = """brilcalc lumi  -i JSON_TRK_Collisions2015_weekly_NO_QUALITY.txt"""
process = subprocess.check_output(cmd, shell=True)
no_quality_dump  = process.split("-+\n")#process.split("+-------------+---+------+------+----------------+---------------+")
no_quality_dump  = no_quality_dump[2].split("\n")
cmd = """rm JSON_TRK_Collisions2015_weekly_NO_QUALITY.txt"""
process = subprocess.check_output(cmd, shell=True)

cmd = """brilcalc lumi  -i JSON_TRK_Collisions2015_PIX.txt"""
process = subprocess.check_output(cmd, shell=True)
good_pix_dump  = process.split("-+\n")#process.split("+-------------+---+------+------+----------------+---------------+")
good_pix_dump  = good_pix_dump[2].split("\n")
cmd = """rm JSON_TRK_Collisions2015_PIX.txt"""
process = subprocess.check_output(cmd, shell=True)

fileobj = open("JSON_TRK_Collisions2015_BADPIX.txt","rb")
if (len(fileobj.read()) > 2):
  cmd = """brilcalc lumi  -i JSON_TRK_Collisions2015_BADPIX.txt"""
  process = subprocess.check_output(cmd, shell=True)
  bad_pix_dump  = process.split("-+\n")#process.split("+-------------+---+------+------+----------------+---------------+")
  bad_pix_dump  = bad_pix_dump[2].split("\n")
else:
  bad_pix_dump = []

cmd = """rm JSON_TRK_Collisions2015_BADPIX.txt"""
process = subprocess.check_output(cmd, shell=True)

cmd = """brilcalc lumi  -i JSON_TRK_Collisions2015_TRACK.txt"""
process = subprocess.check_output(cmd, shell=True)
good_track_dump  = process.split("-+\n")#process.split("+-------------+---+------+------+----------------+---------------+")
good_track_dump  = good_track_dump[2].split("\n")
cmd = """rm  JSON_TRK_Collisions2015_TRACK.txt"""
process = subprocess.check_output(cmd, shell=True)


fileobj = open("JSON_TRK_Collisions2015_BADTRACK.txt","rb")
if (len(fileobj.read()) > 2):
  cmd = """brilcalc lumi  -i JSON_TRK_Collisions2015_BADTRACK.txt"""
  process = subprocess.check_output(cmd, shell=True)
  bad_track_dump  = process.split("-+\n")#process.split("+-------------+---+------+------+----------------+---------------+")
  bad_track_dump  = bad_track_dump[2].split("\n")
else:
  bad_track_dump = []
cmd = """rm JSON_TRK_Collisions2015_BADTRACK.txt"""
process = subprocess.check_output(cmd, shell=True)

cmd = """brilcalc lumi  -i JSON_TRK_Collisions2015_STRIP.txt"""
process = subprocess.check_output(cmd, shell=True)
good_strip_dump  = process.split("-+\n")#process.split("+-------------+---+------+------+----------------+---------------+")
good_strip_dump  = good_strip_dump[2].split("\n")
cmd = """rm JSON_TRK_Collisions2015_STRIP.txt"""
process = subprocess.check_output(cmd, shell=True)

fileobj = open("JSON_TRK_Collisions2015_BADSTRIP.txt","rb")
if (len(fileobj.read()) > 2):
  cmd = """brilcalc lumi  -i JSON_TRK_Collisions2015_BADSTRIP.txt"""
  process = subprocess.check_output(cmd, shell=True)
  bad_strip_dump  = process.split("-+\n")
  bad_strip_dump  = bad_strip_dump[2].split("\n")
else:
  bad_strip_dump = []
cmd = """rm JSON_TRK_Collisions2015_BADSTRIP.txt"""
process = subprocess.check_output(cmd, shell=True)


cmd = """brilcalc lumi  -i JSON_TRK_Collisions2015_ALLGOOD.txt"""
process = subprocess.check_output(cmd, shell=True)
good_all_dump  = process.split("-+\n")#process.split("+-------------+---+------+------+----------------+---------------+")
good_all_dump  = good_all_dump[2].split("\n")
cmd = """rm JSON_TRK_Collisions2015_ALLGOOD.txt"""
process = subprocess.check_output(cmd, shell=True)


t2Holder = []
goodRuns   = {}
no_quality_delivered,no_quality_recorded = 0,0
good_strip_delivered,good_strip_recorded = 0,0
bad_strip_recorded = 0
good_pix_delivered,good_pix_recorded = 0,0
bad_pix_recorded = 0
good_track_delivered,good_track_recorded = 0,0
bad_track_recorded = 0
good_all_delivered,good_all_recorded = 0,0
bad_any_delivered,bad_any_recorded = 0,0

for line in good_all_dump:
        if len(line) == 0: continue
        entries =  line.split("|")
	if (len(entries) == 1) : continue
        run = int(entries[1].split(":")[0])
        good_all_delivered += float(entries[-3])/1000000.
        good_all_recorded += float(entries[-2])/1000000.

for line in no_quality_dump:
	if len(line) == 0: continue
	entries =  line.split("|")
        if (len(entries) == 1) : continue

	run = int(entries[1].split(":")[0])
	delivered  =  "%.5f pb" % (float(entries[-3])/1000000.) #+ """<sup>-1</sup>"""# % (float(entries[-3])/1000000.)
	no_quality_delivered += float(entries[-3])/1000000.
	recorded  =  "%.5f pb" % (float(entries[-2])/1000000.) #+ """<sup>-1</sup>""" #% (float(entries[-2])/1000000.)
	no_quality_recorded += float(entries[-2])/1000000.
	goodRuns[run] = len(t2Holder)
	t2Holder.append(OrderedDict([ ("Run" , run),("Lumi Delivered",delivered),("Lumi Recorded",recorded),("PIXEL","TODO"),("STRIP","TODO"),("TRACK","TODO")]))
print("The delivered and recorderd luminosity w/ no quality requirements = %.3f,%.3f, respectively" % (no_quality_delivered,no_quality_recorded))

for line in good_pix_dump:
        if len(line) == 0: continue
	entries =  line.split("|")
        if (len(entries) == 1) : continue

	run = int(entries[1].split(":")[0])
	delivered = float(entries[-3])/1000000				        
	good_pix_delivered += delivered				        
	recorded  = float(entries[-2])/1000000					        
	good_pix_recorded += recorded
	for entry in t2Holder:
		try:
			t2Holder[goodRuns[run]]["PIXEL"] = "GOOD"
		except:
			pass
print("The delivered and recorderd luminosity w/ pixel quality requirements = %.3f,%.3f, respectively" % (good_pix_delivered,good_pix_recorded))

for line in good_strip_dump:
        if len(line) == 0: continue
        entries =  line.split("|")
        if (len(entries) == 1) : continue

	run = int(entries[1].split(":")[0])
        delivered = float(entries[-3])/1000000
        good_strip_delivered += delivered
        recorded  = float(entries[-2])/1000000
        good_strip_recorded += recorded
        for entry in t2Holder:
                try:
                        t2Holder[goodRuns[run]]["STRIP"] = "GOOD"
                except:
                        pass

print("The delivered and recorderd luminosity w/ strip quality requirements = %.3f,%.3f, respectively" % (good_strip_delivered,good_strip_recorded))

for line in good_track_dump:
        if len(line) == 0: continue
        entries =  line.split("|")
        if (len(entries) == 1) : continue

	run = int(entries[1].split(":")[0])
        delivered = float(entries[-3])/1000000
        good_track_delivered += delivered
        recorded  = float(entries[-2])/1000000
        good_track_recorded += recorded
        for entry in t2Holder:
                try:
                        t2Holder[goodRuns[run]]["TRACK"] = "GOOD"
                except:
                        pass

d_ = {}
q_ = {}
for line in bad_track_dump:
        if len(line) == 0: continue
        entries =  line.split("|")
        if (len(entries) == 1) : continue

	run = int(entries[1].split(":")[0])
        for entry in t2Holder:
                try:
                        if run not in q_:
                                q_[run] = 0
			else:	
				continue
			t2Holder[goodRuns[run]]["TRACK"] = "BAD"
		        recorded  = float(t2Holder[goodRuns[run]]["Lumi Recorded"].replace("pb",""))
			bad_track_recorded += recorded
			if run not in d_: 
				d_[run] = 0
				bad_any_recorded += recorded
                except:
                        pass
q_ = {}
for line in bad_pix_dump:
        if len(line) == 0: continue
        entries =  line.split("|")
        if (len(entries) == 1) : continue

	run = int(entries[1].split(":")[0])
        for entry in t2Holder:
                try:
                        if run not in q_:
                                q_[run] = 0                     
                        else:   
                                continue

			t2Holder[goodRuns[run]]["PIXEL"] = "BAD"
                        recorded  = float(t2Holder[goodRuns[run]]["Lumi Recorded"].replace("pb ",""))
			bad_pix_recorded += recorded			
                        if run not in d_:
                                d_[run] = 0
                                bad_any_recorded += recorded
                except:
                        pass			

q_ = {}
for line in bad_strip_dump:
        if len(line) == 0: continue
        entries =  line.split("|")
        if (len(entries) == 1) : continue

        run = int(entries[1].split(":")[0])
        for entry in t2Holder:
                try:
                        if run not in q_:
                                q_[run] = 0                     
                        else:   
                                continue

                        t2Holder[goodRuns[run]]["STRIP"] = "BAD"
                        recorded  = float(t2Holder[goodRuns[run]]["Lumi Recorded"].replace("pb",""))
                        bad_strip_recorded += recorded
                        if run not in d_:
                                d_[run] = 0
                                bad_any_recorded += recorded
                except:
                        pass



print("The delivered and recorderd luminosity w/ track quality requirements = %.3f,%.3f, respectively" % (good_track_delivered,good_track_recorded))
t2 = json2html.convert( json = json.dumps(t2Holder)  )
t2 = t2.replace("<td>GOOD","<td class=\"GOOD\">GOOD")
t2 = t2.replace("<td>BAD","<td class=\"BAD\">BAD")
t2 = t2.replace("<td>TODO","<td class=\"TODO\">TODO")
t2 = t2.replace("pb","pb<sup>-1</sup>")
import time
now = time.strftime("%c")
htmlHeader = """

<html>
<head>
  <title>Certification Status</title>
  <style type='text/css'>
    body { font-family: "Candara", sans-serif; }
    td.BAD { background-color: rgb(255,100,100); }
    td.bah { background-color: rgb(255,180,80); }
    td.GOOD { background-color: rgb(100,255,100); }
    td.TODO { background-color: yellow; }
    td.WAIT { background-color: rgb(200,200,255); }
    td.Wait { background-color: rgb(200,230,255); }
    td.SKIP { background-color: rgb(200,200,200); }
    td, th { padding: 1px 5px;
             background-color: rgb(200,200,200);
             margin: 0 0;  }
    td.num { text-align: right; padding: 1px 10px; }
    table, tr { background-color: black; }
  </style>
</head>
<body>
<h1>Certification Status, Collisions17 """ + now + """</h1>"""


t1Holder = []
t1Holder.append( OrderedDict([
("GOOD Recorded Summary", OrderedDict([	("No Quality" , "%.2f fb" % (no_quality_recorded/1000.)), 
									("GOOD Track" , "%.2f fb" % (good_track_recorded/1000.)), 
									("GOOD PIXEL" , "%.2f fb" %(good_pix_recorded/1000.)), 
									("GOOD STRIP" , "%.2f fb" % (good_strip_recorded/1000.)), 
									("ALL GOOD + ALL FLAGS" , "%.2f fb" % (good_all_recorded/1000.))]) ),
	                                ("BAD Recorded Summary", OrderedDict([ ("No Quality" , "%.3f fb" % (no_quality_recorded/1000.)), 
                                                                        ("BAD Track" , "%.3f fb" % (bad_track_recorded/1000.)),
                                                                        ("BAD PIXEL" , "%.3f fb" %(bad_pix_recorded/1000.)),
                                                                        ("BAD STRIP" , "%.3f fb" % (bad_strip_recorded/1000.)),
                                                                        ("ANY BAD" , "%.3f fb" % (bad_any_recorded/1000.))])) ]))

t1 = json2html.convert( json = json.dumps(t1Holder)  )
t1 = t1.replace("fb","fb<sup>-1</sup>")

html = htmlHeader + t1 + t2 + """</body> \n </html>"""

f = open('table.html', 'w')
f.write(html)
f.close()
