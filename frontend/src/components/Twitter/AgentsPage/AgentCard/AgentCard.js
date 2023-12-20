import React from 'react';
import './AgentCard.css';

const Agent = ()=>{return{
    name:'ahmed' ,
    project:'alamia' ,
    account_count : 5 
}}
const AgentCard = (props) => {
    const agent = props.agent
    return (
        <div className='m-auto col-xs-1 col-lg-4 col-md-4'>  
            <div className="card mb-3 mx-auto shadow-lg text-center" id='card'>
            <div className="card-header h5">{agent.name} - {agent.project}</div>
            <div className="card-body">
                <h5 className="card-title mb-3">Account : {agent.account_count}</h5>
                <a href="##" className="btn btn-primary">
                Go to {agent.name} Accounts
                </a>
            </div>
            </div>
        </div>
    );
}

export {Agent};
export default AgentCard;
