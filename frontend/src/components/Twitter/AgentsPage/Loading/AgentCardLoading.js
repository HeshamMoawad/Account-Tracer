import React from 'react';
import '../AgentCard/AgentCard.css'


const AgentCardLoading = () => {
    return (
        <>
            <div className='m-auto col-xs-1 col-lg-4 col-md-4' id='card-container'>  
                <div className="card mb-3 mx-auto shadow-lg text-center" id='card'>
                <div className="card-header h5 placeholder">...</div>
                <div className="card-body">

                    <p className="card-text placeholder-glow">
                        <span className="placeholder col-5"></span>
                        <span className="placeholder col-4"></span>
                    </p>
                    <a href="##" className="btn btn-primary disabled placeholder col-6" aria-disabled="true">
                    ...
                    </a>
                </div>
                </div>
            </div>
            <div className='m-auto col-xs-1 col-lg-4 col-md-4' id='card-container'>  
                <div className="card mb-3 mx-auto shadow-lg text-center" id='card'>
                <div className="card-header h5 placeholder">...</div>
                <div className="card-body">

                    <p className="card-text placeholder-glow">
                        <span className="placeholder col-5"></span>
                        <span className="placeholder col-4"></span>
                    </p>
                    <a href="##" className="btn btn-primary disabled placeholder col-6" aria-disabled="true">
                    ...
                    </a>
                </div>
                </div>
            </div>
            <div className='m-auto col-xs-1 col-lg-4 col-md-4' id='card-container'>  
                <div className="card mb-3 mx-auto shadow-lg text-center" id='card'>
                <div className="card-header h5 placeholder">...</div>
                <div className="card-body">

                    <p className="card-text placeholder-glow">
                        <span className="placeholder col-5"></span>
                        <span className="placeholder col-4"></span>
                    </p>
                    <a href="##" className="btn btn-primary disabled placeholder col-6" aria-disabled="true">
                    ...
                    </a>
                </div>
                </div>
            </div>

        </>
    );
}

export default AgentCardLoading;
