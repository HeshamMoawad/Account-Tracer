import React, { useState } from "react";

const IconButton = (props) => {
  const { item, onClickButtonHandler } = props;
  const [isHovering, setIsHovering] = useState(false);
  const [isToggled, setToggled] = useState(false);
  
  const mouseToggleHandler = () => {
    setToggled(!isToggled);
  };
  const mouseOverLeaveHandler = () => {
    setIsHovering(!isHovering);
  };

  return (
    <>
      <img
        src={item.imgURL}
        alt={item.name}
        type="button"
        className="icon-button"
        id="filter-btn"
        value={item.name}
        onClick={(e) => {
          mouseToggleHandler();
          onClickButtonHandler(item.name, e);
        }}
        style={{
          width: "80px",
          height: "70px",
          maxHeight: "70px",
          margin: isHovering ? "0px 12px 12px 12px" : "12px",
          padding: "6px",
          borderRadius: "50%",
          backgroundColor: isToggled
            ? item.color
            : isHovering
            ? item.color
            : "#51907B",
        }}
        onMouseEnter={mouseOverLeaveHandler}
        onMouseLeave={mouseOverLeaveHandler}
      />
    </>
  );
};

export default IconButton;
