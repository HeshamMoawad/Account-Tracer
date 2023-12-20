import React, { Fragment } from "react";
import "./AccountCard.css";

const example = ()=>{return{
  id: `${Math.random()}`,
  name: "name",
  handle: "handle",
  descreption: "descreption",
  profileImgURL: "https://img.icons8.com/?size=256&id=32309&format=png",
}};

const Card = (props , key) => {
  const account = props.account
  return (
    <>
      {account ? ( 
        <div className="card mb-3 mx-auto shadow-lg" style={{ maxWidth: 540 }} id="cardlayer" key={key} >
          <div className="row g-0" >
            <div className="col-md-4">
              <img
                src={account.profileImgURL}
                className="img-fluid rounded-start"
                alt=""
              />
            </div>
            <div className="col-md-8">
              <div className="card-body">
                <h5 className="card-title">
                  {account.name ? account.name : 'Not Found'} - {account.handle ? account.handle :'Not Found'}
                </h5>
                <p className="card-text">{account.descreption ? account.descreption : 'Not Found'}</p>
                <div className="btn-group" role="group" aria-label="Basic example">
                  <button type="button" className="btn btn-primary" >
                    View Analytics
                  </button>
                  <button type="button" className="btn btn-danger" >
                    Delete
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      ) : ( null )}
    </>
  );
};

export { example };
export default Card;
