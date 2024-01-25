import React from "react";
import IconButton from "./IconButton/IconButton";

const Filter = (props) => {
  const { filterProjects } = props;
  const { setFilterProjects } = props;
  const { projects } = props;

  const removeFilterProjectHandler = (f) => {
    const updatedList = filterProjects.filter((item) => item !== f);
    return updatedList;
  };

  const onClickButtonHandler = (f, e) => {
    const btn = e.target;
    if (String(btn.className).includes("active")) {
      setFilterProjects(removeFilterProjectHandler(f));
      btn.className = String(btn.className).replace("active","")
    } else {
      setFilterProjects([...filterProjects, btn.alt]);
      btn.className = String(btn.className) + "active"
    }
  };
  return (
    <>
      <div className="container col-lg-7" style={{"minHeight":"150px","marginTop":"20px"}}>
        {projects.length !== 0 ? (
          projects.map((item) => {
            return (
              <IconButton item={item} onClickButtonHandler={onClickButtonHandler} key={item.name}/>
            );
          })
        ) : (
          <div className="alert alert-warning text-center" role="alert">
            No Projects Found <br /> Please add one from admin panel
          </div>
        )}
      </div>
    </>
  );
};

export default Filter;
