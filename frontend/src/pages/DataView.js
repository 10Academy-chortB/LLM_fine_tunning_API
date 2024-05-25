import React from 'react';

const DataView = ({ match }) => {
  const { id } = match.params;


  return (
    <div>
      <h1>Data View for ID: {id}</h1>
      {/* Detailed data view */}
    </div>
  );
};

export default DataView;
