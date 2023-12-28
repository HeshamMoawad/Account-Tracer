import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const AnalyticsPage = () => {
    const {handle} = useParams();
    const [isExist , setIsExist] = useState(false);

    // for chack exist handle 
    useEffect(()=>{
        // endpoint here
    });

    // fetch account info
    useEffect(()=>{

    });


    return (
        <div className='container text-left '>
            <div className='row'>
                <div className="card mx-auto shadow-lg"  style={{ width: "18rem" , minWidth:"1000px" }}>
                    <div className="card-body">
                        <h5 className="card-title text-center h1">{isExist ? handle : "Not Found " + handle }</h5>

                    </div>
                </div>
            </div>
        </div>
    );
}

export default AnalyticsPage;
