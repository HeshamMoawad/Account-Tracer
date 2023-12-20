import React from 'react';
import AgentCard , {Agent} from './AgentCard/AgentCard';



const AgentsPage = () => {
    return (
        <>
            <h1 className='h1 text-center mb-5 text-dark'>All Agents Twitter </h1>
            <div className='container'>
                <div className='row'>
                    <AgentCard agent={Agent()}  key={"5"}/>
                    <AgentCard agent={Agent()}  key={"8"}/>
                    <AgentCard agent={Agent()}  key={"5955"}/>
                    <AgentCard agent={Agent()}  key={"5957895"}/>
                    <AgentCard agent={Agent()}  key={"5789955"}/>

                </div>
            </div>

        </>
    );
}

export default AgentsPage;
