import { Link, useParams } from 'react-router-dom'

function CourseDetail() {
    let { course_id } = useParams()
    return (
        <div className='container mt-3'>
            <div className='row'>
                <div className='col-4'>
                    <img src="/logo512.png" className="img-thumbnail" alt="..." />
                </div>
                <div className='col-8 '>
                    <h3>Course Title</h3>
                    <p>
                        Lorem Ipsum is simply dummy text of the printing and typesetting industry.
                        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
                        when an unknown printer took a galley of type and scrambled it to make a type specimen book.
                        It has survived not only five centuries, but also the leap into electronic typesetting,
                        remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset
                        sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like
                        Aldus PageMaker including versions of Lorem Ipsum.</p>
                    <p className='fw-bold'>
                        Course By:
                        <Link to="/teacher-details/1">
                            Teacher 1
                        </Link>
                    </p>
                    <p className='fw-bold'>
                        Duration: 3 hours 30 minutes
                    </p>
                    <p className='fw-bold'>
                        Total Enrolled: 427 students
                    </p>
                    <p className='fw-bold'>
                        Rating: 4.5/5
                    </p>
                </div>
            </div>
            {/* course videos */}
            <div className="card" >
                <div className="card-header">
                    <h3> Course Videos </h3>
                </div>
                <ul className="list-group list-group-flush">
                    <li className="list-group-item "> Introduction
                        <span className='me-3' > 1:30 mins </span>
                        <button className='btn btn-sm btn-danger float-right ' data-bs-toggle="modal" data-bs-target="#VideoModal1">     <i className="bi bi-youtube"></i> </button>

                        {/* modal start  */}
                        <div className="modal fade" id="VideoModal1" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                            <div className="modal-dialog modal-xl">
                                <div className="modal-content">
                                    <div className="modal-header">
                                        <h5 className="modal-title" id="exampleModalLabel">Video 1</h5>
                                        <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div className="modal-body">
                                        <div class="ratio ratio-16x9">
                                            <iframe src="https://www.youtube.com/embed/zpOULjyy-n8?rel=0" title="YouTube video" allowfullscreen></iframe>
                                        </div>
                                    </div>

                                </div>
                            </div>
                        </div>
                        {/* video modal end  */}

                    </li>  {/* float right is not working */}
                    <li className="list-group-item "> Introduction
                        <span className='me-3' > 1:30 mins </span>
                        <button className='btn btn-sm btn-danger float-right ' >   <i className="bi bi-youtube"></i> </button>
                    </li>  {/* float right is not working */}
                    <li className="list-group-item "> Introduction
                        <span className='me-3' > 1:30 mins </span>
                        <button className='btn btn-sm btn-danger float-right ' >   <i className="bi bi-youtube"></i> </button>
                    </li>  {/* float right is not working */}
                    <li className="list-group-item "> Introduction
                        <span className='me-3' > 1:30 mins </span>
                        <button className='btn btn-sm btn-danger float-right ' >   <i className="bi bi-youtube"></i> </button>
                    </li>  {/* float right is not working */}

                </ul>
            </div>

            {/* related courses starts heres */}
            <h3 className=" pb-1 mb-2 mt-5" >Related Courses <a href="#" className="float-end" >See All</a> </h3>
            <div className="row" >
                <div className="col-md-3 " >
                    <div className="card" >
                        <img src="/logo512.png" className="card-img-top" alt="..." />
                        <div className="card-body">
                            <h5 className="card-title"> <a href="#"> Course title </a>  </h5>
                        </div>
                    </div>
                </div>

                <div className="col-md-3 " >
                    <div className="card" >
                        <img src="/logo512.png" className="card-img-top" alt="..." />
                        <div className="card-body">
                            <h5 className="card-title"> <a href="#"> Course title </a>  </h5>
                        </div>
                    </div>
                </div>

                <div className="col-md-3 " >
                    <div className="card" >
                        <img src="/logo512.png" className="card-img-top" alt="..." />
                        <div className="card-body">
                            <h5 className="card-title"> <a href="#"> Course title </a>  </h5>
                        </div>
                    </div>
                </div>

                <div className="col-md-3 " >
                    <div className="card" >
                        <img src="/logo512.png" className="card-img-top" alt="..." />
                        <div className="card-body">
                            <h5 className="card-title"> <a href="#"> Course title </a>  </h5>
                        </div>
                    </div>
                </div>
            </div>
            {/* related courses ends heres */}

        </div>
    )
}


export default CourseDetail;
