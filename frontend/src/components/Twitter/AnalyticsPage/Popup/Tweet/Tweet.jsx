import React from "react";
import "./Tweet.css";

const Tweet = (props) => {
    const { tweet, target, userInfo } = props;
    const tweetURL = `https://twitter.com/${target}/status/${tweet.conversation_id_str}`;
    return (
        <>
            <div className="container" id="tweet">
                <div className="row text-center" id="header">
                    <img
                        className="img"
                        src={userInfo.profileImgURL}
                        alt=""
                        id="account-img-as-logo"
                    />
                    <label className="h6 col">@{target}</label>
                    <label className="col" id="type">
                        Retweeted
                    </label>
                    {/* url Here */}
                    <a href={tweetURL} className="col text-center">
                        <button id="go-to-tweet">Tweet</button>
                    </a>
                </div>

                <div className="row" id="body">
                    <div className="">{tweet.full_text}</div>
                    {tweet.media_links.length >= 1 ? tweet.media_links.map((url)=>(
                        <img
                            className="img"
                            src={url}
                            alt=""
                            id="tweet-img"
                        />)
                    ) : null}
                </div>
                <div className="row" id="footer">
                    footer
                </div>
            </div>
        </>
    );
};

export default Tweet;
