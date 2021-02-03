import React from "react";
import ReactDOM from "react-dom";

function FilesBoxApp() {
  return "This is the React FilesBoxApp";
}

const domContainer = document.querySelector("#files-box-react-app");
ReactDOM.render(React.createElement(FilesBoxApp), domContainer);
