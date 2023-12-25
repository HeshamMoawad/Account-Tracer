import React from "react";
import './Filter.css';
import logo from '../../../../assets/el alamia white.svg'

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
      btn.className = "btn col mt-2";
      setFilterProjects(removeFilterProjectHandler(f));
    } else {
      btn.className = "btn col mt-2 active btn-primary";
      setFilterProjects([...filterProjects, btn.alt]);
    }
  };

  return (
    <>
      <div className="container col-lg-7">
        {projects
          ? projects.map((item) => {
              return (
                <img
                  src={logo}//#{item.imgURL}
                  alt={item.name}
                  type="button"
                  className="img-fluid col shadow-lg bg-dark"
                  id="filter-btn"
                  // data-bs-toggle="button"
                  // aria-pressed="true"
                  value={item.name}
                  onClick={(e) => {
                    onClickButtonHandler(item, e);
                  }}
                  key={item.name}
                />
              );
            })
          : null}
      </div>
    </>
  );
};

export default Filter;
