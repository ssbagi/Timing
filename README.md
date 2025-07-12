# Timing
The Report Timing. 

It's just a thought way of thinking. This might have already been done also. 

Google provides the Image datasets, Classifier and Pre-built trained models ready ones. 

So, similarly Synopysys, Cadence, MG and third parties can also provide the data. Even the Foundries give the Standard Cell Transition, delays, caps in Table format. 
The table formats like Interpolation and  Extrapolation concepts are used for predicting or calculating the delays. We did basic calculations in college as part of coursework. 

- INV - INV   : The distance can be 5units, 10 units, 15units ......... 200 ....... 500units. So, Measure the tr, tf, td, cap, diving strength.
- INV - BUF  :
- BUF - BUF :
- NOT - NOT :

- Like this for all combinations of the logic gates. Like different test cases scenarios like how we verify the chip, DUT, validation or use cases Performance, Power or anything. 

- Make a huge list now we have AI. It can generate a random list the same way like how we do in Verification. The Random constraints concepts just this time we will include in constraints list the logic gates and distance in one more list. It has to place these stuff in Synopsys ICC2 tool and run the timing analysis and collect the things. 

Similarly now for Flip-Flops :

- STA book J Bhasker : All the 8 case scenarios which were taught for us in college. Similar tweaking like above generates the test cases and measures the timing delay. 
Next once the timing report is generated, now use script to parse and have pre-conditions set for that path. Like we can say the cap value, tr value, fanout value. If there are violations, create a cell list like how we did in college in TCL script INV list, buffer list, Logic gates list. Keep all the cells in it. When it wants to upsize it based on the index it will upgrade or downsize it will downgrade.

- Step 9 can create a catastrophe like a chain reaction where you try to fix one it might affect others or the optimization is such that it takes longer time to do. Dependency of things. There can be a lot of scenarios also.

- In similar additional test cases and concepts can be linked or added. Like the CDC, DCD and different scenarios aslo.  
There can be limits so it doesn't go into a lot of optimization or longer duration. 


## Top Level Analysis

Based on the Report like : In below we observe the cell name followed by pin :
 
- Count the No. of Inverter or Buffer present in the Clock path : Top Analysis Easy feedback. (It's just Regular Expression script can be written in Python)
  - count inverter cells
  - count buffer cells.
  - Segregate based on the strength of the cells. 

Consider this as one top level of giving feedback on the clock paths. Like In general Replace the long cells of Buffer with few Inverter cells.
If the degradation is more in any path then add a buffer in between the inverter path. Not changing the logic. Retain the logic. 

<img width="940" height="528" alt="image" src="https://github.com/user-attachments/assets/fd996f07-fab5-4969-8870-1b9dd4faa2c3" />

## Script 

The script is attached in this GitHub. The Method flow is simple :
- STEP1 : Feed one Timing Report.
- STEP2 : In Log File we can see the Number of Inverter Cells, Buffer Cells and with respect to their strength.
- STEP3 : In the Excel File for each path we can see the count written. 




