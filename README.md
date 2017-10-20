# MakeLumiTable


## Getting Started

Login in the vocms061 machine and go in scratch0/Shifter_scripts/JSON.
```
ssh cctrack@vocms061 -X
cd scratch0/Shifter_scripts/JSON
```
Here you will find *cfgMaker.sh* and *buildTable.py*. To run over a given run range please submit two arguments: the =firstRun= and the =lastRun=; i.e. the first and last runs you certified during your shift.
```
bash
export PATH=$HOME/.local/bin:/afs/cern.ch/cms/lumi/brilconda-1.0.3/bin:$PATH
sh cfgMaker.sh firstRun lastRun beamEnergy && python buildTable.py
```
The =beamEnergy= argument is *optional* and should only be used when not in normal pp collision. In case of pA or HI collisions, please set this parameter to =HI=, which correspond to a beamEnergy of 4000 !GeV. If needed, one can set =beamEnergy= to any value (e.g. =2000=) if the beam conditions are not standard.
      
## Running over a list of runs

To compute the luminosity for a given list of runs, produce a file containing a comma separated list of the runs in question and modify your call to computeLuminosity s.t. it reads 
```
sh cfgMaker.sh firstRun lastRun beamEnergy yourRunList.csv
```
To get output in inverse femtobarns repleace beamEnergy above with "pp".  Note that firstRun and lastRun must contain the range of values filled in yourRunList.csv.

## Output
buildTables outputs to table.html, please feel free to copy this file as necessary.  For instance, copying to /data/users/event_display/RunList/ will make the file available via your web browser at http://vocms061.cern.ch/event_display/RunList/test.html
