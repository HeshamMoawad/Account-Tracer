import React, { useEffect, useState } from "react";
import axios from "axios";
import {AccountTweetsURL , AccountRepliesURL} from "../../../../Constants";
import Tweet from "./Tweet/Tweet";
import Reply from "./Tweet/Reply";


const Popup = (props) => {
    const { name , target , date} = props;
    const [isShowed, setIsShowed] = useState(false);
    const [legacies, setLegacies] = useState(null);
    const [userInfo, setUserInfo] = useState(null);
    const onClickShowInfoHandler = () => setIsShowed(!isShowed);

    // set legacies from endpoint
    useEffect(() => {
        // endpoint here
        if (isShowed){
            console.log(`${date.getDate()}/${date.getMonth() + 1}/${date.getFullYear()}`)
            console.log(target , date,name)
            var url = "";
            if (name === "Tweets"){
                var url = AccountTweetsURL
            }
            else if (name === "Replies"){
                var url = AccountRepliesURL
            }
            axios
                .get(url+`?${new URLSearchParams({
                    date : `${date.getDate()}/${date.getMonth() + 1}/${date.getFullYear()}` ,
                    screen_name : target ,
                })}`)
                .then(response=>{setLegacies(response.data.data);setUserInfo(response.data.user);console.log(response.data)})
                .catch(error => console.log(`Fetching Error ${error}`))
        }
    },[isShowed]);

    return (
        <>
            <button
                className="btn btn-outline-secondary col"
                type="button"
                data-bs-toggle="offcanvas"
                data-bs-target="#offcanvasWithBothOptions"
                aria-controls="offcanvasWithBothOptions"
                onClick={onClickShowInfoHandler}
                style={{
                    minWidth: "100px",
                    maxWidth: "200px",
                    marginLeft: "250px",
                }}
            >
                Show {name}
            </button>
            {isShowed ? (
                <>
                    <div
                        className="offcanvas offcanvas-start show"
                        data-bs-scroll="true"
                        tabIndex={-1}
                        id="offcanvasWithBothOptions"
                        aria-labelledby="offcanvasWithBothOptionsLabel"
                        aria-modal="true"
                        role="dialog"
                        style={{ minWidth: "35vw" , backgroundColor:"transparent"}}
                    >
                        <div
                            className="offcanvas-header text-center"
                            style={{
                                borderBottom: "1px gray solid",
                                marginBottom: "10px",
                            }}
                        >
                            <h5
                                className="offcanvas-title h3"
                                id="offcanvasWithBothOptionsLabel"
                            >
                                {name}
                            </h5>
                            <button
                                type="button"
                                className="btn-close"
                                data-bs-dismiss="offcanvas"
                                aria-label="Close"
                                onClick={onClickShowInfoHandler}
                            />
                        </div>

                        <div className="offcanvas-body">
                            <div className="container">
                              {legacies ? (
                                // when legacies is null before loading endpoint
                                legacies.length === 0 ? (
                                    //*// When endpoint return empty list (no legacies)
                                    <div
                                        className="alert alert-warning"
                                        role="alert"
                                    >
                                        No {name} Found
                                    </div>
                                ) : (legacies.map((legacy)=>{
                                    if (name === "Tweets"){
                                        return <Tweet key={Math.random()} tweet={legacy} target={target} userInfo={userInfo}/>
                                    }
                                    else if (name === "Replies"){
                                        return <Reply key={Math.random()} tweet={legacy} target={target} userInfo={userInfo}/>
                                    }
                                    return null
                               
                            }))   //*  set map loop here for show all tweets  -- TweetsCards Here -- */
                            ) : (
                                // When loading endpoint data
                                <div className="container text-center mt-5">
                                    <div
                                        className="spinner-border"
                                        role="status"
                                        style={{
                                            minWidth: "80px",
                                            minHeight: "80px",
                                        }}
                                    >
                                        <span className="visually-hidden">
                                            Loading...
                                        </span>
                                    </div>
                                </div>
                            )}  
                            </div>
                            
                        </div>
                    </div>
                    <div
                        className="offcanvas-backdrop fade show"
                        onClick={onClickShowInfoHandler}
                    />
                </>
            ) : null}
        </>
    );
};

export default Popup;
