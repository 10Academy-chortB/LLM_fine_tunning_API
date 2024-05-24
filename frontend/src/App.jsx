import { useState } from 'react';
import { data } from './data.js';
import './App.css';

function App() {
  const [search, setSearch] = useState('');

  console.log('Data:', data); // Add this line to verify the data is being imported correctly

  return (
    <div className='m-auto w3/4'>
      <form className="search-container">
        <input
          className='input'
          onChange={(e) => setSearch(e.target.value)}
          type="search"
          placeholder="Search"
          aria-label="Search"
        />
        <button className='button' type="submit">Search</button>
      </form>

      <table className='outer_table'>
        <thead>
          <tr>
            <th>Username</th>
            <th>Message</th>
            <th>URL</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {data.filter((item) => {
            return search.toLocaleLowerCase() === '' ? item : item.message.toLowerCase().includes(search);
          }).map((item) => {
            console.log('Item:', item); // Add this line to verify the data is being passed correctly
            return (
              <tr key={item.channel_username}>
                <td>{item.channel_username}</td>
                <td>{item.message}</td>
                <td>{item.url}</td>
                <td>{item.date}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

export default App;