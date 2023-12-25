import React, { useEffect, useState } from "react";
import LoadingCardContainer from "./Loading/LoadingCardContainer";
import axios from "axios";
import refreshImg from "../../../assets/refresh-white.png";
import CardContainer from './AccountCard/CardContainer';
import { useParams } from "react-router-dom";

const AccountsPage = () => {
  const {agentName} = useParams();
  const [data, setData] = useState(null);
  const [refresh, setRefresh] = useState(0);

  // useEffect(() => {
    // endpoint connection here

  //   axios
  //     .get(Testing)
  //     .then((response) => setData(response.data))
  //     .catch((error) => {
  //       console.error("Error fetching data:", error);
  //       setData({});
  //     });
  // }, [refresh]);

  const accs = [
  ];
  return (
    <>
    <h1 className='h1 text-center'>All Accounts of {agentName ? agentName : 'Not Found'}</h1>
      <div className="container" key={"topcontainer"}>
        <div className="row">
          <div
            className="btn-group mx-auto "
            role="group"
            aria-label="Basic example"
          >
            <button
              className="btn btn-outline-success col-4 shadow-lg"
              type="button"
              id="add-account-btn"
            >
              Add Account
            </button>
            <button
              className="btn btn-primary col shadow-lg"
              type="button"
              id="refresh-account-btn"
              onClick={() => setRefresh(Math.random())}
            >
              <img src={refreshImg} alt="" />
            </button>
          </div>
        </div>
      </div>

      {data ? <CardContainer accounts={accs} /> : <LoadingCardContainer />}
    </>
  );
};

export default AccountsPage;
