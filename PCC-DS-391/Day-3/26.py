''' 
  * * * * * 
   * * * * 
    * * * 
     * * 
      * 
      * 
     * * 
    * * * 
   * * * * 
  * * * * * 
'''

for i in range(5):
    print(" " * i, "* " * (5 - i))
for i in range(5):
    print(" " * (5-i-1), "* " * (i+1))