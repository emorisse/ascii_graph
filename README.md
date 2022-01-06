# ascii_graph
basic plotting in python with ascii output for use in command line etc with minimal dependencies

# example
```
$ python ascii_graph.py input.csv 
   16.0000	           *
   15.2000	            
   14.4000	            
   13.6000	            
   12.8000	            
   12.0000	            
   11.2000	            
   10.4000	            
    9.6000	            
    8.8000	        *   
    8.0000	       * *  
    7.2000	            
    6.4000	      *   * 
    5.6000	     *      
    4.8000	    *       
    4.0000	   *        
    3.2000	            
    2.4000	  *         
    1.6000	 *          
    0.8000	*           
         
```

# ideas on how you can help
* Take a look at my bounds checking, I'm often off by 1 in indicie assignment.
* I don't bucket horizontally, so if you have more inputs than your terminal width, this is going to be ugly
* How to format the vertical axis labels. Eg, if there's a wide spread in digits in the labels, eg 0 vs 1,000,000, rounding and spacing between the labels and the \* won't line up the same
