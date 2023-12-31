import React from 'react';
import Popup from '../Popup/Popup';

const LineInfo = (props) => {
    const { title , value , hasButton } = props


    return (
        <div className='row mt-3 mb-3'>
            <h3 className='col-7 text-left h3'>{title} : {value} </h3>
            {hasButton? (
                <Popup  name={title}/>
            ) : null }
        </div>
    );
}

export default LineInfo;
