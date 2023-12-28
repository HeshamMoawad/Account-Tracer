import React, { useEffect, useState } from "react";
import AgentCard from "./AgentCard/AgentCard";
import AgentCardLoading from "./Loading/AgentCardLoading";
import Filter from "./Filter/Filter";
import axios from "axios";
import { AgentsURL, ProjectsURL } from "../../../Constants";

const AgentsPage = () => {
  const [agents, setAgents] = useState(null);
  const [projects, setProjects] = useState([]);
  const [filterProjects, setFilterProjects] = useState([]);

  useEffect(() => {
    axios     // endpoint connection here
      .get(ProjectsURL)
      .then((data) => {
        setProjects(data.data);
      })
      .catch((error) => {
        console.log(error);
      });
    
  }, []);

  useEffect(() => {
    const params = (filterProjects ? new URLSearchParams({"filter":filterProjects}).toString(): null )
    axios     // endpoint connection here
      .get(AgentsURL+ `?${params}` )
      .then((data) => {
        setAgents(data.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, [filterProjects]);

  return (
    <>
      <h1 className="h1 text-center mb-5 text-dark">All Agents Twitter </h1>
      <div className="container">
        <div className="row text-center">
          <Filter
            filterProjects={filterProjects}
            setFilterProjects={setFilterProjects}
            projects={projects}
          />
          <div className="container">
            <div className="row">
              {Array.isArray(agents) ? (
                agents.length === 0 ? (
                  <div className="alert alert-warning text-center" role="alert">
                    No Accounts Found 
                    <br/>
                    Please choose Project
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
