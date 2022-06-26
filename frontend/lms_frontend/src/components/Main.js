import Footer from './footer';
import Header from './Header';
import Home from './Home'
import About from './About';

// User  
import CourseDetail from './CourseDetail';
import Login from './User/login';
import Register from './User/Register';
import Dashboard from './User/Dashboard';
import Mycourses from './User/Mycourses';
import Favourite from './User/Favourite';
import Recommended from './User/Recommended';
import Changepassword from './User/Changepassword';
import Profilesetting from './User/Profilesetting';

import { Routes as Switch,Route } from 'react-router-dom'

// Teacher 
import TeacherLogin from './Teacher/Teacherlogin';
import TeacherRegister from './Teacher/TeacherRegister';
import TeacherDashboard from './Teacher/TeacherDashboard';
import TeacherMycourses from './Teacher/TeacherMycourses';
import TeacherFavourite from './Teacher/TeacherAddcourse';
import TeacherRecommended from './Teacher/TeacherRecommended';
import TeacherProfilesetting from './Teacher/TeacherProfilesetting';
import TeacherChangepassword from './Teacher/TeacherChangepassword';
import TeacherDetails from './Teacher/TeacherDetail';
import AllCourses from './AllCourses';
import PopularCourses from './PopularCourses';
import PopularTeachers from './PopularTeachers';
import CategoryCourses from './CategoryCourses';
import TeacherLogout from './Teacher/TeacherLogout';
import TeacherAddchapter from './Teacher/TeacherAddchapter';






function Main() {
  return (
    <div className="App">
      <Header />
      <Switch>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/detail/:course_id" element={<CourseDetail />} /> {/* here the course_id is passed to the component and useParams is used to pass the data which is passed through the url */}
        <Route path="/AllCourses" element={<AllCourses />} />
        <Route path="/popular-courses" element={<PopularCourses />} />
        <Route path="/popular-teachers" element={<PopularTeachers />} />
        <Route path="/Category/:category_slug" element={<CategoryCourses />} />

        {/* User  */}
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/mycourses" element={<Mycourses />} />
        <Route path="/favourite" element={<Favourite />} />
        <Route path="/recommended" element={<Recommended />} />
        <Route path="/profilesetting" element={<Profilesetting />} />
        <Route path="/changepassword" element={<Changepassword />} />

        {/* Teacher  */}
        <Route path="/teacher-login" element={<TeacherLogin />} />
        <Route path="/teacher-logout" element={<TeacherLogout />} />
        <Route path="/teacher-register" element={<TeacherRegister />} />
        <Route path="/teacher-dashboard" element={<TeacherDashboard />} />
        <Route path="teacher-mycourses" element={<TeacherMycourses />} />
        <Route path="/teacher-addcourse" element={<TeacherFavourite />} />
        <Route path="/teacher-mycourses/teacher-addchapter/:course_id" element={<TeacherAddchapter />} />
        <Route path="/teacher-recommended" element={<TeacherRecommended />} />
        <Route path="/teacher-profilesetting" element={<TeacherProfilesetting />} />
        <Route path="/teacher-changepassword" element={<TeacherChangepassword />} />
        <Route path="/teacher-details/:teacher_id" element={<TeacherDetails />} />
        

      </Switch> 
      <Footer />
    </div>
  );
}

export default Main;