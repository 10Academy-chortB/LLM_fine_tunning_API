import React, { useState } from 'react';
import axios from 'axios';
import SearchBar from '../components/SearchBar';
import DataDisplay from '../components/DataDisplay';

const Home = () => {
  const [data, setData] = useState([]);

  const fetchData = async (query = '', filter = '') => {
    const response = await axios.get('/api/data', {
      params: { query, filter }
    });
    setData(response.data);
  };

  return (
    <div>
      <SearchBar onSearch={(query) => fetchData(query)} />
      <DataDisplay data={data} />
    </div>
  );
};

export default Home;
