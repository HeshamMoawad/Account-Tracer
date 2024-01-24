import React from 'react';
import Logo from '../../assets/logo.jpg'
import './Home.css'

const Home = () => {
    return (
        <>
        <div className="px-4 py-5 my-5 text-center">
        <img
            className="d-block mx-auto mb-4"
            id='banner'
            src={Logo}
            alt=""
        />
        <h1 className="">Welcome to Account Tracer tool</h1>
        <div className="col-lg-6 mx-auto">
            <p className="lead mb-4">
                حبيبى يا ابو الصحاب منورنى و الله
            </p>
            <div className="d-grid gap-2 d-sm-flex justify-content-sm-center">
            </div>
        </div>
        </div>

        </>
    );
}


export default Home;


