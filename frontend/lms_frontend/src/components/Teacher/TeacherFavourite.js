import { Link } from 'react-router-dom'
import Sidebar from './TeacherSidebar';


function TeacherFavourite() {
    return (
       
        <div className='container mt-4' >
        <div className='row' >
            <aside className='col-md-3' >
                <Sidebar />
            </aside>
            <section className='col-md-9' >
                <div className='card' >
                    <h5 className='card-header' > Add Course </h5>
                    <div className='card-body' >


                        <div class="mb-3 row">
                            <label for="staticEmail" class="col-sm-2 col-form-label"> Title </label>
                            <div class="col-sm-10">
                                <input type="text" readonly class="form-control" id="staticEmail" />
                            </div>
                        </div>
                        <div class="mb-3 row">
                            <label for="staticEmail" class="col-sm-2 col-form-label"> Description </label>
                            <div class="col-sm-10">
                                <input type="text" readonly class="form-control" id="staticEmail" />
                            </div>
                        </div>
                        <div class="mb-3 row">
                            <label for="staticEmail" class="col-sm-2 col-form-label"> Course Video </label>
                            <div class="col-sm-10">
                                <input type="file" readonly class="form-control" id="staticEmail" />
                            </div>
                        </div>
                        

                        <div class="mb-3 row">
                            <label for="staticEmail" class="col-sm-2 col-form-label"> Technologies </label>
                            <div class="col-sm-10">
                                <input type="text" readonly class="form-control" id="staticEmail" />
                            </div>
                        </div>

                        <hr />
                        <button className='btn btn-primary'>Update</button>

                    </div>
                </div>

            </section>
        </div>
    </div>
    )

}
export default TeacherFavourite;