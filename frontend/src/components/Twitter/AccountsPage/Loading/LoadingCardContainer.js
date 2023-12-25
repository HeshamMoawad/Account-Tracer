import React from 'react';
import './LoadingCardContainer.css';

const LoadingCardContainer = () => {
    const LoadingCard = (key)=>{return(        
            <div className="card mb-3 mx-auto" style={{ maxWidth: 540 }} id="cardlayer" aria-hidden="true" key={key}>
            <div className="row g-0">
                <div className="col-md-4 mt-2 placeholder-glow">
                <span className="placeholder col-12" id='img-loading'></span>
                {/* <span className="placeholder col-12"></span>
                <span className="placeholder col-12"></span>
                <span className="placeholder col-12"></span>
                <span className="placeholder col-12"></span> */}
                </div>
                <div className="col-md-8">
                <div className="card-body">
                    <h5 className="card-title placeholder-glow">
                        <span className="placeholder col-6"></span>
                    </h5>
                    <p className="card-text placeholder-glow">
                        <span className="placeholder col-7"></span>
                    </p>
                    <div className="btn-group" role="group" aria-label="Basic example">
                        <button type="button" className="btn btn-primary disabled placeholder">
                            ...
                        </button>
                    <button type="button" className="btn btn-danger disabled placeholder">
                        ...
                    </button>
                    </div>
                </div>
                </div>
            </div>
            </div>
)}
    return (
        <div>
        <div className="container text-center">
            <div className="row">
            {LoadingCard(Math.random())}
            {LoadingCard(Math.random())}
            </div>
        </div>

        </div>
    );
}

export default LoadingCardContainer;
