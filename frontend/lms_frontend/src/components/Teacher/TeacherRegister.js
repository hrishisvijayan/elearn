import {Link}  from 'react-router-dom'
import {useEffect} from 'react'

function TeacherRegister(){
    useEffect(()=>{
        document.title='Teacher Register'
    })
    return(
        <div className='container mt-4' >
        <div className='row' >
            <div className='col-6 offset-3' >
                <div className='card' >
                    <h3 className='card-header' > Teacher Register </h3>
                    <div className='card-body' >

                        <form>
                            <div className="mb-3">
                                <label for="exampleInputEmail1" className="form-label"> Full Name </label>
                                <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" />
                                    
                            </div>
                            <div className="mb-3">
                                <label for="exampleInputEmail1" className="form-label">Email </label>
                                <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" />
                                    
                            </div>
                            
                            <div className="mb-3">
                                <label for="exampleInputPassword1" className="form-label">Password</label>
                                <input type="password" className="form-control" id="exampleInputPassword1" />
                            </div>

                            <div className="mb-3">
                                <label for="exampleInputEmail1" className="form-label"> Qualification </label>
                                <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" />
                                    
                            </div>

                            <div className="mb-3">
                                <label for="exampleInputEmail1" className="form-label"> Mobile Number </label>
                                <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" />
                                    
                            </div>

                            <div className="mb-3">
                                <label for="exampleInputEmail1" className="form-label"> Skills </label>
                                <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" />
                                <div id="emailHelp" class="form-text"> Python,JavaScript,Php,etc. </div>    
                            </div>
                            
                            <div className="mb-3 form-check">
                                <input type="checkbox" className="form-check-input" id="exampleCheck1" />
                                    <label className="form-check-label" for="exampleCheck1">Remember Me</label>
                            </div>
                            <button type="submit" className="btn btn-primary"> Login </button>
                        </form>

                    </div>

                </div>
            </div>
        </div>
    </div>
    )
   
}
export default TeacherRegister;


