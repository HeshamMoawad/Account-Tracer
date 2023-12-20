import React from 'react';
import Logo from '../../assets/testLogo.jpg'
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
        <h1 className="display-5 fw-bold text-body-emphasis">Welcome to Account Tracer tool</h1>
        <div className="col-lg-6 mx-auto">
            <p className="lead mb-4">
                حبيبى يا ابو الصحاب منورنى و الله
            </p>
            <div className="d-grid gap-2 d-sm-flex justify-content-sm-center">
            <button type="button" className="btn btn-primary btn-lg px-4 gap-3">
                عاوز تعمل حاجة ؟
            </button>
            <button type="button" className="btn btn-outline-secondary btn-lg px-4">
                مش عاوز تعمل حاجة
            </button>
            </div>
        </div>
        </div>

        </>
    );
}


export default Home;


