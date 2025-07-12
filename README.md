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




