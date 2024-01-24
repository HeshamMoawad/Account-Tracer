import React from 'react';
import './Nav.css'
// import Logo from '../../assets/testLogo.jpg'
import Logo from '../../assets/logo.jpg'
import { Link } from 'react-router-dom';



const Nav = () => {
    return (
        <>
            <div className="container">
            <header className="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 mb-4 border-bottom">
                <div className="col-md-3 mb-2 mb-md-0">
                <a
                    href="/"
                    className="d-inline-flex link-body-emphasis text-decoration-none"
                >
                <img src={Logo} alt="Bootstrap" width="100" height="50" />
                </a>
                </div>
                <ul className="nav col-12 col-md-auto mb-2 justify-content-center mb-md-0">
                <li>
                    <Link to="" className="text-white fw-bold px-2">
                    Home
                    </Link>
                </li>
                <li>
                    <Link to="twitter" className="text-white fw-bold px-2">
                    Twitter
                    </Link>
                </li>
                <li>
                    <Link to="tiktok" className="text-white fw-bold px-2">
                    TikTok
                    </Link>
                </li>
                </ul>
                <div className="col-md-3 text-end">
                </div>
            </header>
            </div>
        </>
    );
}


export default Nav;
