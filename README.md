# ascii_graph
basic plotting in python with ascii output for use in command line etc with minimal dependencies

# example
```
$ python ascii_graph.py input.csv 
16.0	           *
8.0	            
5.3	            
4.0	            
3.2	            
2.7	            
2.3	            
2.0	            
1.8	            
1.6	        *   
1.5	       * *  
1.3	            
1.2	      *   * 
1.1	     *      
1.1	    *       
1.0	   *        
0.9	            
0.9	  *         
0.8	 *          
0.8	*
```

# ideas on how you can help
* Take a look at my bounds checking, I'm often off by 1 in indicie assignment.
* I don't bucket horizontally, so if you have more inputs than your terminal width, this is going to be ugly
