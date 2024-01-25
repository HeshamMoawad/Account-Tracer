import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import Calendar from "react-calendar";
import Analytics from "./Analytics/Analytics";
import axios from "axios";
import {CheckExistHandleURL} from "../../../Constants";
// import "react-calendar/dist/Calendar.css";
import "./AnalyticsPage.css";


const AnalyticsPage = () => {
    const { handle } = useParams();
    const [fetchDate, setFetchDate] = useState(new Date());
    const [currentSelectedDate, setCurrentSelectedDate] = useState(new Date());
    const [userInfo, setUserInfo] = useState(null);

    // fetch account info
    useEffect(() => {
        const params = new URLSearchParams({
            handle : handle.replace("@","")
        })
        // endpoint here
        axios  
            .get(CheckExistHandleURL + `?${params}`)
            .then(response => {setUserInfo(response.data);console.log(response)})
            .catch(error => console.log(`Fetching Error ${error}`))
    },[]);

    return (
        <div className="container text-left mt-5">
            <div className="row">
                <div
                    className="card mx-auto shadow-lg"
                    style={{ minWidth: "400px" }}
                >
                    <div className="card-body">
                        <div className="container text-center">
                            <div className="row">
                                {userInfo ? (
                                    <>
                                        <div className="col">
                                            <img
                                                className="img-fluid"
                                                src={userInfo.profileImgURL}
                                                alt=""
                                                id="account-img-as-logo"
                                            />
                                            <h1
                                                className="card-title h1"
                                                id="name"
                                            >
                                                {userInfo.name}
                                            </h1>
                                            <h2
                                                className="card-title h3"
                                                id="handle"
                                            >
                                                {userInfo.handle}
                                            </h2>
                                        </div>

                                        <div className="container col-3 mx-auto">
                                            <Calendar
                                                minDate={new Date(userInfo.minDate)}
                                                maxDate={new Date(userInfo.maxDate)}
                                                onClickDay={(v, e) => setCurrentSelectedDate(v)}
                                            />
                                            <div className="row">
                                            <button className="btn btn-outline-primary mt-3 col" onClick={()=>setFetchDate(currentSelectedDate)}>
                                                Fetch Data
                                            </button>
                                            <label className="h6 col mt-4 border border-secondary-subtle">
                                                {currentSelectedDate.getDate()} / {currentSelectedDate.getMonth()+1} / {currentSelectedDate.getFullYear()}
                                            </label></div>
                                        </div>
                                    </>
                                ) : (
                                    <h2 className="card-title h3" id="handle">
                                        Not Found {handle}
                                    </h2>
                                )}
                            </div>
                        </div>
                        {
                            userInfo ?
                            <Analytics handle={userInfo.handle} fetchDate = {fetchDate} /> :
                            null
                        }
                    </div>
                </div>
            </div>
        </div>
    );
};

export default AnalyticsPage;
