1. first go to teacher details page to have an idea about how use state and use effect works and how request is send to the backend and things

2. then go to teacher register page and read the comments from there especially about hooks and spread operator

3. after register teache next work is done on teacher login page

4. after login completion category is added through django admin, and additional change is modification of add course which new module add chapter is inluded.
In the add course page we can get the categroy from backend.

5. after this we have to upload course image so we have to intall a package pip install pillow.

6. after that we have to fetch the uploaded content from the backend. for that we are making some changes in the backend, inorder to fetch the courses according to the teacher we are passing the id along with the boolean json response.
 and the id is received in the front end and we save the id in the local storage. you can check the login page.

7. In order to fetch images from the backend and display it on the front end we have to put media_url, media_root inside the settings.py folder in the backend. do some research on it.

 the process to display image is a big task changes have been done in the urls.py of the django main project folder not in the app urls.py folder, and some thing is added like 'static', you have to go there and read the comments. including the imported modules like 'os.path.something' understand why this these things are used and what is happening.


8. when we are adding the chapter we need to pass the id of the course dynaimically. for that we have to get the id from the url using 'useparams()' hook.
befor that we have to install 'react router dom' package. do some research on it.

9. spend some time on adding course and chapters working. In terms of what is happening in models and how the currect chapter is passed to the correct course

10. finished login page error message. for that to happen we have created a usestate and we created an error message which will store in to the state whenever bool : false is returned from the backend.

11. in order to display the video from the backend we have to input the video tag. 

12. inorder to apply sweet alert first install it and import it in the component that you are going to apply it. sweet alert 2 is the installed version.

