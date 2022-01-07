# ascii_graph
basic plotting in python with ascii output for use in command line etc with minimal dependencies

# example
```
$ python ascii_graph.py input.csv 
     16.00	           *
     15.21	            
     14.42	            
     13.63	            
     12.84	            
     12.05	            
     11.26	            
     10.47	            
      9.68	            
      8.89	        *   
      8.11	            
      7.32	       * *  
      6.53	      *   * 
      5.74	     *      
      4.95	    *       
      4.16	            
      3.37	   *        
      2.58	  *         
      1.79	 *          
      1.00	*         
         
```

# ideas on how you can help
* Take a look at my bounds checking, I'm often off by 1 in indicie assignment.
* I don't bucket horizontally, so if you have more inputs than your terminal width, this is going to be ugly
* How to format the vertical axis labels. Eg, if there's a wide spread in digits in the labels, eg 0 vs 1,000,000, rounding and spacing between the labels and the \* won't line up the same
