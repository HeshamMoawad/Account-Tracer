import React from "react";
import "./AccountCard.css";
import { useNavigate } from "react-router-dom";

const AccountCard = (props) => {
  const account = props.account
  const navigate = useNavigate();

  const onClickHandler = ()=>{
    navigate(`/twitter/analytics/${account.account.handle}`)
  }

  return (
    <>
      {account ? ( 
        <div className="card mb-3 mx-auto shadow-lg" style={{ maxWidth: 540 }} id="cardlayer">
          <div className="row g-0" >
            <div className="col-md-4">
              <img
                src={account.profileImgURL}
                className="img-fluid"
                alt=""
                id="account-img"
              />
            </div>
            <div className="col-md-8">
              <div className="card-body">
                <h5 className="card-title">
                  {account.name ? account.name : 'Not Found'} - {account.account.handle ? account.account.handle :'Not Found'}
                </h5>
                <p className="card-text">{account.description ? account.description : 'Not Found'}</p>
                <div className="btn-group" role="group" aria-label="Basic example">
                  <button type="button" className="btn btn-primary" onClick={onClickHandler} >
                    View Analytics
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

// export { example };
export default AccountCard;
