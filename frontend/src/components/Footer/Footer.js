import React from 'react';
import {Link} from 'react-router-dom';


import facebook from '../../assets/facebook.png' ;
import whatsapp from '../../assets/whatsapp.png';
import x from '../../assets/x.png';
import instgram from '../../assets/instagram.png';
import Logo from '../../assets/testLogo.jpg';



const Footer = () => {
    return (
        <>
            <div className="container">
            <footer className="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
                <div className="col-md-4 d-flex align-items-center">
                <a
                    href="/"
                    className="mb-3 me-2 mb-md-0 text-body-secondary text-decoration-none lh-1"
                >
                    <img src={Logo} alt="Logo" width="40" height="30" />


                </a>
                <span className="mb-3 mb-md-0 text-body-secondary">
                    © 2023 El-Alamia Company, Inc
                </span>
                </div>
                <ul className="nav col-md-4 justify-content-end list-unstyled d-flex">
                <li className="ms-3">
                    <Link className="text-body-secondary" to="">
                        <img src={facebook} alt="Bootstrap" width="30" height="24" />
                    </Link>
                </li>
                <li className="ms-3">
                    <Link className="text-body-secondary" to="">
                        <img src={whatsapp} alt="Bootstrap" width="30" height="24" />
                    </Link>
                </li>
                <li className="ms-3">
                    <Link className="text-body-secondary" to="">
                        <img src={x} alt="Bootstrap" width="30" height="24" />
                    </Link>
                </li>
                <li className="ms-3">
                    <Link className="text-body-secondary" to="">
                        <img src={instgram} alt="Bootstrap" width="30" height="24"/>
                    </Link>
                </li>
                </ul>
            </footer>
            </div>
        </>
    );
}

export default Footer;
