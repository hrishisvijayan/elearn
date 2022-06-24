1. parsing error -syntax error
2. not defined   - not initialized the variable like const handlechange

3. network error -
   1. the backend may not be running so just run it.
   2. axios is not getting the response due to cross site origin policy. 
   so inorder to fix this you have to install corsheader and inlude it in apps and middleware and down below in setting you have to allow all origins or specific urls in it.