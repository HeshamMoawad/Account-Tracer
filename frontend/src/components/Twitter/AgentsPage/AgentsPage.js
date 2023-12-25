import React, { useEffect, useState } from "react";
import AgentCard, { AgentEx } from "./AgentCard/AgentCard";
import AgentCardLoading from "./Loading/AgentCardLoading";
import Filter from "./Filter/Filter";
import axios from "axios";
import { ProjectsURL } from "../../../Constants";




const AgentsPage = () => {
  const [agents, setAgents] = useState(null);
  const [filterProjects, setFilterProjects] = useState([]);

  useEffect(() => {
    axios
      .get(ProjectsURL)
      .then(data=>{console.log(data)})
      .catch(error=>{console.log(error)})
    // endpoint connection here
    setAgents([AgentEx, AgentEx, AgentEx, AgentEx]);
    console.log(filterProjects)
  }, [filterProjects]);


  const projects = [
    {
      'name' : 'profitway',
      'imgURL' : 'https://profitway.info/images/logo.svg'
    },
    {
      'name' : 'almamlaka',
      'imgURL' : 'https://almamlaka.info/images/logo.svg'
    },
    {
      'name' : 'al3alamia',
      'imgURL' : 'https://al3alamia.info/assets/images/logo.svg'
    },
    {
      'name' : 'trading',
      'imgURL' : 'https://tradingtasi.com/images/trading/logo.svg'
    },
    {
      'name' : 'dddddd',
      'imgURL' : 'https://tradingtasi.com/images/trading/logo.svg'
    },
  ]



  return (
    <>
      <h1 className="h1 text-center mb-5 text-dark">All Agents Twitter </h1>
      <div className="container">
        <div className="row text-center">
          <Filter filterProjects={filterProjects} setFilterProjects={setFilterProjects} projects={projects}/>
          <div className="container">
            <div className="row">
              {Array.isArray(agents) ? (
                agents.length === 0 ? (
                  <div className="alert alert-warning text-center" role="alert">
                    No Accounts Found
                  </div>
                ) : (
                  agents.map((agent) => {
                    return <AgentCard agent={agent} key={Math.random()} />;
                  })
                )
              ) : (
                <AgentCardLoading />
              )}
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default AgentsPage;
