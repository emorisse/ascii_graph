# ascii_graph
basic plotting in python with ascii output for use in command line etc with minimal dependencies

# example
```
$ python ascii_graph.py input.csv 
16.0	           *
15.2	            
14.4	            
13.6	            
12.8	            
12.0	            
11.2	            
10.4	            
9.6	            
8.8	        *   
8.0	       * *  
7.2	            
6.4	      *   * 
5.6	     *      
4.8	    *       
4.0	   *        
3.2	            
2.4	  *         
1.6	 *          
0.8	*           
```

# ideas on how you can help
* Take a look at my bounds checking, I'm often off by 1 in indicie assignment.
* I don't bucket horizontally, so if you have more inputs than your terminal width, this is going to be ugly
* How to format the vertical axis labels. Eg, if there's a wide spread in digits in the labels, eg 0 vs 1,000,000, rounding and spacing between the labels and the \* won't line up the same
