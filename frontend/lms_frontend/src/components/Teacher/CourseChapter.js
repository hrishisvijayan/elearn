import { Link, useParams } from 'react-router-dom'
import Sidebar from './TeacherSidebar';
import { useState, useEffect } from 'react';
import axios from 'axios';


const baseUrl = 'http://127.0.0.1:8000/api/'



function CourseChapter() {

    const { course_id } = useParams()  //to get the id from the url

    const [chapterData, setChapterData] = useState([])


    useEffect(() => {
        document.title = 'All chapters'

        try {
            axios.get(baseUrl + 'course-chapter/' + course_id).then((res) => {
                console.log(res.data)
                setChapterData(res.data)
            })
        } catch (error) {
            console.log(error)
        }

    }, [])

    return (
        <div className='container mt-4' >
            <div className='row' >
                <aside className='col-md-3' >
                    <Sidebar />
                </aside>
                <section className='col-md-9' >
                    <div className='card' >
                        <h5 className='card-header' > All Chapters </h5>
                        <div className='card-body'>
                            <table className='table table-bordered' >
                                <thead>
                                    <tr>
                                        <th> title </th>
                                        <th> video </th>
                                        <th> remarks </th>
                                        <th> Action </th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {/* why return is not needed here  the data should be written first and index as second */}
                                    {chapterData.map((chapter, index) =>
                                        <tr>
                                            <td><Link to='#' > {chapter.title} </Link>  </td>
                                            <td>

                                                <video controls width="250">

                                                    <source src={ chapter.video.url } type="video/webm" />

                                                    <source src={ chapter.video.url } type="video/mp4" />

                                                    Sorry, your browser doesn't support embedded videos.
                                                </video>

                                            </td> {/* video is pending we will deal with this later */}
                                            <td> {chapter.remarks}  </td>
                                            <td>
                                                <button className='btn btn-danger btn-sm m-2' > Delete </button>
                                                <button className='btn btn-info btn-sm m-2' > Edit </button>

                                            </td>

                                        </tr>
                                    )}
                                </tbody>

                            </table>
                        </div>

                    </div>

                </section>
            </div>
        </div>

    )
}

export default CourseChapter;
