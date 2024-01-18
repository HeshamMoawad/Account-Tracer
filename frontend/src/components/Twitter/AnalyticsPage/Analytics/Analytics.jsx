import React, { useEffect, useState } from "react";
import LineInfo from "./LineInfo/LineInfo";
import axios from "axios";
import { AnalyticsURL } from "../../../../Constants";

const Analytics = (props) => {
    const { handle, fetchDate } = props;
    const [analytics, setAnalytics] = useState(null);

    useEffect(() => {
        axios
            .post(AnalyticsURL, {
                handle: handle,
                date: fetchDate.toISOString(),
            })
            .then((response) => setAnalytics(response.data)) // console.log(response)
            .catch((error) => console.log(error));
    }, [fetchDate]);

    return (
        <>
            {analytics ? (
                <div className="container" id="analytics-container">
                    <div className="row text-center">
                    <label className="h4 col mt-2">
                        {fetchDate.getDate()} /{" "}
                        {fetchDate.getMonth() + 1} /{" "}
                        {fetchDate.getFullYear()}
                    </label>
                    </div>
                    <LineInfo
                        title="Tweets"
                        value={analytics.tweets}
                        hasButton={true}
                        target={analytics.handle}
                        date={fetchDate}
                        key={Math.random()}
                    />
                    <LineInfo
                        title="Replies"
                        value={analytics.replies}
                        hasButton={true}
                        target={analytics.handle}
                        date={fetchDate}
                        key={Math.random()}
                    />
                    <LineInfo
                        title="Follow"
                        value={analytics.stats.follow}
                        key={Math.random()}
                    />
                    <LineInfo
                        title="UnFollow"
                        value={analytics.stats.unfollow}
                        key={Math.random()}
                    />
                    <LineInfo
                        title="Follow Back"
                        value={analytics.stats.followback}
                        key={Math.random()}
                    />
                    <LineInfo
                        title="Messages"
                        value={analytics.messages}
                        key={Math.random()}
                    />
                    <LineInfo
                        title="Tweets & Replies"
                        value={analytics.tweets + analytics.replies}
                        key={Math.random()}
                    />
                </div>
            ) : null}
        </>
    );
};

export default Analytics;
