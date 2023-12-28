import React, { useEffect, useState } from "react";
import LoadingCardContainer from "./Loading/LoadingCardContainer";
import axios from "axios";
import CardContainer from "./AccountCard/CardContainer";
import { useParams } from "react-router-dom";
import { CheckExistAccountURL  , AccountsURL } from "../../../Constants";

const AccountsPage = () => {
  const { agentName, project } = useParams();
  const [data, setData] = useState(null);
  const [isExist, setIsExist] = useState(false);
  useEffect(() => {
    // endpoint connection here
    const params = new URLSearchParams({
      agentName: agentName,
      project: project,
    });
    axios
      .get(CheckExistAccountURL + "?" + params)
      .then((response) => {
        setIsExist(true);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  useEffect(() => {
    // endpoint connection here
    const params = new URLSearchParams({
      agent: agentName,
      project: project,
    });
    axios
      .get(AccountsURL + "?" + params)
      .then((response) => {
        setData(response.data);
        console.log(response.data);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
        setData({});
      });
  }, []);


  return (
    <>
      <h1 className="h1 text-center">
        All Accounts of {agentName ? agentName : "Not Found"}
      </h1>
      <br />
      <div className="container" key={"topcontainer"}>
        <div className="row" style={{ margin: "30px" }}></div>
      </div>
      {!isExist ? (
        <div className="alert alert-warning text-center" role="alert">
          No Accounts Found
          <br />
          Please choose Project
        </div>
      ) : null}
      {isExist ? (
        data ? (
          <CardContainer accounts={data} />
        ) : (
          <LoadingCardContainer />
        )
      ) : null}
    </>
  );
};

export default AccountsPage;
