import React from "react";
import AccountCard from "./AccountCard";

const CardContainer = (props) => {
  return (
    <>
      <div className="container text-center">
        <div className="row">
          {props.accounts ? (
            props.accounts.map((acc) => {
              return <AccountCard account={acc} key={Math.random()}/>;
            })
          ) : (
            <div className="alert alert-warning" role="alert">
              No Accounts Found
            </div>
          )}
        </div>
      </div>
    </>
  );
};

export default CardContainer;
